#!/usr/bin/env python

import csv
import os
import re
import sys

CSVFIELDS = ("id", "title", "date", "description", "note")
LOCATION = "NCSA"  # for all tests

fn = sys.argv[1]
of = fn.replace(".csv", ".tex")
tf = open("testsections.tex","w")
out = open(of, "w")

def sanitize(string):
     return string.strip().replace("#", "\#").replace("&", "and").replace("Test report: ", "")


with open(fn, "r") as f:
    reader = csv.DictReader(f, fieldnames=CSVFIELDS)
    for row in reader:
        if not row['id'].startswith("LDM"):
            continue

        desc = "\\textbf{%s}\n%s" % (sanitize(row['title']), sanitize(row['description']))
        out.write("%s & %s & %s & %s\n\\\\ \hline\n" % (sanitize(row["id"]), sanitize(row['date']),
                                                        LOCATION, desc))

        # If there's a pre-existing "id.tex" file on on disk, we use that.
        # Otherwise, construct one from the CSV file.
        if os.path.exists("%s.tex" % (row['id'].strip(),)):
            tf.write("\n\\input %s\n\n" % (row['id'].strip(),))
        else:
            tf.write("\subsection{" + sanitize(row['title']) + " \\textbf{(" + row['id'] + ")}\label{" + row['id'] + "}}\n")
            tf.write(sanitize(row['description'])+"\n \\newline\n")
            tf.write(sanitize(row['note'])+"\n")
