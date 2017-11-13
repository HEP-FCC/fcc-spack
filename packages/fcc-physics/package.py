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


class FccPhysics(CMakePackage):
    """Event data model of FCC"""

    homepage = "https://github.com/HEP-FCC/fcc-physics/"
    url      = "https://github.com/HEP-FCC/fcc-physics/archive/v0.1.tar.gz"

    version('0.2.1', '93aeb48160d8fc5ae18e3568dd4f34b4', preferred=True)
    version('0.1.1', '8136978e23b5b9438646868f8e81d037')
    version('0.1', '89e4f57d0dc9335e2ad6ed796c5e2600')
    version('develop', git='https://github.com/HEP-FCC/fcc-physics.git', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    depends_on('cmake', type='build')
    depends_on('fcc-edm')
    depends_on('podio')
    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('fastjet')

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCPHYSICS', self.prefix)
