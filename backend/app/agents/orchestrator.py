from .base_agent import BaseAgent
import json
import logging

logger = logging.getLogger(__name__)

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Orchestrator",
            role="Task Decomposer and Manager",
            goal="Break down complex user requests into logical sub-tasks for specialized agents."
        )

    async def plan_task(self, user_prompt: str):
        """The Orchestrator takes one big prompt and makes it a list of small tasks."""
        prompt = f"""
        Analyze this user request: "{user_prompt}"
        Break it down into exactly 3 specialized sub-tasks.
        Respond ONLY with a JSON list in this format:
        [
            {{"agent": "research_agent", "task": "Step 1 description"}},
            {{"agent": "writing_agent", "task": "Step 2 description"}},
            {{"agent": "review_agent", "task": "Step 3 description"}}
        ]
        """
        response = await self.get_completion(prompt)
        try:
            # We clean the response to ensure it's pure JSON
            clean_json = response.strip().replace("```json", "").replace("```", "")
            return json.loads(clean_json)
        except Exception as e:
            logger.error(f"Failed to parse Orchestrator plan: {e}")
            return []

orchestrator_agent = OrchestratorAgent()