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

The document is built using LaTeX, and relies upon the `lsst-texmf <https://lsst-texmf.lsst.io/>`_, `images <https://github.com/lsst-dm/images>`_, and `milestones <https://github.com/lsst-dm/milestones>`_ repositories.
To build from scratch::

  git clone --recurse-submodules https://github.com/lsst/ldm-503
  cd ldm-503
  make
