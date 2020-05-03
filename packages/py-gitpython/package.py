
from spack import *

class PyGitpython(PythonPackage):
    """GitPython is a python library used to interact with git repositories,
    high-level like git-porcelain, or low-level like git-plumbing.."""

    homepage = "https://github.com/gitpython-developers/GitPython"
    url      = "https://pypi.python.org/packages/1c/08/a2b5ba4ad43c4c33066ced2c45958593ab2554bb0d09f7ecb9bf9092e5f6/GitPython-2.1.8.tar.gz#md5=7a94ee1b923fb772a2a0c6649430a17c"

    version('2.1.8', '7a94ee1b923fb772a2a0c6649430a17c')

    depends_on('git', type=('build', 'run'))
