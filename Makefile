check_flake8:
	flake8 src/*.py

check_pep8:
	pycodestyle src/*.py

lint: check_pep8 check_flake8

migrate_db:
	alembic upgrade head

run:
	gunicorn --workers=2 src.service:app
