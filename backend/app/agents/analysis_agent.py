from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Analysis Agent",
            role="Data Analyst and Strategist",
            goal="Analyze information deeply to find patterns, insights, and strategic recommendations."
        )

    async def execute(self, task_description: str, context: str = None) -> str:
        # We use triple quotes (""") for long AI prompts to avoid Syntax Errors
        prompt = f"""
        You are the Analysis Agent. Your job is to take the following task and context, 
        and provide a deep, logical analysis.
        
        TASK: {task_description}
        CONTEXT: {context if context else 'No additional context provided.'}
        
        INSTRUCTIONS:
        1. Identify key patterns and insights.
        2. Evaluate potential risks or gaps.
        3. Provide clear, data-driven recommendations.
        4. Format your analysis professionally with clear sections.
        """
        
        return await self.get_completion(prompt)

analysis_agent = AnalysisAgent()