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


class Podio(Package):
    """PODIO, or plain-old-data I/O, is a C++ library to support the creation
    and handling of data models in particle physics."""

    homepage = "https://github.com/HEP-FCC/podio"
    url      = "https://github.com/HEP-FCC/podio/archive/v0.8.tar.gz"

    version('0.8', '07bf090649fc8e3b94e348e6b7fb8c7e')
    version('0.7', '79e11c02c8d588f7b1dfc39b7de4eed9', preferred=True)
    version('0.6', '1a1d2aa70fc16cce372ce10c3612c32d')
    version('develop', git='https://github.com/HEP-FCC/podio.git', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    depends_on('cmake')
    depends_on('root@6.08.06:')
    depends_on('python@2.7:')
    depends_on('py-pyyaml')

    def install(self,spec, prefix):
        cmake("-DCMAKE_INSTALL_PREFIX:PATH=%s" % prefix)
        make()
        make("install")

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('PODIO', self.prefix)
