PWD:=$(shell pwd)
TOP:=$(shell echo `cd ../.. && pwd`)

.PHONY: build
build:
	docker build -t aquatone:latest .

# Check a single domain
.PHONY: run
run: build
	echo 'www.cnn.com' | docker run -i --privileged --rm \
			   	-v $(PWD)/output:/output \
				aquatone:latest \
				-chrome-path /usr/bin/chromium \
				-out /output \
				-debug \
				-scan-timeout 10000 \
				-http-timeout 30000 \
				-save-body true \
				-resolution 1920,1080 \
				-ports 80,443

# Create a list of domains to be checked, e.g.:
#   for i in {0..255}; do echo "0x$(printf '%02x' $i).a.hackycorp.com"; done > input.txt
.PHONY: run-cat
run-cat: build
	cat input.txt | docker run -i --privileged --rm \
			   	-v $(PWD)/output:/output \
			   	-v $(PWD)/tmp:/tmp \
				aquatone:latest \
				-out /output \
				-chrome-path /usr/bin/chromium \
				-debug \
				-scan-timeout 10000 \
				-http-timeout 60000 \
				-save-body true \
				-resolution 1920,1080 \
				-ports 80