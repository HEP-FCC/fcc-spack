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
    version('32.0', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v32r0')

    # Minimal Gaudi build
    depends_on("boost")
    depends_on('cppgsl', when='@32.0:')
    depends_on("intel-tbb")
    depends_on("libuuid")
    depends_on("python")
    depends_on('py-xenv@develop_2018-12-20:')
    depends_on('range-v3' )
    depends_on("root")
    depends_on("vdt", when="@32.0:, root@6.16:")
    depends_on("zlib")

    # optional
    # depends_on("py-qmtest")
    depends_on("clhep")
    depends_on("cppunit")
    depends_on("aida")
    depends_on("gperftools")
    depends_on("heppdt")

    depends_on('gsl')
    depends_on('relax')
    depends_on('xerces-c')

    patch('rt.patch', when="@30.1:30.5 ^boost@1.67:")
    patch('lcg95-gaudiv29v5.patch', when="@v29r2 ^boost@1.67:")
    patch('cxx17.patch', when="@:30.4 %gcc@8:")
    patch('BoostAllPython.patch', when="@v29r2 ^boost@1.67:")

    def cmake_args(self):

        spec = self.spec

        options = []

        if '^boost@1.69:' in spec:
             options = [
                 # Otherwise find_package(Boost) finds the wrong directories
                 '-DBoost_NO_BOOST_CMAKE=TRUE',
             ]

        return options
