build:
	docker build ./backend/ -t local/ancestors:dev

run: build
	docker run --rm -ti \
		--network host \
		-v $$(pwd)/ancestors:/app \
		local/ancestors:dev
