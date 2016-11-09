clean:
	rm *.pyc

lint:
	pep8 . --show-source --statistics

test:
	python -m unittest test_translator
