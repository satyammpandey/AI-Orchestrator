from fastapi import APIRouter, HTTPException, Request
import json, os

router = APIRouter()
USERS_FILE = os.path.join(os.getcwd(), "users_db.json")

def load_users():
    if not os.path.exists(USERS_FILE): return []
    with open(USERS_FILE, "r") as f:
        try: return json.load(f)
        except: return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

@router.post("/register")
async def register(request: Request):
    data = await request.json()
    users = load_users()
    if any(u['username'] == data['username'] for u in users):
        raise HTTPException(status_code=400, detail="Username already exists")
    users.append({
        "username": data['username'],
        "email": data['email'],
        "password": data['password'] # In a real app, use hashing!
    })
    save_users(users)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(request: Request):
    data = await request.json()
    users = load_users()
    user = next((u for u in users if u['username'] == data['username'] and u['password'] == data['password']), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "username": user['username']}

@router.post("/forgot-password")
async def forgot_password(request: Request):
    data = await request.json()
    users = load_users()
    user = next((u for u in users if u['email'] == data['email']), None)
    if not user:
        raise HTTPException(status_code=404, detail="Email not found")
    # For this demo, we just update the password to the new one provided
    user['password'] = data['new_password']
    save_users(users)
    return {"message": "Password updated successfully"}