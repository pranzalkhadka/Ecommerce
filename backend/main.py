
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

users_db = {
    "pranjal@gmail.com": "password",
    "pukar@gmail.com" : "password123"
}

class LoginRequest(BaseModel):
    email: str
    password: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(request: LoginRequest):
    user_password = users_db.get(request.email)
    if user_password and user_password == request.password:
        return JSONResponse(content={"success": True, "message": "Login successful"}, status_code=200)
    else:
        return JSONResponse(content={"success": False, "message": "Invalid email or password"}, status_code=401)
