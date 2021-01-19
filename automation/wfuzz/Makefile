TOP:=$(shell  echo `cd ../.. && pwd`)

.PHONY: build
build:
	docker build -t wfuzz:latest .

# Look for apache files
.PHONY: run-vulns-apache
run-vulns-apache: build
	docker run  -ti \
			   	-v $(TOP)/wordlists:/wordlists/ \
			   	wfuzz:latest \
				-H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
				-H "accept-encoding: gzip, deflate, br" \
				-H "accept-language: en,en-AU;q=0.9,nl;q=0.8" \
				-H "cache-control: no-cache" \
				-H "pragma: no-cache" \
				-H "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36" \
				--hc 404 \
				-c \
				-z file,/wordlists/vulns/apache.txt \
				https://tomorro.com/FUZZ

# Discover admin panels on a given url
.PHONY: run-adminpanels
run-adminpanels: build
	docker run  -ti \
			   	-v $(TOP)/wordlists:/wordlists/ \
			   	wfuzz:latest \
				-H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
				-H "accept-encoding: gzip, deflate, br" \
				-H "accept-language: en,en-AU;q=0.9,nl;q=0.8" \
				-H "cache-control: no-cache" \
				-H "pragma: no-cache" \
				-H "user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36" \
				--hc 404 \
				-c \
				-z file,/wordlists/general/admin-panels.txt \
				https://tomorro.com/FUZZ