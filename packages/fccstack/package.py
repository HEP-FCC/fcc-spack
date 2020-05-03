from spack import *
from spack.package import PackageBase

class Fccstack(PackageBase):
    """Bundle package to install the FCC software stack."""

    version('1.0')

    maintainers = ['vvolkl']

    depends_on('fccdevel')
    depends_on('fccsw')
