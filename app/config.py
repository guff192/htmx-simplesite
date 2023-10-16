from pathlib import Path
from typing import Any
from typing import Any

from fastapi.responses import HTMLResponse
from pydantic_settings import BaseSettings


APP_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    DEBUG: bool = True

    APP_DIR: Path = APP_DIR
    ROOT_DIR: Path = APP_DIR.parent

    DATA_DIR: Path = ROOT_DIR / 'data'

    STATIC_DIR: Path = APP_DIR / 'static'
    TEMPLATE_DIR: Path = APP_DIR / 'templates'

    FASTAPI_PROPERTIES: dict[str, Any] = {
        'title': 'Simple Site',
        'description': 'A simple htmx and tailwind site built with FastAPI',
        'version': '0.0.1',
        'default_response_class': HTMLResponse,  # Change default from JSONResponse
    }

    DISABLE_DOCS: bool = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        '''Creates dictionary of values to pass to FastAPI app
        as **kwargs.

        Returns:
            dict: This can be unpacked as **kwargs to pass to FastAPI app.
        '''
        fastapi_kwargs = self.FASTAPI_PROPERTIES
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    'openapi_url': None,
                    'openapi_prefix': None,
                    'docs_url': None,
                    'redoc_url': None,
                }
            )
        return fastapi_kwargs




