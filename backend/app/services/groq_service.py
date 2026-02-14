from groq import Groq
from ..core.config import settings
import logging

logger = logging.getLogger(__name__)

class GroqService:
    def __init__(self):
        # We check if the key exists to avoid the 'proxies' error on empty keys
        api_key = settings.GROQ_API_KEY
        if not api_key:
            logger.warning("GROQ_API_KEY is not set in .env file!")
        
        # Initialize the client
        self.client = Groq(api_key=api_key)

    async def get_chat_completion(self, messages, model="mixtral-8x7b-32768", temperature=0.1):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Groq API Error: {str(e)}")
            return f"Error: {str(e)}"

# Create one instance to be used across the app
groq_service = GroqService()