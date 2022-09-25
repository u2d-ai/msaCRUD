from typing import Optional, List
from sqlmodel import SQLModel, Field
from fastapi import FastAPI
from msaCRUD import MSASQLModelCrud


class TestArticle(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(title='ArticleTitle', max_length=200)
    description: Optional[str] = Field(default='', title='ArticleDescription', max_length=400)
    status: bool = Field(None, title='status')
    content: str = Field(title='ArticleContent')


class TestCategory(SQLModel, table=True):
    __table_args__ = {'extend_existing': True}
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(title='ArticleTitle', max_length=200)
    description: Optional[str] = Field(default='', title='ArticleDescription', max_length=400)
    status: bool = Field(None, title='status')
    content: str = Field(title='ArticleContent')


app = FastAPI()

# create your preferred DB Engine, create the schemas and then you can create the CRUD API models and add the router
# if you like

new_crud: MSASQLModelCrud = MSASQLModelCrud(model=TestArticle, engine=YOUR_DB_ENGINE).register_crud()
app.include_router(new_crud.router)

new_crud_second: MSASQLModelCrud = MSASQLModelCrud(model=TestCategory, engine=YOUR_DB_ENGINE).register_crud()
app.include_router(new_crud_second.router)

if __name__ == '__main__':
    pass