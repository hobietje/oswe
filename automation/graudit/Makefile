TOP:=$(shell echo `cd ../.. && pwd`)
PWD:=$(shell pwd)

# .PHONY: clean
# clean:
# 	rm -f john.pot
# 	touch john.pot

.PHONY: build
build:
	docker build -t graudit:latest .

# List available databases
.PHONY: run-list
run-list: build
	@docker run -ti \
			   	graudit:latest \
				-l

# Scan a golang codebase
.PHONY: run-scan-go
run-scan-go: build
	@docker run -ti \
			   	-v $(PWD)/tests/go:/workdir \
			   	graudit:latest \
				-d /opt/graudit/signatures/go.db \
				-c 3 \
				-B \
				-A \
				/workdir
