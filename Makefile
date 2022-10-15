list:
	pip3 list

install:
	python3 setup.py install

config:
	python3 -m spacy download en_core_web_sm
	python3 -m "nltk.downloader" all

all:
	make install
	make config
	make list

test:
	python3 -m pytest -v

delete:
	python3 setup.py clean --all

flake:
	flake8 --ignore=BLK100 --exclude=.git

uninstall:
	pip3 uninstall vocably

format:
	flake8 --max-line-length=120 --ignore=E305,E402,W503,BLK100



	
