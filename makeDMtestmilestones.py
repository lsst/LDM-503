#!/usr/bin/env python

import csv
import re
import sys

fn = sys.argv[1]
of = fn.replace(".csv", ".tex")
out = open(of, "w")


with open(fn, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        c=0
        tid = row[c]
        if tid.startswith("LDM") :
            c= c+ 1
            desc = row[c]
            desc=re.sub(r'\#', '\\#', desc)
            c= c+ 1
            date = row[c]
            c= c+ 1
            txt = row[c]
            txt=re.sub(r'\&', 'and', txt)
            txt=re.sub(r'\#', '\\#', txt)

            c= c+ 1
            out.write(tid+" & "+date +" &\n NCSA & \\textbf{"+ desc +"} \n" + txt + "\n \\\\ \hline\n")
