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

    # in LCG_96 ROOT is installed with an external xz rather than the builtin,
    # so the genreflex binary needs to find it.
    # As root is installed as an external package we cannot modify its
    # setup_dependent_environment function to add the xz lib folder to the
    # LD_LIBRARY_PATH hence we need to do it here.
    depends_on('xz', when='^root@6.16:')

    # Override pre-defined test step
    # Multiple tests access to the same root file, thus we avoid parallel
    # execution at this stage
    def check(self):
        with working_dir(self.build_directory):
            make("test", "CTEST_OUTPUT_ON_FAIL=1")
    
    def setup_environment(self, spack_env, run_env):
	# needed for genreflex
    	spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
    	run_env.prepend_path('LD_LIBRARY_PATH', self.spec['root'].prefix.lib)
        if 'xz' in self.spec:
            spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['xz'].prefix.lib)

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('FCCEDMLEGACY', self.prefix)
