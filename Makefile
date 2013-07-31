all: .installed test
test: bin/nosetests bin/flake8

.installed: 
	virtualenv .
	bin/pip install -U setuptools
	bin/python bootstrap.py
	bin/buildout
	touch .installed

bin/nosetests:
	@echo "==== Running nosetests ===="
	@bin/nosetests

bin/flake8:
	@echo "==== Running Flake8 ===="
	@bin/flake8 substanced_multilingual *.py

clean:
	rm -rf eggs lib include parts bin

.PHONY: bin/flake8 bin/nosetests
