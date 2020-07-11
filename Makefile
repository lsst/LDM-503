export TEXMFHOME = lsst-texmf/texmf
VENVDIR = venv

all: $(tex) dmtestgantt.tex dmtestmilestones.tex testsections.tex acronyms.tex
	latexmk -bibtex -pdf LDM-503.tex

clean :
	latexmk -c
	rm *.pdf
	rm -rf $(VENVDIR)

tex=LDM-503.tex DMVcdExample.tex approach.tex body.tex dmtestgantt.tex dmtestmilestones.tex dmvv.tex intro.tex rehearsal.tex reporting.tex roles.tex schedtab.tex schedule.tex scivalidation.tex testsections.tex

acronyms.tex :$(tex) myacronyms.txt skipacronyms.txt
	python3 ${TEXMFHOME}/../bin/generateAcronyms.py $(tex)

venv: milestones/requirements.txt
	python3 -m venv $(VENVDIR)
	( \
		source $(VENVDIR)/bin/activate; \
		pip install -r milestones/requirements.txt; \
	)

dmtestmilestones.tex: milestones/milestones.py venv
	( \
		source $(VENVDIR)/bin/activate; \
		python3 milestones/milestones.py ldm503 --table-location $@; \
	)

dmtestgantt.tex: milestones/milestones.py venv
	( \
		source $(VENVDIR)/bin/activate; \
		python3 milestones/milestones.py ldm503 --gantt-location $@; \
	)

testsections.tex: milestones/milestones.py venv
		( \
		source $(VENVDIR)/bin/activate; \
		python3 milestones/milestones.py ldm503 --text-location $@; \
	)
