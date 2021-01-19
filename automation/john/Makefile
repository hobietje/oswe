TOP:=$(shell  echo `cd ../.. && pwd`)
PWD:=$(shell  pwd)

.PHONY: clean
clean:
	rm -f john.pot
	touch john.pot

.PHONY: build
build:
	docker build -t john:latest .
				
# Unshadow a linux /etc/shadow file
.PHONY: run-unshadow
run-unshadow: build
	@docker run  -ti \
			   	-v $(PWD)/tests:/workdir \
				-v $(PWD)/john.pot:/root/.john/john.pot \
				--entrypoint unshadow \
			   	john:latest \
				/workdir/passwd \
				/workdir/shadow

# Check /etc/passwd hashes against wordlist
.PHONY: run-wordlist-passwd
run-wordlist-passwd: build clean
	docker run  -ti \
				-v $(PWD)/john.pot:/root/.john/john.pot \
			   	-v $(PWD)/tests:/workdir \
			   	-v $(TOP)/wordlists:/wordlists \
			   	john:latest \
				--wordlist=/wordlists/others/common_pass.txt \
				--show \
				/workdir/passwd
				
# Check /etc/passwd hashes against wordlist
.PHONY: run-passwd-des
run-passwd-des: build clean
	docker run  -ti \
				-v $(PWD)/john.pot:/root/.john/john.pot \
			   	-v $(PWD)/tests:/workdir \
			   	john:latest \
				--format=descrypt \
				/workdir/passwd-des
				
# Check /etc/passwd hashes
.PHONY: run-passwd-md5
run-passwd-md5: build clean
	docker run  -ti \
				-v $(PWD)/john.pot:/root/.john/john.pot \
			   	-v $(PWD)/tests:/workdir \
			   	john:latest \
				/workdir/passwd-md5
				
# Check a MySQL password .myd file
.PHONY: run-mysql
run-mysql: build clean
	docker run  -ti \
				-v $(PWD)/john.pot:/root/.john/john.pot \
			   	-v $(PWD)/tests:/workdir \
			   	john:latest \
				/workdir/mysql
				
# Show cracked passwords
.PHONY: run-show
run-show: build
	touch john.pot
	docker run  -ti \
				-v $(PWD)/john.pot:/root/.john/john.pot \
			   	-v $(PWD)/tests:/workdir \
			   	john:latest \
				--show \
				/workdir/passwd
