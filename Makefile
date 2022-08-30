.PHONY: setup
setup:
	python3 -m venv venv

.PHONY: install
install: setup
	pip install -r requirements.txt

.PHONY: save
save:
	pip freeze >requirements.txt
