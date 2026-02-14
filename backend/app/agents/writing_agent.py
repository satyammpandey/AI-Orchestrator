from .base_agent import BaseAgent

class WritingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Writing Agent",
            role="Professional Content Creator",
            goal="Create polished, engaging, and publication-ready written content."
        )

    async def execute(self, task_description: str, context: str = None) -> str:
        prompt = f"""
        You are the Writing Agent. Your task is to create high-quality written material.
        
        TASK: {task_description}
        CONTEXT: {context if context else 'No additional context provided.'}
        
        INSTRUCTIONS:
        1. Use a tone appropriate for the audience.
        2. Ensure logical flow and clear structure.
        3. Use professional formatting (headings, lists).
        4. Ensure the content is polished and ready for use.
        """
        return await self.get_completion(prompt)

writing_agent = WritingAgent()