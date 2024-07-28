
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Dummy data to represent registered users
users_db = {
    "pranjal@gmail.com": "password",
    "pukar@gmail.com" : "password123"
}

class LoginRequest(BaseModel):
    email: str
    password: str

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/login")
async def login(request: LoginRequest):
    user_password = users_db.get(request.email)
    if user_password and user_password == request.password:
        return JSONResponse(content={"success": True, "message": "Login successful"}, status_code=200)
    else:
        return JSONResponse(content={"success": False, "message": "Invalid email or password"}, status_code=401)
