import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    APP_HOST = str(os.getenv('APP_HOST'))
    APP_PORT = int(os.getenv('APP_PORT'))
    APP_RELOAD = bool(os.getenv('APP_RELOAD'))
