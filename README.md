<p align="center">
  <img src="http://logos.u2d.ai/msaCRUD_logo.png?raw=true" alt="msaCRUD Logo"/>
</p>

------
<p align="center">
    <em>msaCRUD - SQLModel/SQLAlchemy/FastAPI - DB Object CRUD/API Automation</em>
<br>
    Optimized for use with FastAPI/Pydantic. Generates CRUD Router based on SQLModel and SQLAlchemy.
<br>
  <a href="https://pypi.org/project/msaCRUD" target="_blank">
      <img src="https://img.shields.io/pypi/v/msaCRUD?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/msaCRUD" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/msaCRUD.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

------

**Documentation**: <a href="https://msaCRUD.u2d.ai/" target="_blank">msaCRUD Documentation (https://msaCRUD.u2d.ai/)</a>

------

## Main Dependencies

- fastapi[all]~=0.85.0 # FastAPI framework, high performance, easy to learn, fast to code, ready for production
- starlette~=0.20.4 # Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
- sqlmodel~=0.0.8 # SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
- sqlalchemy[asyncio]~=1.4.41 # Database Abstraction Library
- sqlalchemy_database~=0.0.7 # SQLAlchemy-Database provides shortcut functions to common database operations for SQLAlchemy ORM

## Usage

```python
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
```

## License Agreement

- `msaCRUD`Based on `MIT` open source and free to use, it is free for commercial use, but please show/list the copyright information about msaCRUD somewhere.


## How to create the documentation

We use mkdocs and mkdocsstring. The code reference and nav entry get's created virtually by the triggered python script /docs/gen_ref_pages.py while ``mkdocs`` ``serve`` or ``build`` is executed.

### Requirements Install for the PDF creation option:
PDF Export is using mainly weasyprint, if you get some errors here pls. check there documentation. Installation is part of the msaCRUD, so this should be fine.

We can now test and view our documentation using:

    mkdocs serve

Build static Site:

    mkdocs build


## Build and Publish
  
Build:  

    python setup.py sdist

Publish to pypi:

    twine upload dist/*
