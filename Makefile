lint:
	flake8 gendiff tests

install:
	uv pip install -e .

check:
	make lint
	pytest