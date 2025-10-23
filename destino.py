from fastapi import APIRouter
from sqlmodel import select
from models import bus
from utils import get_session