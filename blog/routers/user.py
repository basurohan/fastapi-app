from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from blog.repository import user_repository
from sqlalchemy.orm import Session
from blog import schemas
from blog.database import get_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserDTO)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user_repository.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserDTO)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return user_repository.get_by_id(id, db)
