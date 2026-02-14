from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from ..core.database import Base
from datetime import datetime

class Agent(Base):
    __tablename__ = "agents"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    type = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)