.PHONY: deps lint run

deps: requirements.txt
	pip3 install --requirement $<

SHELL_SCRIPTS = $(shell find . -type f -name '*.sh')
PYTHON_SCRIPTS = $(shell find . -type f -name '*.py')
lint: $(SHELL_SCRIPTS) $(PYTHON_SCRIPTS)
	shellcheck $(SHELL_SCRIPTS)
	flake8 $(PYTHON_SCRIPTS)

run: run.sh
	./$<