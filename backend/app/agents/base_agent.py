from ..services.groq_service import groq_service

class BaseAgent:
    def __init__(self, name: str, role: str, goal: str):
        self.name = name
        self.role = role
        self.goal = goal

    async def get_completion(self, prompt: str):
        """This is the universal method that all agents use to talk to Groq AI."""
        messages = [
            {
                "role": "system", 
                "content": f"You are the {self.name}. Your role is {self.role}. Your goal is {self.goal}."
            },
            {"role": "user", "content": prompt}
        ]
        return await groq_service.get_chat_completion(messages)