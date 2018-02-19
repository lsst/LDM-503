all: $(tex) dmtestgantt.tex dmtestmilestones.tex acronyms.tex
	latexmk -bibtex -pdf -f LDM-503.tex

clean :
	latexmk -c
	rm *.pdf

tex=LDM-503.tex LDM-503-2.tex TopLevelTestSpecs.tex approach.tex approach.tex body.tex body.tex constraints.tex dmvv.tex f17_drp.tex intro.tex orstab.tex passfail.tex roles.tex schedtab.tex schedule.tex scivalidation.tex testsections.tex tools.tex validation.tex vvmatrix.tex

acronyms.tex: $(tex) myacronyms.tex
	acronyms.csh $(tex)

dmtestmilestones.tex: makeDMtestmilestones.py milestones_pmcs.csv milestone_descriptions.csv
	python3 makeDMtestmilestones.py milestones_pmcs.csv milestone_descriptions.csv --table $@

dmtestgantt.tex: makeDMtestmilestones.py milestones_pmcs.csv milestone_descriptions.csv
	python3 makeDMtestmilestones.py milestones_pmcs.csv milestone_descriptions.csv --gantt $@
