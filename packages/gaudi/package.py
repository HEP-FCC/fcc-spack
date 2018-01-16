from spack import *

class Gaudi(CMakePackage):
    """Gaudi framework."""
    homepage = "https://gaudi.cern.ch"
    url      = "https://gaudi.cern.ch"

    version('v27r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v27r1')
    version('v28r0', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r0')
    version('v28r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r1')
    version('v28r2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r2')
    version('v29r2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v29r2')

    depends_on("python")
    depends_on("root")
    depends_on("py-qmtest")
    depends_on("clhep")
    depends_on("boost")
    depends_on("cppunit")
    depends_on("aida")
    depends_on("intel-tbb")
    depends_on("gperftools")
    depends_on("heppdt")
