from .base_agent import BaseAgent

class CodingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Coding Agent",
            role="Senior Software Engineer",
            goal="Write clean, documented, and efficient code following industry best practices."
        )

    async def execute(self, task_description: str, context: str = None) -> str:
        prompt = f"""
        You are the Coding Agent. Your task is to generate high-quality code.
        
        TASK: {task_description}
        CONTEXT: {context if context else 'No additional context provided.'}
        
        INSTRUCTIONS:
        1. Write clean, well-commented code.
        2. Include a brief explanation of the architecture.
        3. Provide usage examples or setup instructions.
        4. Use proper Markdown code blocks for syntax highlighting.
        """
        return await self.get_completion(prompt)

coding_agent = CodingAgent()