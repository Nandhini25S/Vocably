list:
	pip3 list

install:
	python3 setup.py install

config:
	python3 -m pip install pylint pytest
	python3 -m spacy download en_core_web_sm
	python3 -m "nltk.downloader" all

delete:
	python3 setup.py clean --all

flake:
	flake8 --ignore=BLK100 --exclude=.git

uninstall:
	pip3 uninstall vocably

format:
	flake8 --max-line-length=120 --ignore=BLK100 --exclude=build --format="%(path)s:%(row)d:%(col)d: %(code)s %(text)s" --show-source --statistics

# Language: makefile
lint:
	pylint src/vocably --disable=C0201
	pylint src/vocably --disable=C0201 > pylint.txt

test:
	python test
