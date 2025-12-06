import random
from typing import List

class Chatbot:
    """Simple rule-based chatbot"""
    
    def __init__(self):
        self.greeting_responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Greetings! How are you doing?"
        ]
        
        self.positive_responses = [
            "I'm glad to hear that!",
            "That's wonderful!",
            "Great to hear you're satisfied!",
            "Excellent! I'm happy I could help."
        ]
        
        self.negative_responses = [
            "I'm sorry to hear that. How can I help improve the situation?",
            "I apologize for the inconvenience. Let me see what I can do.",
            "I understand your frustration. Let's work on resolving this.",
            "That's disappointing. I'll make sure your concern is addressed."
        ]
        
        self.neutral_responses = [
            "I understand. Can you tell me more?",
            "I see. What would you like to know?",
            "Okay. How else can I assist you?",
            "Got it. What can I help you with?"
        ]
        
    def get_response(self, user_message: str, sentiment: str) -> str:
        """Generate response based on user message and sentiment"""
        user_lower = user_message.lower()
        
        # Check for greetings
        if any(word in user_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return random.choice(self.greeting_responses)
        
        # Check for thanks
        if any(word in user_lower for word in ['thank', 'thanks', 'appreciate']):
            return "You're welcome! Anything else I can help with?"
        
        # Respond based on sentiment
        if sentiment == "Positive":
            return random.choice(self.positive_responses)
        elif sentiment == "Negative":
            return random.choice(self.negative_responses)
        else:
            return random.choice(self.neutral_responses)
