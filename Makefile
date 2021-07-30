build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
brain-games:
	poetry run brain-games
package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
python:
	poetry run python3
lint:
	poetry run flake8 brain_games
install:
	poetry install
check:
	poetry check
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime		
	
