#!/usr/bin/env python

import csv
import re
import sys

fn=sys.argv[1]
of=fn.replace(".csv",".tex")
out=open (of,"w")


with open(fn, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        req = row[3]
        name=row[5]
        meth=row[14]
        name = re.sub(r'\&', 'and', name)
        if (req!=""):
           out.write(req+" & "+name +" & "+ meth + "\\\\ \hline\n")
