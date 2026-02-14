import sys
import os

print("=== AI Orchestrator Verification ===\n")

# Test imports
try:
    from app.core.config import settings
    print("✓ Config OK")
except Exception as e:
    print(f"✗ Config Error: {e}")
    sys.exit(1)

try:
    from app.core.database import Base, engine
    print("✓ Database OK")
except Exception as e:
    print(f"✗ Database Error: {e}")
    sys.exit(1)

try:
    from app.models.user import User
    print("✓ User model OK")
except Exception as e:
    print(f"✗ User model Error: {e}")
    sys.exit(1)

try:
    from app.models.task import Task, TaskStatus
    print("✓ Task model OK")
except Exception as e:
    print(f"✗ Task model Error: {e}")
    sys.exit(1)

try:
    from app.models.agent import Agent
    print("✓ Agent model OK")
except Exception as e:
    print(f"✗ Agent model Error: {e}")
    sys.exit(1)

try:
    from app.api import auth, tasks, agents, uploads
    print("✓ API routes OK")
except Exception as e:
    print(f"✗ API routes Error: {e}")
    sys.exit(1)

try:
    from app.services.groq_service import groq_service
    print("✓ Groq service OK")
except Exception as e:
    print(f"✗ Groq service Error: {e}")
    sys.exit(1)

print("\n=== All checks passed! ✓ ===")
print("You can now run: python -m uvicorn app.main:app --reload")