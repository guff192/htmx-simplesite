from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import Settings


settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
      name='shared/main.html',
      context={'request': request},
    )
