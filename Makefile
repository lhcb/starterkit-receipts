.DEFAULT_GOAL := all

registrations.yaml: indico_to_yaml.py registrations.csv
	python indico_to_yaml.py registrations.csv registrations.yaml

receipts.pdf : template.tex details.yaml registrations.yaml
	pandoc $(filter-out $<,$^ ) -o $@ --template=$< --latex-engine=xelatex

.PHONY: all
all: receipts.pdf

.PHONY: clean
clean :
	rm receipts.pdf registrations.yaml
