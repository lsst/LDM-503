#
#

SRCS=$(wildcard LDM-*.tex)

OBJS=$(SRCS:.tex=.pdf)

all: $(OBJS) 


%.pdf: %.tex 
	latexmk -bibtex -pdf -f  $<

clean :
	latexmk -c 
	rm *.pdf
