.PHONY: all freeze check covercheck

SRC=.

VENV=./venv
BINPREFIX=$(VENV)/bin/
APP      = trip
PIP      = $(BINPREFIX)pip
COVERAGE = $(BINPREFIX)coverage
MANAGER  = manage.py
COVERFILE:=.coverage

freeze: $(VENV)
	$(PIP) freeze >| requirements.txt

install:
	virtualenv $(VENV)
	deps

$(VENV):
	virtualenv $@

deps: $(VENV)
	$(BINPREFIX)pip install -r requirements.txt

clean-dist:
	$(RM) -r dist

check:
	$(BINPREFIX)python $(MANAGER) test

