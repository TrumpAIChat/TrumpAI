from flask import Flask, request, jsonify
import random
import logging
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename="chat_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Mock AI responses
default_ai_responses = [
    "Hello! I'm Donald Trump, how can I help you today?",
    "That’s an excellent question, let me give you a tremendous answer.",
    "Let me tell you, I know a lot about that topic!",
    "Nobody knows this better than me, believe me!"
]

# AI Response Logic
def generate_ai_response(user_input):
    """Generate an AI response based on user input."""
    try:
        user_input = user_input.lower()
        if "economy" in user_input:
            return "The economy under my administration was the greatest ever, and everyone knows it."
        elif "election" in user_input:
            return "Elections were always a point of pride for me, winning is what I do best."
        elif "policy" in user_input:
            return "My policies were and remain the strongest, bringing prosperity like no one has seen before."
        else:
            return random.choice(default_ai_responses)
    except Exception as e:
        logging.error(f"Error generating AI response: {e}")
        return "I’m sorry, something went wrong with my tremendous brain."

# Utilities
class ChatHistory:
    """Manages chat history for each session."""
    def __init__(self):
        self.history = []

    def add_message(self, user_message, ai_response):
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_message,
            "ai": ai_response
        })

    def get_history(self):
        return self.history

chat_history = ChatHistory()

# Routes
@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat interactions."""
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()

        if not user_input:
            return jsonify({"error": "Message cannot be empty."}), 400

        logging.info(f"User input received: {user_input}")

        # Generate AI response
        ai_response = generate_ai_response(user_input)

        # Log and save chat history
        chat_history.add_message(user_input, ai_response)
        logging.info(f"AI response sent: {ai_response}")

        return jsonify({"user": user_input, "ai": ai_response, "history": chat_history.get_history()}), 200

    except Exception as e:
        logging.error(f"Error in chat endpoint: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

@app.route('/api/history', methods=['GET'])
def history():
    """API endpoint to retrieve chat history."""
    try:
        return jsonify(chat_history.get_history()), 200
    except Exception as e:
        logging.error(f"Error in history endpoint: {e}")
        return jsonify({"error": "Unable to retrieve chat history."}), 500

@app.route('/')
def index():
    """Home endpoint."""
    return "<h1>Welcome to the AI Chat Interface!</h1><p>Use the /api/chat endpoint to interact with the AI and /api/history to view your chat history.</p>"

if __name__ == '__main__':
    app.run(debug=True)
