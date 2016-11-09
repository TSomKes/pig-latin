clean:
	rm *.pyc

pep8:
	pep8 .

test:
	python -m unittest test_translator
