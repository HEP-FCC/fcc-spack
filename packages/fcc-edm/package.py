##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
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


class FccEdm(CMakePackage):
    """Event data model of FCC"""

    homepage = "https://github.com/HEP-FCC/fcc-edm"
    url      = "https://github.com/HEP-FCC/fcc-edm/archive/v0.5.1.tar.gz"

    version('0.5.1', '99aea85185a2afdf1f4eb6c24e7d9e74')
    version('0.5', '8ddae2d96d61f79ef113cc1e2e197189')
    version('0.4', '6c9f4d42bac4e55797e5e0f126290796')
    version('0.3', 'a361b57a5944dd00c8ad7960d0e6772e')
    version('0.2.2', '14ab88993995311f45e6927228fb8738')
    version('0.2.1', 'c68d0ab3c07d7f5c885b6d2be7a3be74')
    version('0.2', 'fe014e238e8afc76523f2e1ada9bc087')
    version('develop', git='https://github.com/HEP-FCC/fcc-edm.git', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    conflicts('podio@0.8')

    depends_on('cmake', type='build')
    depends_on('python', type='build')
    depends_on('dag', when='@0.4:')
    depends_on('root')
    depends_on('podio@0.7')

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCEDM', self.prefix)
