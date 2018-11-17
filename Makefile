.PHONY: test lint style

all: test

test:
	py.test --cov=./ --mypy --codestyle --docstyle --pylint --pylint-rcfile=pylintrc --pylint-error-types=RCWEF

lint:
	py.test --pylint -m pylint --pylint-rcfile=pylintrc --pylint-error-types=RCWEF

static:
	mypy -p bowtie
