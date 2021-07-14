build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
brain-games:
	poetry run brain-game
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
python:
	poetry run python3
lint:
	poetry run flake8 brain_games
install:
	poetry install

selfcheck:
	poetry check

check: selfcheck test lint	

