from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.database import Base
from datetime import datetime

# 1. THE PARENT TABLE (Must be first)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    
    # This links the user to their tasks
    tasks = relationship("Task", back_populates="owner")

# 2. THE CHILD TABLE
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String, default="pending") # pending, processing, completed, failed
    
    # This line was causing the error - it links to 'users.id'
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Store the final result from AI here
    result = Column(JSON, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # This links the task back to the user
    owner = relationship("User", back_populates="tasks")
    subtasks = relationship("SubTask", back_populates="parent_task")

class SubTask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("tasks.id"))
    agent_type = Column(String) # research, coder, etc.
    instruction = Column(Text)
    output = Column(Text, nullable=True)
    status = Column(String, default="pending")

    parent_task = relationship("Task", back_populates="subtasks")