build:
	docker build ./ancestors/ -t noyr:dev

run: build
	docker run --rm -ti \
		--network host \
		-v $$(pwd)/ancestors:/app \
		agrrh/ancestors:dev
