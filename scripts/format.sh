#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --in-place msaCRUD docs_src --exclude=__init__.py
black msaCRUD docs_src
isort msaCRUD docs_src
