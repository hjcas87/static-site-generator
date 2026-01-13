#!/bin/bash
export PYTHONPATH=$PYTHONPATH:.
python3 -m unittest discover -s src -p "test_*.py"