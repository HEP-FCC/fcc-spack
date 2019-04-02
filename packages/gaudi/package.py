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
    version('30.1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r1')
    version('30.2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r2')
    version('30.3', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r3')
    version('30.4', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r4')
    version('30.5', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r5')

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
    depends_on('xerces-c')

    depends_on('range-v3' )
    depends_on('relax')
    depends_on('gsl')

    patch('rt.patch', when="@30.1: ^boost@1.67:")
    patch('lcg95-gaudiv29v5.patch', when="@v29r2 ^boost@1.67:")
    patch('cxx17.patch', when="%gcc@8:")
    patch('BoostAllPython.patch', when="@v29r2 ^boost@1.67:")
