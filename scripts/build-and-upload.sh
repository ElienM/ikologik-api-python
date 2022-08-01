#!/usr/bin/env bash

clear

rm -Rf ./build
rm -Rf ./dist
rm -Rf ./ikologikapi.egg-info

./venv/bin/python setup.py bdist_wheel
./venv/bin/python -m pip install --upgrade twine
./venv/bin/twine upload dist/*