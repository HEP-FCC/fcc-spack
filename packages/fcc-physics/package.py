
from spack import *


class FccPhysics(CMakePackage):
    """Event data model of FCC"""

    homepage = "https://github.com/HEP-FCC/fcc-physics/"
    url      = "https://github.com/HEP-FCC/fcc-physics/archive/v0.1.tar.gz"

    version('0.2.2', sha256='6e2bca1fc51e52cd70329056395cf0ebe5c660642f3ab57d98b03140cdbacdd4')
    version('0.2.1', '93aeb48160d8fc5ae18e3568dd4f34b4')
    version('0.1.1', '8136978e23b5b9438646868f8e81d037')
    version('0.1', '89e4f57d0dc9335e2ad6ed796c5e2600')
    version('develop', git='https://github.com/HEP-FCC/fcc-physics.git', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    depends_on('cmake', type='build')
    depends_on('fcc-edm')
    depends_on('podio')
    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('fastjet')

    # in LCG_96 ROOT is installed with an external xz rather than the builtin,
    # so the genreflex binary needs to find it.
    # As root is installed as an external package we cannot modify its
    # setup_dependent_environment function to add the xz lib folder to the
    # LD_LIBRARY_PATH hence we need to do it here.
    depends_on('xz', when='^root@6.16:')

    def setup_environment(self, spack_env, run_env):
      spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
      run_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
      spack_env.set('HEPMC_PREFIX', self.spec['hepmc'].prefix)
      if 'xz' in self.spec:
        spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['xz'].prefix.lib)

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCPHYSICS', self.prefix)
