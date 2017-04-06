# LDM-503
DM System Validation, Verification and Test Plan.

There is no version in DocuShare yeat -- the first release is in a branch 
tickets/DM-10125

This is following a lsstdoc.cls. 
You need the lsst-texmf in your TEXMFLOCAL to build it. 

Clone this repo:

     https://github.com/lsst/lsst-texmf/


then add the texmf folder  to TEXMFLOCAL environment variable in your bashrc or equivalent

    export TEXMFLOCAL=pathtolsst-texmf/texmf


then you must run 

    mktexlsr

After this tex will find all the cls files bibliography etc ..


