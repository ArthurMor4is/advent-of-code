# Makefile

new_advent_day:
	mkdir -p $(year)/p$(day)
	cp template.py $(year)/p$(day)/p$(day).py
	touch $(year)/p$(day)/input.txt
	touch $(year)/p$(day)/README.md

.PHONY: new_advent_day
