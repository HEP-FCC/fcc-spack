
from spack import *


class PyFcchhanalyses(PythonPackage):
    """Produce flat ROOT trees using FCCSW EDM root files."""

    homepage = "https://github.com/HEP-FCC/FCChhAnalyses"
    git      = "https://github.com/HEP-FCC/FCChhAnalyses"

    version('0.1.1', tag='v0.1.1')

    depends_on('py-setuptools',   type='build')
    depends_on('py-wheel',        type='build')
    depends_on('root',            type=('run'))
    depends_on('heppy',           type=('run'))

    # Prevent passing --single-version-externally-managed to
    # setup.py, which it does not support.
    def install_args(self, spec, prefix):
        return ['--prefix={0}'.format(prefix), '--root=/']
