from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path
#my
from dashboard import Dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="web"), name="static")
Dashboard_ = Dashboard()

@app.get("/")
async def load_surface():
	try:
		file_path = Path("/app/web/index.html")
		return FileResponse(str(file_path))
	except Exception as e:
		raise HTTPException(status_code=404, detail="index.html")

@app.get("/dashboard")
async def get_dashboard():
    return Dashboard_.get_all_data()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4200)
