from flask import Flask, request, render_template, jsonify
from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
from PIL import Image
import os
import gc
import cohere

app = Flask(__name__)

# Initialize Cohere API
cohere_client = cohere.Client('your API key')  # Replace with your key

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def load_model():
    print("Loading model and processor...")
    torch.cuda.empty_cache()
    gc.collect()
    
    max_memory = {
        0: "3.5GB",    # GPU
        "cpu": "12GB"  # CPU
    }
    
    processor = Blip2Processor.from_pretrained("local_blip_model/processor")
    model = Blip2ForConditionalGeneration.from_pretrained(
        "local_blip_model/model",
        device_map="auto",
        max_memory=max_memory,
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
    )
    return processor, model

# Load model when starting server
blip_processor, blip_model = load_model()

def enhance_response_with_cohere(blip_response):
    prompt = f"Make the following response more conversational and provide additional context if possible:\nResponse: {blip_response}\nEnhanced Response:"
    response = cohere_client.generate(
        model='command',
        prompt=prompt,
        max_tokens=100  # Adjust token length based on needs
    )
    return response.generations[0].text.strip()

def generate_response(image_path, question):
    image = Image.open(image_path).convert("RGB")
    inputs = blip_processor(images=image, text=question, return_tensors="pt")
    
    for k, v in inputs.items():
        if hasattr(v, "to"):
            inputs[k] = v.to(blip_model.device)
    
    output = blip_model.generate(**inputs, max_length=50)
    blip_response = blip_processor.decode(output[0], skip_special_tokens=True)
    
    # Enhance BLIP-2 response with Cohere
    enhanced_response = enhance_response_with_cohere(blip_response)
    return enhanced_response

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    if 'image' not in request.files:
        return jsonify({"error": "No image file"}), 400
    file = request.files['image']
    question = request.form.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)

    try:
        # Generate and enhance response
        response = generate_response(image_path, question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
