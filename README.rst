##################################
LDM-503: Data Management Test Plan
##################################

This document describes the validation, verification & test procedures in use by LSST Data Management.

Links
=====

- Accepted version: https://ls.st/LDM-294
- Drafts: https://ldm-294.lsst.io/v

Building the PDF locally
========================

The document is built using LaTeX, and relies upon the `lsst-texmf <https://lsst-texmf.lsst.io/>`_ and `images <https://github.com/lsst-dm/images>`_ repositories.
To build from scratch::

  git clone https://github.com/lsstm/lsst-texmf
  git clone https://github.com/lsst-dm/images
  git clone https://github.com/lsst/ldm-503
  export TEXMFHOME=$(pwd)/lsst-texmf/texmf
  cd ldm-503
  ln -s ../images .
  make

Updating milestone definitions
==============================

When the document is built, the CSV files ``milestones/pmcs.csv`` and ``milestones/descriptions.csv`` are used by the script ``milestones/makeDMtestmilestones.py`` to generate:

- A table of DM level 2 milestones;
- A Gantt chart showing DM level 2 milestones and their relationship to other major project events;
- Textual descriptions of DM level 2 milestones.

All of these artefacts are then included in the generated document.

``milestones/pmcs.csv`` is an extract from the project baseline, as stored in Primavera.
Update it by using the “DM LDM-503 Milestones” template to export to export to Excel format, then convert that to CSV.
It may be necessary to strip the BOM from the CSV file to enable it to be easily read by other tools.
This file should be regularly (e.g. monthly) updated as new PMCS baselines are issued; it should *never* be edited by hand.

``milestones/descriptions.csv`` provides hand-edited information about the milestones which is not recorded in PMCS.
It should be updated as needed.
