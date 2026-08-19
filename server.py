from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from GetSystemInfo import Dashboard

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "web")), name="static")
Dashboard_ = Dashboard()


###################################
##main page
###################################
@app.get("/")
async def load_surface():
    file_path = BASE_DIR / "web" / "index.html"
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail="index.html")
    return FileResponse(str(file_path))

@app.api_route("/dashboard", methods=["GET","POST"])
async def get_dashboard():
    return Dashboard_.get_all_data()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4200)
