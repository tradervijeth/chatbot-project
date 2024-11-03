from typing import Dict, List, Tuple
import re
import spacy
import random
from collections import deque

class EnhancedChatbot:
    def __init__(self):
        # Load spaCy model for NLP
        self.nlp = spacy.load("en_core_web_sm")
        
        # Maintain conversation context
        self.context_window = deque(maxlen=5)  # Keep last 5 exchanges
        self.user_info = {}  # Store user-specific information
        
        # Define personality traits
        self.personality = {
            "empathy_level": 0.8,  # High empathy
            "formality_level": 0.6,  # Moderately formal
            "verbosity": 0.7,  # Moderately verbose
        }
        
        # Enhanced knowledge base with contextual responses
        self.knowledge_base = {
            "personal_info": {
                "patterns": [
                    r"my name is (?P<name>\w+)",
                    r"i am (?P<age>\d+) years old",
                    r"i (?:am|work as) an? (?P<profession>\w+)",
                ],
                "responses": {
                    "name": [
                        "Nice to meet you, {name}! How can I help you today?",
                        "Hello {name}! I'll remember your name for our conversation.",
                    ],
                    "age": [
                        "Got it! I'll keep in mind that you're {age} years old.",
                        "Thank you for sharing that with me, {age} is a great age!",
                    ],
                    "profession": [
                        "Interesting! I'd love to hear more about your work as a {profession}.",
                        "Being a {profession} must be fascinating. What aspects of your work interest you most?",
                    ],
                }
            },
            "emotions": {
                "patterns": [
                    r"i feel (?P<emotion>happy|sad|angry|excited|worried|stressed)",
                    r"i am (?P<emotion>happy|sad|angry|excited|worried|stressed)",
                ],
                "responses": {
                    "happy": [
                        "I'm glad you're feeling happy! What's bringing you joy?",
                        "That's wonderful! It's great to hear you're in good spirits.",
                    ],
                    "sad": [
                        "I'm sorry to hear you're feeling sad. Would you like to talk about it?",
                        "It's okay to feel sad sometimes. Is there anything specific bothering you?",
                    ],
                    "angry": [
                        "I understand feeling angry can be overwhelming. What triggered this feeling?",
                        "I hear you. Sometimes taking a deep breath can help. Want to talk about what's bothering you?",
                    ],
                    "excited": [
                        "Your excitement is contagious! What's got you so thrilled?",
                        "That's fantastic! I'd love to hear what you're excited about!",
                    ],
                    "worried": [
                        "I understand being worried can be difficult. Would you like to share what's concerning you?",
                        "It's natural to feel worried sometimes. Let's talk about what's on your mind.",
                    ],
                    "stressed": [
                        "I hear you. Stress can be really challenging. What's causing you stress right now?",
                        "I'm here to listen. Sometimes talking about our stressors can help manage them better.",
                    ],
                }
            },
            "topics": {
                "work": {
                    "patterns": [r"at work", r"my job", r"my career", r"my boss", r"my colleagues"],
                    "responses": [
                        "How long have you been in this field?",
                        "What aspects of your work do you find most challenging?",
                        "Do you feel fulfilled in your current role?",
                    ]
                },
                "hobbies": {
                    "patterns": [r"hobby", r"free time", r"for fun", r"enjoy doing"],
                    "responses": [
                        "That sounds interesting! How did you get started with that?",
                        "What do you enjoy most about this hobby?",
                        "How often do you get to practice this hobby?",
                    ]
                }
            }
        }

    def extract_entities(self, text: str) -> Dict[str, str]:
        """Extract named entities and key information from user input."""
        doc = self.nlp(text)
        entities = {}
        
        # Extract named entities
        for ent in doc.ents:
            entities[ent.label_] = ent.text
            
        # Extract personal information using patterns
        for category, data in self.knowledge_base.items():
            if isinstance(data, dict) and "patterns" in data:
                for pattern in data["patterns"]:
                    match = re.search(pattern, text.lower())
                    if match:
                        entities.update(match.groupdict())
        
        return entities

    def update_user_info(self, entities: Dict[str, str]) -> None:
        """Update stored user information based on extracted entities."""
        self.user_info.update(entities)

    def analyze_sentiment(self, text: str) -> float:
        """Analyze the sentiment of user input."""
        doc = self.nlp(text)
        # Simple sentiment analysis based on positive/negative words
        return sum(token.sentiment for token in doc) / len(doc)

    def generate_contextual_response(self, user_input: str) -> str:
        """Generate a response based on context and user input."""
        # Extract entities and update user info
        entities = self.extract_entities(user_input)
        self.update_user_info(entities)
        
        # Update context window
        self.context_window.append(user_input)
        
        # Check for emotion or personal info patterns first
        for category, data in self.knowledge_base.items():
            if isinstance(data, dict) and "patterns" in data:
                for pattern in data["patterns"]:
                    match = re.search(pattern, user_input.lower())
                    if match:
                        matched_items = match.groupdict()
                        for key, value in matched_items.items():
                            if value in data["responses"]:
                                response = random.choice(data["responses"][value])
                                return response.format(**matched_items)
        
        # If no specific pattern matched, generate a response based on topic and context
        doc = self.nlp(user_input)
        
        # Check for topic-specific responses
        for topic, topic_data in self.knowledge_base["topics"].items():
            for pattern in topic_data["patterns"]:
                if re.search(pattern, user_input.lower()):
                    response = random.choice(topic_data["responses"])
                    
                    # Personalize response if we have user info
                    if "name" in self.user_info:
                        response = f"{self.user_info['name']}, {response}"
                    
                    return response
        
        # Default to context-aware general response
        context = " ".join(list(self.context_window))
        context_doc = self.nlp(context)
        
        # Generate a relevant response based on context
        if context_doc.similarity(doc) > 0.5:
            return "I see how this relates to what we were discussing. Can you tell me more?"
        else:
            return "That's an interesting new topic. Would you like to explore it further?"

    def format_response(self, response: str) -> str:
        """Format the response based on personality settings."""
        if self.personality["formality_level"] > 0.7:
            response = response.replace("you're", "you are").replace("I'm", "I am")
        
        if self.personality["empathy_level"] > 0.7 and "name" in self.user_info:
            if not response.startswith(self.user_info["name"]):
                response = f"{self.user_info['name']}, {response.lower()}"
        
        return response

    def chat(self, user_input: str) -> str:
        """Main chat function that handles the conversation flow."""
        if not user_input.strip():
            return "I didn't catch that. Could you please say something?"
        
        response = self.generate_contextual_response(user_input)
        formatted_response = self.format_response(response)
        return formatted_response