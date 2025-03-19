@echo off
python gen-dot.py > diagram.dot && dot -Tsvg -Gbgcolor=transparent diagram.dot -o diagram.svg
pause
