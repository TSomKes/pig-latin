clean:
	rm *.pyc

pep8:
	pep8 . --show-source --statistics

test:
	python -m unittest test_translator
