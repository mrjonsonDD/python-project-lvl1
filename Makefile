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

