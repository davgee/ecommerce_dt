check_flake8:
	flake8 models.py

check_pep8:
	pycodestyle models.py

lint: check_pep8 check_flake8
