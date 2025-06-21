from fastapi import FastAPI
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace * with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the auth router
app.include_router(auth_router)
