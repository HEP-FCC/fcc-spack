
from spack import *

class FccEdm(CMakePackage):
    """Event data model of FCC"""

    homepage = "https://github.com/HEP-FCC/fcc-edm"
    url      = "https://github.com/HEP-FCC/fcc-edm/archive/v0.5.5.tar.gz"
    git =      "https://github.com/HEP-FCC/fcc-edm.git"

    version('master', branch='master')
    version('0.5.6', sha256='aaf4ff58dfbdf9dfc3f755ad8b14d5e5701ed875f4031b1f7538deaf0f027705')
    version('0.5.5', sha256='a07a2f1304ce08a6d9819200c77e4a739f1e96f2ebb59715ebc27992e6a014e0')
    version('0.5.4', '236206ca4e00f239d574bfcd6aa44b53')
    version('0.5.3', 'ce4e041c795a22e7a6b4558ebe5a9545')
    version('0.5.2', '8f17139fae2bbc14fca88843791be9c3')
    version('0.5.1', '99aea85185a2afdf1f4eb6c24e7d9e74')
    version('0.5', '8ddae2d96d61f79ef113cc1e2e197189')
    version('0.4', '6c9f4d42bac4e55797e5e0f126290796')
    version('0.3', 'a361b57a5944dd00c8ad7960d0e6772e')
    version('0.2.2', '14ab88993995311f45e6927228fb8738')
    version('0.2.1', 'c68d0ab3c07d7f5c885b6d2be7a3be74')
    version('0.2', 'fe014e238e8afc76523f2e1ada9bc087')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    patch('cpack.patch')

    depends_on('cmake', type='build')
    depends_on('python', type='build')
    depends_on('dag')
    depends_on('root@6.08:')
    depends_on('podio@:0.9.2', when='@:0.5.5')
    depends_on('podio@0.10.0:', when='@0.5.6:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args

    # Override pre-defined test step
    # Multiple tests access to the same root file, thus we avoid parallel
    # execution at this stage
    def check(self):
        with working_dir(self.build_directory):
            make("test", "CTEST_OUTPUT_ON_FAIL=1")
