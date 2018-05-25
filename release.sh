#!/bin/sh

python3 setup.py sdist
twine upload -r pypi --skip-existing dist/*
