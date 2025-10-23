from fastapi import APIRouter
from sqlmodel import select
from models import conductor
from utils import get_session