# Example to add experimental protos:
# EXTRA_EXTRA_DIRS="-I ~/go/src/arista/resources" EXTRA_EXTRA_PROTOS="~/go/src/arista/resources/arista/configlet.v1/configlet.proto ~/go/src/arista/resources/arista/configlet.v1/services.gen.proto" make
VENDORPATH=cloudvision-apis
EXTRAPATH=${PWD}/extra_cv_protos
EXTRA_EXTRA_DIRS?=
EXTRA_EXTRA_PROTOS?=
DUMMY := $(shell \
  rm -rf $(VENDORPATH); \
  git clone --single-branch --branch trunk https://github.com/aristanetworks/cloudvision-apis.git $(VENDORPATH); \
)

APIPATH=api

PYTHON ?= python3

VENDOR_PROTOS=$(shell find $(VENDORPATH) -name "*.proto")
EXTRA_PROTOS=$(shell find $(EXTRAPATH) -name "*.proto")

default: api

.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

api-dir:
	mkdir -p api
	rm -rf ./api/*
	touch ./api/__init__.py

api-models: api-dir
	$(PYTHON) -m grpc_tools.protoc -I $(VENDORPATH) -I $(EXTRAPATH) $(EXTRA_EXTRA_DIRS) --python_aristaproto_out=$(APIPATH) $(VENDOR_PROTOS) $(EXTRA_PROTOS) $(EXTRA_EXTRA_PROTOS)

api: api-dir api-models  ## Build/refresh gRPC bindings in ./api
	@rm -rf $(VENDORPATH)
	@pre-commit run insert-license --files $(shell find $(APIPATH)/ -name "*.py") || true
	@echo "--- done"
	@echo "If you got here, everything went well."
	@echo "All the output above is just because we use pre-commit to insert licenses into the generated files."
