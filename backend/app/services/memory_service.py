from typing import Dict, List, Optional
import json

class MemoryService:
    """In-memory storage for task context and agent communication"""
    
    def __init__(self):
        self.task_memory: Dict[int, Dict] = {}
    
    def store_task_context(self, task_id: int, context: Dict):
        """Store context for a task"""
        if task_id not in self.task_memory:
            self.task_memory[task_id] = {
                "context": {},
                "agent_outputs": {},
                "shared_data": {}
            }
        self.task_memory[task_id]["context"].update(context)
    
    def store_agent_output(self, task_id: int, agent_name: str, output: any):
        """Store output from an agent"""
        if task_id not in self.task_memory:
            self.task_memory[task_id] = {
                "context": {},
                "agent_outputs": {},
                "shared_data": {}
            }
        self.task_memory[task_id]["agent_outputs"][agent_name] = output
    
    def get_agent_output(self, task_id: int, agent_name: str) -> Optional[any]:
        """Retrieve output from a specific agent"""
        if task_id in self.task_memory:
            return self.task_memory[task_id]["agent_outputs"].get(agent_name)
        return None
    
    def get_all_agent_outputs(self, task_id: int) -> Dict:
        """Get all agent outputs for a task"""
        if task_id in self.task_memory:
            return self.task_memory[task_id]["agent_outputs"]
        return {}
    
    def get_task_context(self, task_id: int) -> Dict:
        """Get full context for a task"""
        return self.task_memory.get(task_id, {})
    
    def share_data(self, task_id: int, key: str, value: any):
        """Share data between agents for a task"""
        if task_id not in self.task_memory:
            self.task_memory[task_id] = {
                "context": {},
                "agent_outputs": {},
                "shared_data": {}
            }
        self.task_memory[task_id]["shared_data"][key] = value
    
    def get_shared_data(self, task_id: int, key: str) -> Optional[any]:
        """Retrieve shared data"""
        if task_id in self.task_memory:
            return self.task_memory[task_id]["shared_data"].get(key)
        return None
    
    def clear_task_memory(self, task_id: int):
        """Clear memory for a completed task"""
        if task_id in self.task_memory:
            del self.task_memory[task_id]

memory_service = MemoryService()