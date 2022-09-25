<p align="center">
  <img src="http://logos.u2d.ai/msaCRUD_logo.png?raw=true" alt="msaCRUD Logo"/>
</p>

------
<p align="center">
    <em>msaCRUD - SQLModel/SQLAlchemy/FastAPI - DB Object CRUD/API Automation</em>
<br>
  <a href="https://pypi.org/project/msaCRUD" target="_blank">
      <img src="https://img.shields.io/pypi/v/msaCRUD?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypi.org/project/msaCRUD" target="_blank">
      <img src="https://img.shields.io/pypi/pyversions/msaCRUD.svg?color=%2334D058" alt="Supported Python versions">
  </a>
</p>

------

## Main Dependencies

- fastapi[all]~=0.85.0 # FastAPI framework, high performance, easy to learn, fast to code, ready for production
- starlette~=0.20.4 # Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
- sqlmodel~=0.0.8 # SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
- sqlalchemy[asyncio]~=1.4.41 # Database Abstraction Library
- sqlalchemy_database~=0.0.7 # SQLAlchemy-Database provides shortcut functions to common database operations for SQLAlchemy ORM


### Usage example
```python
{!./docs_src/home/index_first.py!}
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
