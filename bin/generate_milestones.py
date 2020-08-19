from io import StringIO

from milestones import (escape_latex, write_output,
                        get_latest_pmcs_path, get_local_data_path,
                        load_milestones)


def generate_table(milestones):
    output = StringIO()
    for ms in sorted([ms for ms in milestones
                     if ms.code.startswith("LDM-503")],
                     key=lambda x: (x.due, x.code)):
        output.write(f"{escape_latex(ms.code)} &\n")
        output.write(f"{escape_latex(ms.due.strftime('%Y-%m-%d'))} &\n")
        output.write("NCSA &\n")
        output.write(f"{escape_latex(ms.short_name)} \\\\\n\n")
    return output.getvalue()


def generate_commentary(milestones):
    output = StringIO()
    for ms in sorted([ms for ms in milestones
                     if ms.code.startswith("LDM-503")],
                     key=lambda x: (x.due, x.code)):
        output.write(f"\\subsection{{{escape_latex(ms.short_name)} ")
        output.write(f"(\\textbf{{{escape_latex(ms.code)}}})}}\n")
        output.write(f"\\label{{{escape_latex(ms.code)}}}\n\n")
        output.write("\\subsubsection{Execution Procedure}\n\n")
        if ms.test_spec:
            output.write(f"This text will be executed following the procedure "
                         f"defined in {escape_latex(ms.test_spec)}.\n\n")
        else:
            output.write("The execution procedure for this test is "
                         "currently unspecified.\n\n")
        output.write("\\subsubsection{Description}\n\n")
        output.write(f"{escape_latex(ms.description)}\n\n")
        if ms.comment:
            output.write("\\subsubsection{Comments}\n\n")
            output.write(f"{escape_latex(ms.comment)}\n\n")
    return output.getvalue()


if __name__ == "__main__":
    milestones = load_milestones(get_latest_pmcs_path(), get_local_data_path())
    write_output("dmtestmilestones.tex", generate_table(milestones))
    write_output("testsections.tex", generate_commentary(milestones))
