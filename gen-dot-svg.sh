#!/bin/bash

python3 gen-dot.py > diagram.dot && dot -Tsvg -Gbgcolor=transparent diagram.dot -o diagram.svg
