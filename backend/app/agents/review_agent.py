from .base_agent import BaseAgent

class ReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Review Agent",
            role="Quality Assurance Expert",
            goal="Critically evaluate agent outputs to ensure accuracy, consistency, and high quality."
        )

    async def execute(self, task_description: str, context: str = None) -> str:
        prompt = f"""
        You are the Review Agent. Your task is to perform a quality assurance check on the provided material.
        
        TASK: {task_description}
        CONTENT TO REVIEW: {context if context else 'No content provided to review.'}
        
        INSTRUCTIONS:
        1. Assess the overall quality and accuracy.
        2. Identify any logical gaps, errors, or inconsistencies.
        3. Provide specific, constructive recommendations for improvement.
        4. Assign a final "Quality Score" (1-10).
        """
        return await self.get_completion(prompt)

review_agent = ReviewAgent()