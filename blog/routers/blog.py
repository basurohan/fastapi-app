from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from blog import schemas, oauth2
from blog.repository import blog_repository
from blog.database import get_db


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.create(request, db)


@router.get('/', response_model=List[schemas.BlogDTO])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_all(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogDTO)
def get_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.get_by_id(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repository.delete(id, db)
