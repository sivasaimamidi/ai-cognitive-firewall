import sys
import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from openenv.core.env_server import create_fastapi_app

# Add project root to sys.path for robust imports
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from server.environment import MessageRoutingEnvironment
from models import Observation, Action

# Standard OpenEnv manifest variables
WORKERS = int(os.getenv("WORKERS", "1"))   # Use 1 worker for stateful env
PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

# Create a single shared environment instance for statefulness
_shared_env = MessageRoutingEnvironment()

# Create the FastAPI app using the OpenEnv factory
# The env factory returns the shared instance so state persists across requests
app = create_fastapi_app(
    env=lambda: _shared_env,
    observation_cls=Observation,
    action_cls=Action,
)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_dashboard():
    dashboard_path = os.path.join(ROOT_DIR, "dashboard.html")
    if os.path.exists(dashboard_path):
        return FileResponse(dashboard_path)
    return {"status": "Dashboard not found"}

def main():
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT, workers=1)

if __name__ == "__main__":
    main()
