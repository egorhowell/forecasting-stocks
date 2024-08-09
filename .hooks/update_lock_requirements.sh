#!/bin/bash

poetry lock
poetry export -f requirements.txt --output requirements.txt --without-hashes
git add poetry.lock requirements.txt