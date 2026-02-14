from fastapi import APIRouter, BackgroundTasks, Request, UploadFile, File, Form
import json, os, asyncio, datetime
from groq import Groq
from pydantic import BaseModel
from typing import Optional, List
from app.utils.file_processor import extract_text
from app.utils.search_tool import perform_web_search

router = APIRouter()
DB_FILE = os.path.join(os.getcwd(), "tasks_db.json")

# 🎯 YOUR GROQ BRAIN
client = Groq(api_key="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") 

def load_db():
    if not os.path.exists(DB_FILE): return []
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except: return []

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

async def run_structured_ai_logic(task_id, title, description):
    try:
        db = load_db()
        # 1. ORCHESTRATOR -> 2. RESEARCHER -> 3. ANALYST -> 4. CODER -> 5. WRITER
        agent_steps = [
            "Orchestrator: Defining Strategy",
            "Researcher: Scanning Global Data",
            "Analyst: Evaluating Context",
            "Coder: Validating Technicals",
            "Writer: Finalizing Intelligence"
        ]
        
        for i, step_title in enumerate(agent_steps):
            db = load_db()
            for t in db:
                if str(t["id"]) == str(task_id):
                    if i == 0: t["subtasks"] = []
                    # Mark previous as completed
                    if i > 0: t["subtasks"][i-1]["status"] = "completed"
                    t["subtasks"].append({"id": i, "title": step_title, "status": "in_progress"})
                    save_db(db)
                    break
            
            if i == 1: # Researcher Step
                web_data = perform_web_search(title)
            else:
                await asyncio.sleep(1) # Simulation for other agents

        # Final Writer Output
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Act as a 5-Agent Collective. Provide a Dossier with headers: MISSION STRATEGY, GLOBAL DATA, ANALYTICAL VERDICT, TECHNICAL ARCHITECTURE, EXECUTIVE SUMMARY. Use ALL CAPS for headers."},
                {"role": "user", "content": f"Project: {title}\nPrompt: {description}"}
            ]
        )
        answer = completion.choices[0].message.content
        
        db = load_db()
        for t in db:
            if str(t["id"]) == str(task_id):
                t["status"] = "completed"
                t["subtasks"][-1]["status"] = "completed"
                t["final_result"] = answer
                save_db(db); break
    except Exception as e: print(f"Error: {e}")

@router.post("/{task_id}/chat")
async def chat_with_task(task_id: str, request: Request):
    try:
        data = await request.json()
        user_msg = data.get("message")
        agent_type = data.get("agent_type", "Orchestrator")
        
        db = load_db()
        task = next((t for t in db if str(t["id"]) == str(task_id)), None)
        context = task.get('final_result') if task else "Direct uplink established."

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"You are the {agent_type}. Provide structured info with ALL CAPS headers. Use triple backticks for code."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_msg}"}
            ]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"response": "Uplink Error. Check Backend."}

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    db = load_db()
    new_db = [t for t in db if str(t["id"]) != str(task_id)]
    save_db(new_db)
    return {"message": "Deleted"}

@router.post("/")
@router.post("")
async def create_task(bg: BackgroundTasks, title: str = Form(...), description: str = Form(...), file: Optional[UploadFile] = File(None)):
    db = load_db()
    new_id = str(int(datetime.datetime.now().timestamp()))
    new_task = {
        "id": new_id, "title": title, "description": description, "status": "in_progress",
        "subtasks": [], "final_result": None, "created_at": datetime.datetime.utcnow().isoformat()
    }
    db.append(new_task); save_db(db)
    bg.add_task(run_structured_ai_logic, new_id, title, description)
    return new_task

@router.get("/")
@router.get("")
async def get_tasks():
    return sorted(load_db(), key=lambda x: x.get('created_at', ''), reverse=True)