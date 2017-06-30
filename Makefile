#
#


SRCS=$(wildcard LDM-*.tex)

OBJS=$(SRCS:.tex=.pdf)

all: LDM-503.tex
	latexmk -bibtex -pdf -f LDM-503.tex

clean :
	latexmk -c 
	rm *.pdf


tex=	LDM-503.tex constraints.tex passfail.tex scivalidation.tex TopLevelTestSpecs.tex intro.tex reporting.tex schedtab.tex tools.tex body.tex schedule.tex validation.tex

acronyms.tex :$(tex) myacronyms.tex 
	acronyms.csh  $(tex)
