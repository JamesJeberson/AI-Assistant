from flask import Flask, request, jsonify, render_template
from model import llama3_response, granite_response, mixtral_response
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')
    tone = data.get('tone', 'formal')  # Default tone is 'formal'
    
    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400
    
    if tone == 'formal':
        system_prompt = "You are an professional AI assistant helping with customer inquiries. Provide a helpful and concise response."
    elif tone == 'casual':
        system_prompt = "You are a casual and friendly AI assistant helping with customer inquiries. Provide friendly response."
    elif tone == 'cheerful':
        system_prompt = "You are a cheerful and funny AI assistant helping with customer inquiries. Provide funny response."
    else:
        return jsonify({"error": "Invalid tone selection"}), 400
    
    start_time = time.time()
    
    try:
        if model == 'llama3':
            result = llama3_response(system_prompt, user_message)
        elif model == 'granite':
            result = granite_response(system_prompt, user_message)
        elif model == 'mixtral':
            result = mixtral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400
        
        result['duration'] = time.time() - start_time
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
