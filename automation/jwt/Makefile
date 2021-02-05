TOP:=$(shell  echo `cd ../.. && pwd`)
PWD:=$(shell  pwd)

.PHONY: clean
clean:

.PHONY: build
build: clean
	docker build -t jwt:latest .

# Create token with None algorithm
.PHONY: jwt-create-none
jwt-create-none: build
	@docker run  -ti \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				create-none.py
				
# Change algorithm from RS256 to HS256
.PHONY: jwt-change
jwt-change: build
	docker run  -ti \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				change-rs256-to-hs256.py
				
# Change kid header in token
.PHONY: jwt-kid
jwt-kid: build
	docker run  -ti \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				change-hs256-kid.py
				
# Brute force kid header in token (will need customising to suit your target, intercept with a proxy to see results)
.PHONY: jwt-brute-kid
jwt-brute-kid: build
	docker run  -ti \
			   	-v $(TOP)/wordlists:/wordlists \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				brute-hs256-kid.py