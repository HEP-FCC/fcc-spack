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


class Papas(CMakePackage):
    """PAPAS (PArametrized PArticle Simulation) provides simulation and
    reconstruction reconstruction algorithm which is designed to allow users to
    test the performance of detector design."""

    homepage = "https://github.com/HEP-FCC/papas"
    url      = "https://github.com/HEP-FCC/papas/archive/1.2.2.tar.gz"

    version('1.2.2', sha256='0f469d54eec726fdf654892a98720696499be0cf73db266e9715b01cb6c9c60c')
    version('1.2.1', '78f34649bd7b82aa1e8eb27b69dae8d1')
    version('1.2.0', '74d700ca5872872b2beda7e5862bfaa4')
    version('develop', git='https://github.com/HEP-FCC/papas.git', branch='master')

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    variant('cxxstd',
            default='14',
            values=('14', '17'),
            multi=False,
	    description='Use the specified C++ standard when building.')

    depends_on('fcc-physics')
    depends_on('fcc-edm')
    depends_on('podio')
    depends_on('pythia8')


    def cmake_args(self):
	args = []

	# C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)

	return args

    def setup_dependent_environment(self, spack_env, run_env, dspec):
        spack_env.set('PAPAS', self.prefix)
