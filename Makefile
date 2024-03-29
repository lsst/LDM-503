export TEXMFHOME ?= lsst-texmf/texmf
VENVDIR = venv

all: $(tex) dmtestgantt.tex dmtestmilestones.tex testsections.tex acronyms.tex
	xelatex LDM-503.tex
	bibtex LDM-503
	xelatex LDM-503.tex
	xelatex LDM-503.tex

clean :
	latexmk -c
	rm -f *.pdf
	rm -f dmtestmilestones.tex
	rm -f testsections.tex
	rm -f dmtestgantt.tex
	rm -rf $(VENVDIR)

generated :dmtestmilestones.tex dmtestgantt.tex

tex=LDM-503.tex DMVcdExample.tex approach.tex body.tex dmtestgantt.tex dmtestmilestones.tex dmvv.tex intro.tex rehearsal.tex reporting.tex roles.tex schedtab.tex schedule.tex scivalidation.tex testsections.tex

acronyms.tex :$(tex) myacronyms.txt skipacronyms.txt
	python3 ${TEXMFHOME}/../bin/generateAcronyms.py $(tex)

venv: milestones/requirements.txt
	python3 -m venv $(VENVDIR)
	( \
		.  $(VENVDIR)/bin/activate; \
		pip install -r milestones/requirements.txt; \
	)

dmtestmilestones.tex testsections.tex &: bin/generate_milestones.py venv
	( \
		.  $(VENVDIR)/bin/activate; \
		PYTHONPATH=milestones python3 bin/generate_milestones.py \
	)

dmtestgantt.tex: milestones/milestones.py venv
	( \
		.  $(VENVDIR)/bin/activate; \
		PYTHONPATH=milestones python3 milestones/milestones.py gantt --embedded --output $@ \
	)

