from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Greeting SPA")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/greet")
async def greet(name: str = Query(..., description="Name to greet")):
    """Return a greeting message for the given name."""
    return {"greeting": f"Hello, {name}!"}

@app.get("/")
async def serve_spa(request):
    """Serve the SPA index page."""
    return FileResponse("templates/index.html", media_type="text/html")