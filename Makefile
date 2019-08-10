test:
	py.test --cov=whichcraft --cov-report html
	open htmlcov/index.html | xdg-open htmlcov/index.html
