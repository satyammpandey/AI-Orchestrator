from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from ..core.security import get_current_user

router = APIRouter(prefix="/agents", tags=["Agents"])

class AgentInfo(BaseModel):
    name: str
    type: str
    description: str
    capabilities: List[str]

@router.get("/", response_model=List[AgentInfo])
async def get_agents(current_user: dict = Depends(get_current_user)):
    """Get information about all available agents"""
    return [
        {
            "name": "Research Agent",
            "type": "research_agent",
            "description": "Specializes in gathering information and conducting research",
            "capabilities": ["Information gathering", "Source finding", "Data collection"]
        },
        {
            "name": "Analysis Agent",
            "type": "analysis_agent",
            "description": "Analyzes data and provides insights",
            "capabilities": ["Data analysis", "Pattern recognition", "Trend identification"]
        },
        {
            "name": "Coding Agent",
            "type": "coding_agent",
            "description": "Generates and debugs code",
            "capabilities": ["Code generation", "Bug fixing", "Architecture design"]
        },
        {
            "name": "Writing Agent",
            "type": "writing_agent",
            "description": "Creates high-quality written content",
            "capabilities": ["Report writing", "Technical documentation", "Content creation"]
        },
        {
            "name": "Review Agent",
            "type": "review_agent",
            "description": "Reviews and validates agent outputs",
            "capabilities": ["Quality assurance", "Consistency check", "Gap identification"]
        }
    ]