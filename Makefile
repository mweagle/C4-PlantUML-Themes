default: build

clean:
	rm -rfv ./palettes
	mkdir -pv ./palettes

build: clean
	python3 ./scripts/palette-creator.py
	python3 readme-creator.py