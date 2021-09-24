build:
	docker build ./backend/ -t local/ancestors:dev

run: build
	docker run --rm -ti \
		--network host \
		-v $$(pwd)/backend:/app \
		local/ancestors:dev
