#!/usr/bin/env bash

set -e
set -x

mypy msaCRUD
flake8 msaCRUD docs_src
black msaCRUD docs_src --check
isort msaCRUD docs_src scripts --check-only

