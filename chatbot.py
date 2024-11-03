import anthropic
from typing import Dict, List
from collections import deque
import os

class Chatbot:
    def __init__(self):
        # Initialize Anthropic client
        self.client = anthropic.Anthropic(
            api_key=os.getenv('ANTHROPIC_API_KEY')
        )
        
        # Maintain conversation context
        self.context_window = deque(maxlen=10)
        self.user_info = {}
        
        self.system_prompt = """You are a helpful and engaging chatbot assistant. 
        Maintain a friendly, conversational tone while being informative and helpful. 
        Remember details about the user and refer back to them naturally in conversation.
        Keep responses concise but informative."""

    def format_messages(self, user_input: str) -> list:
        """Format the conversation history and current input for Claude."""
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        for entry in self.context_window:
            messages.extend([
                {"role": "user", "content": entry['user']},
                {"role": "assistant", "content": entry['bot']}
            ])
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        return messages

    def chat(self, user_input: str) -> str:
        """Generate a response using Anthropic's Claude."""
        try:
            # Format the messages
            messages = self.format_messages(user_input)
            
            # Get response from Claude
            message = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                temperature=0.7,
                messages=messages
            )
            
            response = message.content[0].text
            
            # Update context window
            self.context_window.append({
                'user': user_input,
                'bot': response
            })
            
            return response

        except Exception as e:
            print(f"Error calling Anthropic API: {e}")
            return "I apologize, but I encountered an error. Could you please try again?"
        