from spack import *


class Dag(CMakePackage):
    """The DAG tool supports traversal of a Directed Acyclic Graph (also known
    here as DAG)."""

    homepage = "https://github.com/HEP-FCC/dag"
    url      = "https://github.com/HEP-FCC/dag/archive/v0.1.tar.gz"

    version('0.1', '764c915de4ff36f8e195a28d6aa084a6')
