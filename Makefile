export TEXMFHOME = lsst-texmf/texmf

all: $(tex) dmtestgantt.tex dmtestmilestones.tex testsections.tex acronyms.tex
	latexmk -bibtex -pdf -f LDM-503.tex

clean :
	latexmk -c
	rm *.pdf

tex=LDM-503.tex TopLevelTestSpecs.tex approach.tex approach.tex body.tex body.tex dmvv.tex intro.tex schedtab.tex schedule.tex scivalidation.tex tools.tex rehearsal.tex vvmatrix.tex

#acronyms.tex: $(tex) myacronyms.tex
#	acronyms.csh $(tex)

dmtestmilestones.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --table $@

dmtestgantt.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --gantt $@

testsections.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --commentary $@
