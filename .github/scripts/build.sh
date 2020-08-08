#!/bin/bash

rm -rf build
python -m pip install wheel
python -m pip install -r requirements.txt --target build
mkdir -p build/adgbot
cp adgbot/*.py build/adgbot
cp -R secrets build
cd build
chmod -R 755 .
zip -r ../build.zip .
