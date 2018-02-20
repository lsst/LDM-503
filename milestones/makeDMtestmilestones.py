import argparse
import csv
import sys
import time

from collections import namedtuple
from datetime import datetime
from io import StringIO
from textwrap import dedent

EXCEL_DATEFMT = "%m/%d/%Y %I:%M:%S %p"
LOCATION = "NCSA"  # for all tests
Milestone = namedtuple('Milestone',
                       ['code', 'name', 'short_name', 'test_spec',
                        'description', 'comments', 'date', 'successors'])

def get_milestones(ms_list, ms_dscr):
    milestones = []
    milestone_reader = csv.DictReader(ms_list)
    description_reader = csv.DictReader(ms_dscr)
    descriptions = {}
    short_names = {}
    comments = {}
    for d in description_reader:
        descriptions[d['code']] = d['description']
        short_names[d['code']] = d['short_name']
        comments[d['code']] = d['comments']

    for k in milestone_reader:
        code = k['task_code']
        if code == "Activity ID":
            continue
        dscr = descriptions[code] if code in descriptions else ""
        date = (datetime.strptime(k['end_date'], EXCEL_DATEFMT) if k['end_date']
                else datetime.strptime(k['start_date'], EXCEL_DATEFMT))
        short_name = short_names[code] if (
                        code in short_names and short_names[code]
                     ) else k['task_name']
        cmnts = comments[code] if code in comments else ""
        milestones.append(
            Milestone(code, k['task_name'], short_name, "", dscr,
                      cmnts, date, k['succ_list'].split(', '))
        )

    return milestones

def escape_latex(text):
    return text.strip().replace("#", "\#").replace("&", "\&").replace("Test report: ", "")

def format_table(milestones, prefix="LDM"):
    output = StringIO()
    for ms in sorted(milestones, key=lambda x: x.date):
        if ms.code.startswith(prefix):
            output.write("{} & {} & NCSA & \\textbf{{{}}}: {} \\\\ \hline\n".format(
                escape_latex(ms.code),
                escape_latex(ms.date.strftime("%Y-%m-%d")),
                escape_latex(ms.name),
                escape_latex(ms.description)
            ))
    return output.getvalue()

def format_gantt(milestones, prefix="", start=datetime(2017, 7, 1)):
    def get_month_number(start, date):
        # July 2017 is month 1; all other months sequentially.
        return 1 + (date.year * 12 + date.month) - (start.year * 12 + start.month)
    def get_milestone_name(code):
        return code.lower().replace("-", "").replace("&", "")

    preamble = dedent("""
        \\begin{ganttchart}[
            expand chart=\\textwidth,
            title label font=\\sffamily\\bfseries,
            milestone label font=\\small,
            progress label text={#1},
            milestone progress label node/.append style={right=0.9cm},
            y unit chart=0.6cm,
            y unit title=0.8cm
        ]{1}{115}
          \\gantttitle{}{6} \\gantttitle{2018}{12} \\gantttitle{2019}{12}
          \\gantttitle{2020}{12} \\gantttitle{2021}{12} \\gantttitle{2022}{12}
          \\gantttitle{Operations}{49} \\
          \\ganttnewline\n
    """)
    postamble = dedent("""
        \\end{ganttchart}
    """)
    output = StringIO()
    output.write(preamble)
    for ms in sorted(milestones, key=lambda x: x.date):
        if not ms.code.startswith(prefix): continue
        output.write("\\ganttmilestone[name={},progress label text={}\\phantom{{#1}},progress=100]{{{}}}{{{}}} \\ganttnewline\n".format(
            escape_latex(get_milestone_name(ms.code) ),
            escape_latex(ms.short_name),
            escape_latex(ms.code),
            get_month_number(start, ms.date)
        ))
    for ms in sorted(milestones, key=lambda x: x.date):
        if not ms.code.startswith(prefix): continue
        for succ in ms.successors:
            if succ in [ms.code for ms in milestones]:
                output.write("\\ganttlink{{{}}}{{{}}}\n".format(
                    escape_latex(get_milestone_name(ms.code)),
                    escape_latex(get_milestone_name(succ))
                ))
    output.write(postamble)
    return output.getvalue()

def format_commentary(milestones, prefix="LDM"):
    output = StringIO()
    for ms in sorted(milestones, key=lambda x: x.date):
        if not ms.code.startswith(prefix): continue
        output.write("\\subsection{{{} (\\textbf{{{}}})}}\n".format(
                     escape_latex(ms.name), escape_latex(ms.code)))
        output.write("\\label{{{}}}\n\n".format(escape_latex(ms.code)))
        output.write("{}\n\n".format(escape_latex(ms.description)))
        output.write("{}\n\n".format(escape_latex(ms.comments)))
    return output.getvalue()

def parse_args():
    parser = argparse.ArgumentParser(description='Prepare LDM-503-n milestone summaries')
    parser.add_argument('pmcs', help="Milestone listing extracted from PMCS.")
    parser.add_argument('dscr', help="Mapping of milestone ID to description.")
    parser.add_argument('--table', help="Output location for milestone table.")
    parser.add_argument('--gantt', help="Output location for Gantt chart.")
    parser.add_argument('--commentary', help="Output location for commentary.")
    args = parser.parse_args()
    if not args.table and not args.gantt and not args.commentary:
        raise RuntimeError("No output requested!")
    return args

if __name__ == "__main__":
    args = parse_args()
    with open(args.pmcs) as ms_list, open(args.dscr) as ms_dscr:
        milestones = get_milestones(ms_list, ms_dscr)
    if args.table:
        with open(args.table, 'w') as output:
            output.write("% Auto-generated by {} on {} - DO NOT EDIT\n\n".format(sys.argv[0], time.strftime("%c")))
            output.write(format_table(milestones))
    if args.gantt:
        with open(args.gantt, 'w') as output:
            output.write("% Auto-generated by {} on {} - DO NOT EDIT\n\n".format(sys.argv[0], time.strftime("%c")))
            output.write(format_gantt(milestones))
    if args.commentary:
        with open(args.commentary, 'w') as output:
            output.write("% Auto-generated by {} on {} - DO NOT EDIT\n\n".format(sys.argv[0], time.strftime("%c")))
            output.write(format_commentary(milestones))
