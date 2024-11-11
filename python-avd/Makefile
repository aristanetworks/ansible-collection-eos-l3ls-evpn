CURRENT_DIR = $(shell pwd)
ANSIBLE_AVD_DIR ?= ..
SCRIPTS_DIR = $(CURRENT_DIR)/scripts

# export PYTHONPATH=$(CURRENT_DIR) # Uncomment to test from source

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dep
dep: compile-templates compile-schemas ## compile Jinja templates & AVD schemas

.PHONY: build
build: ## Build pyavd package
	pip3 install build
	rm -rf $(CURRENT_DIR)/build/ $(CURRENT_DIR)/dist/ $(CURRENT_DIR)/pyavd.egg-info/
	python3 -m build --wheel

.PHONY: publish
publish: ## Publish pyavd package to PyPI (build first)
	pip3 install twine && \
	twine check dist/* && \
	twine upload -r testpypi dist/* && \
	twine upload dist/*

.PHONY: compile-schemas
compile-schemas:
	$(SCRIPTS_DIR)/build_schemas.py

.PHONY: compile-templates
compile-templates:
	$(SCRIPTS_DIR)/compile_templates.py
