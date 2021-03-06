
from spack import *


class Papas(CMakePackage):
    """PAPAS (PArametrized PArticle Simulation) provides simulation and
    reconstruction reconstruction algorithm which is designed to allow users to
    test the performance of detector design."""

    homepage = "https://github.com/HEP-FCC/papas"
    git = "https://github.com/HEP-FCC/papas.git"
    url      = "https://github.com/HEP-FCC/papas/archive/1.2.2.tar.gz"

    version('master', branch='master')
    version('1.2.2', sha256='0f469d54eec726fdf654892a98720696499be0cf73db266e9715b01cb6c9c60c')
    version('1.2.1', '78f34649bd7b82aa1e8eb27b69dae8d1')
    version('1.2.0', '74d700ca5872872b2beda7e5862bfaa4')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('cxxstd',
            default='14',
            values=('14', '17'),
            multi=False,
      description='Use the specified C++ standard when building.')

    depends_on('fcc-edm')
    depends_on('podio')
    depends_on('pythia8')


    def cmake_args(self):
      args = []
      # C++ Standard
      args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
      return args

    def setup_dependent_environment(self, spack_env, run_env, dspec):
      spack_env.set('PAPAS', self.prefix)
