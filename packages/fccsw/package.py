
from spack import *

class Fccsw(CMakePackage):
    """software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.5.tar.gz"
    git      = "https://github.com/HEP-FCC/FCCSW.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    version('0.12', sha256='a67151c12177882abd8afcf56bee47c2830c44cac749b23d08d005b45096b264')
    version('0.11', 'e3b5aa8f396cffae745305801eb8f7a38a8a7881')
    version('0.10', '40b75f42fb51934cdc3c52049226ac39')
    version('0.9', 'fbbfc1deeaab40757d05ebfcbfa7b0f5')
    version('0.5.1', 'e2e6e6fa40373c3a14ea823bb9bc0810')
    version('0.5', 'f2c849608ac1ab175f432a5e55dbe673')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('acts-core')
    depends_on('clhep')
    depends_on('dd4hep')
    depends_on('delphes')
    depends_on('gl2ps')
    depends_on('fastjet')

    # LCG Releases built with gcc7 use C++17
    depends_on('fcc-edm@0.5.5: cxxstd=17', when="%gcc@7:")
    depends_on('fcc-edm cxxstd=14', when="%gcc@:6.99")

    depends_on('gaudi')
    depends_on('geant4')
    depends_on('hepmc')
    depends_on('heppdt')

    # LCG Releases built with gcc7 or higher require C++17
    depends_on('papas@1.2.2: cxxstd=17', when="%gcc@7:")
    depends_on('papas cxxstd=14', when="%gcc@:6.99")

    depends_on('podio')
    depends_on('pythia8')
    depends_on('root')
    depends_on('tbb')

    # tricktrack is yet to be refactored (currently included in fccsw)
    #depends_on('tricktrack')
    depends_on('xerces-c')


    patch('permissions.patch', when='@0.9')
    patch('ddeve.patch', when='@0.9 ^dd4hep@01-08')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args
    
