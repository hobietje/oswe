.PHONY: clean
clean:
	docker kill infallible_mccarthy || true
	docker rm infallible_mccarthy || true

.PHONY: build-win
build-win: clean
	docker build -t infallible_mccarthy:win -f Dockerfile.win .

.PHONY: build-alpine
build-alpine: clean
	docker build -t infallible_mccarthy:alpine -f Dockerfile.alpine .

.PHONY: run-win
run-win: build-win
	docker run --rm -it -p 8080:80 --name infallible_mccarthy infallible_mccarthy:win

.PHONY: run-alpine
run-alpine: build-alpine
	docker run --rm -it -p 8080:80 --name infallible_mccarthy infallible_mccarthy:alpine