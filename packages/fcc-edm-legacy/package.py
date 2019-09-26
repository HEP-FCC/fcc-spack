##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install fcc-edm-legacy
#
# You can edit this file again by typing:
#
#     spack edit fcc-edm-legacy
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class FccEdmLegacy(CMakePackage):
    """FCCEDM"""

    """Event data model of FCC"""

    homepage = "https://github.com/HEP-FCC/fcc-edm-legacy"
    url      = "https://github.com/HEP-FCC/fcc-edm-legacy/archive/v0.1.0.zip"

    version('0.1.0', '97a4bdfb355980f6556f9dc032f23e62')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    depends_on('cmake', type='build')
    depends_on('python', type='build')
    depends_on('dag')
    depends_on('root')
    depends_on('podio')

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCEDMLEGACY', self.prefix)
