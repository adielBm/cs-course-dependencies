@echo off
python gen-dot.py > diagram.dot && dot -Tsvg diagram.dot -o diagram.svg
pause
