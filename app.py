from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.chatbot import EnhancedChatbot
import os

app = Flask(__name__)
CORS(app)

# Initialize chatbot
chatbot = EnhancedChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Get response from enhanced chatbot
        response = chatbot.chat(user_message)
        
        return jsonify({
            'response': response,
            'user_info': chatbot.user_info
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)