#Makefile

install: #установить зависимости
	poetry install

brain-games: #для быстроты  запуска brain-games
	poetry run brain-games

build: #check
	poetry build

publish: #публикация
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
