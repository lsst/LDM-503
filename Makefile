#
#

SRCS=$(wildcard LDM-*.tex)

OBJS=$(SRCS:.tex=.pdf)

all: LDM-503.tex
	latexmk -bibtex -pdf -f LDM-503.tex

clean :
	latexmk -c 
	rm *.pdf
