from typing import Any, Dict, List
import json

def format_agent_output(agent_name: str, output: str) -> Dict[str, Any]:
    """Format agent output for display"""
    return {
        "agent": agent_name,
        "output": output,
        "timestamp": None  # Add timestamp if needed
    }

def validate_subtask(subtask: Dict) -> bool:
    """Validate subtask structure"""
    required_fields = ["id", "agent", "description"]
    return all(field in subtask for field in required_fields)

def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal"""
    return "".join(c for c in filename if c.isalnum() or c in "._- ")