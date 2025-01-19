import random
import logging
from datetime import datetime

class TrumpAIPersona:
    """
    This class encapsulates the personality of an AI Donald Trump.
    It generates responses in a characteristic style based on the input context and tracks conversational state.
    """

    def __init__(self):
        self.key_phrases = {
            "greeting": [
                "Hello! It's Donald Trump, the one and only.",
                "Hi there, believe me, it's great to talk to you.",
                "Nobody says hello better than me. Tremendous greeting!"
            ],
            "economy": [
                "Let me tell you, the economy under my leadership was the best ever.",
                "The numbers, believe me, were absolutely incredible.",
                "Everyone knows my economic policies were tremendous."
            ],
            "success": [
                "I’m a winner, and winning is what I do best.",
                "Success follows me wherever I go, believe me.",
                "Nobody achieves success like I do."
            ],
            "humor": [
                "I once said, 'You’re fired!' and people loved it.",
                "My jokes are the best, people tell me they laugh like never before.",
                "Tremendous sense of humor, that’s what I have."
            ],
            "policy": [
                "My policies were always strong, the best policies anyone has ever seen.",
                "Nobody crafts policies better than I do, believe me.",
                "Every policy I made was designed for winning."
            ],
            "default": [
                "I know a lot about this topic, more than anyone, really.",
                "Nobody knows more about this than I do, believe me.",
                "That’s a great question, and I’ll give you the best answer."
            ]
        }
        self.conversation_log = []  # Tracks the conversation state

        # Configure logging
        logging.basicConfig(
            filename="trump_ai_persona.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def generate_response(self, topic):
        """Generates a response based on the given topic and logs the interaction."""
        try:
            responses = self.key_phrases.get(topic, self.key_phrases["default"])
            response = random.choice(responses)

            # Log the response
            logging.info(f"Generated response for topic '{topic}': {response}")

            # Add to conversation log
            self.conversation_log.append({
                "timestamp": datetime.now().isoformat(),
                "topic": topic,
                "response": response
            })

            return response
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "I’m sorry, something went wrong with my tremendous brain."

    def add_custom_phrase(self, topic, phrase):
        """Adds a custom phrase to a specific topic."""
        if topic in self.key_phrases:
            self.key_phrases[topic].append(phrase)
        else:
            self.key_phrases[topic] = [phrase]
        logging.info(f"Custom phrase added to topic '{topic}': {phrase}")

    def list_phrases(self, topic):
        """Lists all phrases under a specific topic."""
        phrases = self.key_phrases.get(topic, [])
        logging.info(f"Listing phrases for topic '{topic}': {phrases}")
        return phrases

    def export_conversation_log(self, file_name="conversation_log.txt"):
        """Exports the entire conversation log to a text file."""
        try:
            with open(file_name, "w") as log_file:
                for entry in self.conversation_log:
                    log_file.write(f"{entry['timestamp']} - Topic: {entry['topic']} - Response: {entry['response']}\n")
            logging.info(f"Conversation log successfully exported to {file_name}")
        except Exception as e:
            logging.error(f"Error exporting conversation log: {e}")

    def analyze_conversation(self):
        """Analyzes the conversation log for insights, such as most discussed topics."""
        topic_counts = {}
        for entry in self.conversation_log:
            topic = entry["topic"]
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

        most_discussed = max(topic_counts, key=topic_counts.get) if topic_counts else None
        analysis = {
            "total_interactions": len(self.conversation_log),
            "most_discussed_topic": most_discussed,
            "topic_counts": topic_counts
        }

        logging.info(f"Conversation analysis: {analysis}")
        return analysis

# Example usage of TrumpAIPersona
if __name__ == "__main__":
    trump_ai = TrumpAIPersona()

    # Example interactions
    print(trump_ai.generate_response("greeting"))
    print(trump_ai.generate_response("economy"))
    print(trump_ai.generate_response("success"))
    print(trump_ai.generate_response("humor"))
    print(trump_ai.generate_response("unknown"))  # Should use default phrases

    # Adding a custom phrase
    trump_ai.add_custom_phrase("economy", "The stock market was the highest under my watch, believe me.")
    print(trump_ai.list_phrases("economy"))

    # Exporting and analyzing conversation
    trump_ai.export_conversation_log()
    print(trump_ai.analyze_conversation())
