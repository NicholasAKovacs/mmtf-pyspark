#!/user/bin/env python
'''
pisces.py

 This filter passes through representative structures or protein chains
 from the PISCES CulledPDB sets. A CulledPDB set is selected by specifying
 sequenceIdentity and resolution cutoff values from the following
 list:
 <p> sequenceIdentity = 20, 25, 30, 40, 50, 60, 70, 80, 90
 <p> resolution = 1.6, 1.8, 2.0, 2.2, 2.5, 3.0

 <p> See <a href="http://dunbrack.fccc.edu/PISCES.php">PISCES</a>.
 Please cite the following in any work that uses lists provided by PISCES
 G. Wang and R. L. Dunbrack, Jr. PISCES: a protein sequence culling server.
 Bioinformatics, 19:1589-1591, 2003.


Authorship information:
    __author__ = "Peter Rose"
    __maintainer__ = "Mars Huang"
    __email__ = "marshuang80@gmai.com:
    __status__ = "debug"
'''
from src.main.webservices import piscesDownloader

class pisces(object):
    '''
     Filters representative PDB structures and polymer chains based
     on the specified criteria using PISCES CulledPDB sets.
     <p> sequenceIdentity = 20, 25, 30, 40, 50, 60, 70, 80, 90
     <p> resolution = 1.6, 1.8, 2.0, 2.2, 2.5, 3.0

    Attributes:

    '''
    def __init__(self, sequenceIdentity, resolition):
        pdbIds = set()

        pD = PiscesDownloader(sequenceIdentity, resolition)

        # TODO check getStructureCahinIds
        for pdbId in pD.getStructureChainIds():
            pdbIds.add(pdbId)
            pdbIds.add(pdbId[:4])

    def __call__(self, t):
        return t[0] in pdbIds
