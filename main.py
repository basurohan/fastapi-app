import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blogs')
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    '''
        /blogs?limit=20&published=true
    '''
    if published:
        return { 'data': f'{limit} published blogs from the db' }
    else:
        return { 'data': f'{limit} blogs from the db' }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog created with title {blog.title}'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)