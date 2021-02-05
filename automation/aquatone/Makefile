PWD:=$(shell pwd)
TOP:=$(shell echo `cd ../.. && pwd`)

.PHONY: build
build:
	docker build -t aquatone:latest .

.PHONY: run
run: build
	echo 'www.cnn.com' | docker run -i --privileged --rm \
			   	-v $(PWD)/output:/output \
				aquatone:latest \
				-chrome-path /usr/bin/chromium \
				-out /output \
				-debug \
				-http-timeout 30000 \
				-save-body true \
				-resolution '1920,1080' \
				-ports '80,443'