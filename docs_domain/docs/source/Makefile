

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

all: html

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

clean:
	rm -rf $(BUILDDIR)

rebuild: clean html

help:
	@echo "  make html    - собрать HTML документацию"
	@echo "  make clean   - удалить сгенерированные файлы"
	@echo "  make rebuild - очистить и пересобрать"
	@echo "  make help    - показать эту справку"

.PHONY: all html clean rebuild help