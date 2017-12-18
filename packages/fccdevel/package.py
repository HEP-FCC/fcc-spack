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
from spack.package import PackageBase

class Fccdevel(PackageBase):
    """Dummy package to install the FCC software development environment."""

    phases = ['build', 'install']
    build_system_class = 'BundlePackage'

    url = 'https://github.com/citibeth/dummy/tarball/v1.0'

    version('1.0', 'e2b724dfcc31d735897971db91be89ff')

    depends_on('cmake', type='build')
    depends_on('dd4hep')
    depends_on('delphes')
    depends_on('fastjet')
    depends_on('fcc-edm')
    depends_on('fcc-physics')
    depends_on('gaudi')
    depends_on('geant4')
    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('root')
    depends_on('tbb')
    depends_on('acts-core')
    depends_on('papas')
    #depends_on('heppy') # As cmake package

    def build(self, spec, prefix):
        pass

    def install(self, spec, prefix):
        pass
