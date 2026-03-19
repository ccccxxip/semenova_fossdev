.DEFAULT_GOAL := help
create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTISE)
endif
	@echo "cteated practice"
	mkdir -p $(PRACTICE)
	cp practiceMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTISE)
endif
	rm -rf $(PRACTICE)

help:
	@echo "this makefile for repo-level activity"

# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# touch demo-practice/README.md 