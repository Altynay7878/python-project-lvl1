#Makefile

install: #установить зависимости
	poetry install

brain-games: #для быстроты  запуска brain-games
	poetry run brain-games

brain-even: #для быстроты запуска brain-even
	poetry run brain-even

brain-calc: #для быстроты запуска brain_calc
	poetry run brain-calc

brain-gcd: #для быстроты запуска brain-gcd
	poetry run brain-gcd

brain-progression: #для быстроты запуска brain-progression
	poetry run brain-progression

brain-prime: #для быстроты запуска brain-progression
	poetry run brain-prime

build: #check
	poetry build

publish: #публикация
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

make-lint: #проверка кода линтером flake8
	poetry run flake8 brain_games
