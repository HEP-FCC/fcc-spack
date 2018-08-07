##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class ActsCore(CMakePackage):
    """A Common Tracking Software (ACTS) Project provides a
    experiment-independent set of track reconstruction tools"""

    homepage = "https://gitlab.cern.ch/acts/acts-core"
    url      = "https://gitlab.cern.ch/acts/acts-core/repository/v0.05.02/archive.tar.gz"

    version('0.06.00', '7364779db21cbb39365e137672b75c74')
    version('0.05.03', '872272ff18b38a01fc3f7b5f33be9d01')
    version('0.05.02', 'c824e925145bbd316b892ebe0c1eddc3')

    depends_on('cmake@3.5:', type='build')
    depends_on('boost@1.62:')
    depends_on('eigen@3.2.9:')
    depends_on('root@6.08.00:')
    depends_on('dd4hep@1.02:')

    # Optional for documentation
    depends_on('doxygen@1.8.11:')
    depends_on('graphviz@2.26.00:')

    conflicts("%gcc@:6.1")

    patch('cmake.patch', when='@0.05.03')

    def url_for_version(self, version):
        url = "https://gitlab.cern.ch/acts/acts-core/repository"
        return "{0}/v{1}/archive.tar.gz".format(url, version)

    def cmake_args(self):
        spec = self.spec
        args = [
            "-DBUILD_DD4HEP_PLUGIN=ON",
            "-DBUILD_MATERIAL_PLUGIN=on",
            "-DBUILD_TGEO_PLUGIN=ON",
            "-DEIGEN_INCLUDE_DIR=%s" % spec['eigen'].prefix + "/include/eigen3"
        ]
        return args
