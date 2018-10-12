export TEXMFHOME = lsst-texmf/texmf

all: $(tex) dmtestgantt.tex dmtestmilestones.tex testsections.tex acronyms.tex
	latexmk -bibtex -pdf LDM-503.tex

clean :
	latexmk -c
	rm *.pdf

tex=LDM-503.tex DMVcdExample.tex TopLevelTestSpecs.tex approach.tex body.tex dmtestgantt.tex dmtestmilestones.tex dmvv.tex intro.tex rehearsal.tex reporting.tex roles.tex schedtab.tex schedule.tex scivalidation.tex testsections.tex

acronyms.tex :$(tex) myacronyms.txt skipacronyms.txt
	python3 ${TEXMFHOME}/../bin/generateAcronyms.py $(tex)

dmtestmilestones.tex: milestones/milestones.py
	python3 milestones/milestones.py ldm503 --table $@

dmtestgantt.tex: milestones/milestones.py
	python3 milestones/milestones.py ldm503 --gantt $@

testsections.tex: milestones/milestones.py
	python3 milestones/milestones.py ldm503 --commentary $@
