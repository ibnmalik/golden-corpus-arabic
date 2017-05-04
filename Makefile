BUILD_GOLDEN_CORPUS="core/build_golden_corpus.py"


default: build

build:
	@echo "building golden_corpus_arabic.json ..."
	@mkdir build
	@python $(BUILD_GOLDEN_CORPUS)

clean:
	@rm -rf build
