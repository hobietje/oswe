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
				
# Brute force kid header in token (will need customising to suit your target, intercept with a proxy to see results) [alternate example]
.PHONY: jwt-brute-kid-v2
jwt-brute-kid-v2: build
	docker run  -ti \
			   	-v $(TOP)/wordlists:/wordlists \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				brute-hs256-kid-v2.py

# Change payload in HS256 (requires signature key to be brute forced first)
.PHONY: jwt-update-hs256
jwt-update-hs256: build
	docker run  -ti \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				update-hs256.py

# Change signature to PS256 and add a JWK to the JWT header
.PHONY: jwk-ps256
jwk-ps256: build
	docker run  -ti \
			   	-v $(PWD)/data:/workdir/data \
			   	jwt:latest \
				jwk-ps256.py