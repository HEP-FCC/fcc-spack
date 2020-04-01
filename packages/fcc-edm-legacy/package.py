
from spack import *


class FccEdmLegacy(CMakePackage):
    """FCCEDM Legacy"""

    """Event data model of FCC - Legacy types"""

    homepage = "https://github.com/HEP-FCC/fcc-edm-legacy"
    url      = "https://github.com/HEP-FCC/fcc-edm-legacy/archive/v0.1.0.zip"

    version('0.1.1', sha256='9891db983dab116c63f665402ca746c2bc9bd034f4c3185b9cacd7f8115707a5')
    version('0.1.0', '97a4bdfb355980f6556f9dc032f23e62')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    depends_on('cmake', type='build')
    depends_on('python', type='build')
    depends_on('dag')
    depends_on('root')
    depends_on('podio')

    # in LCG_96 ROOT is installed with an external xz rather than the builtin,
    # so the genreflex binary needs to find it.
    # As root is installed as an external package we cannot modify its
    # setup_dependent_environment function to add the xz lib folder to the
    # LD_LIBRARY_PATH hence we need to do it here.
    depends_on('xz', when='^root@6.16:')

    # Override pre-defined test step
    # Multiple tests access to the same root file, thus we avoid parallel
    # execution at this stage
    def check(self):
        with working_dir(self.build_directory):
            make("test", "CTEST_OUTPUT_ON_FAIL=1")
    
    def setup_environment(self, spack_env, run_env):
      # needed for genreflex
      spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
      run_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
      if 'xz' in self.spec:
        spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['xz'].prefix.lib)

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCEDMLEGACY', self.prefix)
