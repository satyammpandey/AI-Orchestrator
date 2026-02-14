from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Research Agent",
            role="Expert Researcher",
            goal="Provide comprehensive research, facts, and simulated sources for any topic."
        )

    async def execute(self, task_description: str, context: str = None) -> str:
        prompt = f"""
        You are the Research Agent. Your task is to provide a detailed research report.
        
        TASK: {task_description}
        CONTEXT: {context if context else 'No additional context provided.'}
        
        INSTRUCTIONS:
        1. Provide key facts and detailed information.
        2. Simulate relevant sources or references.
        3. Identify important data points.
        4. Organize the report with clear headings and bullet points.
        """
        return await self.get_completion(prompt)

research_agent = ResearchAgent()