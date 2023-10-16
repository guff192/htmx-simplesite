from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import Settings
from app.crud import CRUD

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    db = CRUD.with_table('artist_info')
    random_artist = db.get_random()

    return templates.TemplateResponse(
      name='main.html',
      context={
        'request': request,
        'artist': random_artist
        }
    )
 

@router.get('/about', response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse(
      name='about.html',
      context={'request': request}
    )


@router.get('/catalog', response_class=HTMLResponse)
def catalog(request: Request):
    db = CRUD.with_table('artist_details')
    artists = db.get_all()

    def get_active_members(artist: dict):
        if 'members' not in artist:
            return [artist]

        return list(filter(lambda member: bool(member['active']), artist['members']))

    def get_website(artist: dict):
        return artist['urls'] if 'urls' in artist else artist['uri']

    return templates.TemplateResponse(
      name='catalog.html',
      context={
          'request': request,
          'artists': artists,
          'get_active_members': get_active_members,
          'get_website': get_website 
      }
    )

