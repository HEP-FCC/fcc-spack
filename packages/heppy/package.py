
from spack import *

class Heppy(PythonPackage):
    """High Energy Physics with PYthon (HEPPY) is a modular python framework
    for the analysis of collision events."""

    homepage = ""
    url      = "heppy"

    version('2.1', git='https://github.com/HEP-FCC/heppy.git', tag='v2.1')
    version('2.0', git='https://github.com/HEP-FCC/heppy.git', tag='v2.0')
    version('develop', git='https://github.com/HEP-FCC/heppy.git')


    depends_on('py-setuptools',   type='build')
    depends_on('py-wheel',        type='build')
    depends_on('py-pyyaml')
    depends_on('py-gitpython')
    depends_on('root')
    depends_on('python@2.7')

    def install_args(self, spec, prefix):
        return ['--prefix={0}'.format(prefix), '--root=/']

    def setup_environment(self, spack_env, run_env):
        run_env.set('HEPPY', self.prefix + "/heppy")
