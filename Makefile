.DEFAULT_GOAL := all

registrations.yaml: indico_to_yaml.py registrations.csv
	python indico_to_yaml.py registrations.csv registrations.yaml

attendance.pdf : template_attendance.tex details.yaml registrations.yaml
	pandoc $(filter-out $<,$^ ) -o $@ --template=$< --pdf-engine=xelatex

receipt.pdf : template_receipt.tex details.yaml registrations.yaml
	pandoc $(filter-out $<,$^ ) -o $@ --template=$< --pdf-engine=xelatex


.PHONY: all
all: attendance.pdf receipt.pdf

.PHONY: clean
clean :
	rm attendance.pdf receipt.pdf registrations.yaml
