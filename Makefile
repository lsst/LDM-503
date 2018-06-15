all: $(tex) dmtestgantt.tex dmtestmilestones.tex testsections.tex acronyms.tex
	latexmk -bibtex -pdf -f LDM-503.tex

clean :
	latexmk -c
	rm *.pdf

tex=LDM-503.tex TopLevelTestSpecs.tex approach.tex approach.tex body.tex body.tex constraints.tex dmvv.tex f17_drp.tex intro.tex orstab.tex passfail.tex roles.tex schedtab.tex schedule.tex scivalidation.tex tools.tex validation.tex vvmatrix.tex

#acronyms.tex: $(tex) myacronyms.tex
#	acronyms.csh $(tex)

dmtestmilestones.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --table $@

dmtestgantt.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --gantt $@

testsections.tex: milestones/milestones.py
	python milestones/milestones.py ldm503 --commentary $@
