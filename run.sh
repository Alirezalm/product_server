#!/bin/zsh

echo "Running Server..."

# make sure dependencies are installed and python venv is activated.
pip install -r req.txt

uvicorn server:app --reload --host 0.0.0.0 --port 8000
