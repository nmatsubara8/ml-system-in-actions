DOCKER_REPOSITORY := shibui/ml-system-in-actions

ABSOLUTE_PATH := $(shell pwd)

DOCKERFILE := Dockerfile
DOCKER_COMPOSE := dockercompose.yaml
IMAGE_VERSION := 0.0.1


HORIZONTAL_MICROSERVICE_PATTERN := horizontal_microservice_pattern
HORIZONTAL_MICROSERVICE_PATTERN_PATH := $(ABSOLUTE_PATH)/$(HORIZONTAL_MICROSERVICE_PATTERN)
HORIZONTAL_MICROSERVICE_PATTERN_SETOSA_PORT := 8000
HORIZONTAL_MICROSERVICE_PATTERN_VERSICOLOR_PORT := 8001
HORIZONTAL_MICROSERVICE_PATTERN_VIRGINICA_PORT := 8002

HORIZONTAL_MICROSERVICE_PATTERN_PROXY_PORT := 9000

.PHONY: build_setosa
build_setosa:
	docker build \
		-t $(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_setosa_$(IMAGE_VERSION) \
		-f ./$(DOCKERFILE).service.setosa \
		.
	
.PHONY: run_setosa
run_setosa:
	docker run \
		-d \
		--name $(HORIZONTAL_MICROSERVICE_PATTERN)_setosa \
		-e MODE:setosa \
		-e PORT:$(HORIZONTAL_MICROSERVICE_PATTERN_SETOSA_PORT) \
		-p $(HORIZONTAL_MICROSERVICE_PATTERN_SETOSA_PORT):$(HORIZONTAL_MICROSERVICE_PATTERN_SETOSA_PORT) \
		$(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_setosa_$(IMAGE_VERSION)

.PHONY: stop_setosa
stop_setosa:
	docker rm -f $(HORIZONTAL_MICROSERVICE_PATTERN)_setosa


.PHONY: build_versicolor
build_versicolor:
	docker build \
		-t $(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_versicolor_$(IMAGE_VERSION) \
		-f ./$(DOCKERFILE).service.versicolor \
		.
	
.PHONY: run_versicolor
run_versicolor:
	docker run \
		-d \
		--name $(HORIZONTAL_MICROSERVICE_PATTERN)_versicolor \
		-e MODE:versicolor \
		-e PORT:$(HORIZONTAL_MICROSERVICE_PATTERN_VERSICOLOR_PORT) \
		-p $(HORIZONTAL_MICROSERVICE_PATTERN_VERSICOLOR_PORT):$(HORIZONTAL_MICROSERVICE_PATTERN_VERSICOLOR_PORT) \
		$(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_versicolor_$(IMAGE_VERSION)

.PHONY: stop_versicolor
stop_versicolor:
	docker rm -f $(HORIZONTAL_MICROSERVICE_PATTERN)_versicolor

.PHONY: build_virginica
build_virginica:
	docker build \
		-t $(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_virginica_$(IMAGE_VERSION) \
		-f ./$(DOCKERFILE).service.virginica \
		.
	
.PHONY: run_virginica
run_virginica:
	docker run \
		-d \
		--name $(HORIZONTAL_MICROSERVICE_PATTERN)_virginica \
		-e MODE:virginica \
		-e PORT:$(HORIZONTAL_MICROSERVICE_PATTERN_VIRGINICA_PORT) \
		-p $(HORIZONTAL_MICROSERVICE_PATTERN_VIRGINICA_PORT):$(HORIZONTAL_MICROSERVICE_PATTERN_VIRGINICA_PORT) \
		$(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_virginica_$(IMAGE_VERSION)

.PHONY: stop_virginica
stop_virginica:
	docker rm -f $(HORIZONTAL_MICROSERVICE_PATTERN)_virginica

.PHONY: build_proxy
build_proxy:
	docker build \
		-t $(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_proxy_$(IMAGE_VERSION) \
		-f ./$(DOCKERFILE).proxy \
		.
	
.PHONY: run_proxy
run_proxy:
	docker run \
		-d \
		--name $(HORIZONTAL_MICROSERVICE_PATTERN)_proxy \
		-e MODE:proxy \
		-e PORT:$(HORIZONTAL_MICROSERVICE_PATTERN_PROXY_PORT) \
		-p $(HORIZONTAL_MICROSERVICE_PATTERN_PROXY_PORT):$(HORIZONTAL_MICROSERVICE_PATTERN_PROXY_PORT) \
		$(DOCKER_REPOSITORY):$(HORIZONTAL_MICROSERVICE_PATTERN)_proxy_$(IMAGE_VERSION)

.PHONY: stop_proxy
stop_proxy:
	docker rm -f $(HORIZONTAL_MICROSERVICE_PATTERN)_proxy

.PHONY: build_all
build_all: build_setosa build_versicolor build_virginica build_proxy

.PHONY: run_all
run_all: run_setosa run_versicolor run_virginica run_proxy

.PHONY: stop_all
stop_all: stop_setosa stop_versicolor stop_virginica stop_proxy

.PHONY: c_build
c_build:
	docker-compose \
		-f ./$(DOCKER_COMPOSE) \
		build

.PHONY: c_up
c_up:
	docker-compose \
		-f ./$(DOCKER_COMPOSE) \
		up -d

.PHONY: c_down
c_down:
	docker-compose \
		-f ./$(DOCKER_COMPOSE) \
		down


.PHONY: health
health:
	curl localhost:9000/health

.PHONY: health_all
health_all:
	curl localhost:9000/health/all

.PHONY: metadata
metadata:
	curl localhost:9000/metadata


.PHONY: predict_get_test
predict_get_test:
	curl localhost:9000/predict/get/test

.PHONY: predict_post_test
predict_post_test:
	curl localhost:9000/predict/post/test


.PHONY: predict
predict:
	curl \
		-X POST \
		-H "Content-Type: application/json" \
		-d '{"Data": [1.0, 2.0, 3.0, 4.0]}' \
		localhost:9000/predict

.PHONY: predict_label
predict_label:
	curl \
		-X POST \
		-H "Content-Type: application/json" \
		-d '{"Data": [1.0, 2.0, 3.0, 4.0]}' \
		localhost:9000/predict/label