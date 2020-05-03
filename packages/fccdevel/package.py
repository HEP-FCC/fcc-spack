from spack import *
from spack.package import PackageBase

class Fccdevel(PackageBase):
    """Bundle package to install the FCC software development environment."""


    version('1.0')

    maintainers = ['vvolkl']

    depends_on('cmake', type='build')
    depends_on('dd4hep')
    depends_on('delphes')
    depends_on('fastjet')

    # LCG Releases built with gcc7 use C++17
    depends_on('fcc-edm@0.5.5: cxxstd=17', when="%gcc@7:")
    depends_on('fcc-edm cxxstd=14', when="%gcc@:6.99")
    depends_on('fcc-edm-legacy')

    depends_on('py-fcchhanalyses')
    depends_on('fcc-physics')
    depends_on('gaudi')
    depends_on('geant4')
    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('root')
    depends_on('tbb')
    depends_on('acts_core')

    # LCG Releases built with gcc7 use C++17
    depends_on('papas@1.2.2: cxxstd=17', when="%gcc@7:")
    depends_on('papas cxxstd=14', when="%gcc@:6.99")
    depends_on('heppy')
    #depends_on('tricktrack')
    depends_on('guinea-pig')
    depends_on('fccsw')

