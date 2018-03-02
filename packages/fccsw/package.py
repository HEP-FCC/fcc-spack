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


class Fccsw(CMakePackage):
    """software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.5.tar.gz"

    version('develop', git='https://github.com/HEP-FCC/FCCSW.git', branch='master')
    version('0.9',   'fbbfc1deeaab40757d05ebfcbfa7b0f5')
    version('0.5.1', 'e2e6e6fa40373c3a14ea823bb9bc0810')
    version('0.5', 'f2c849608ac1ab175f432a5e55dbe673')

    depends_on('cmake', type='build')
    depends_on('dd4hep')
    depends_on('delphes')
    depends_on('fastjet')
    depends_on('fcc-edm')
    depends_on('gaudi')
    depends_on('geant4')
    depends_on('hepmc')
    depends_on('pythia8')
    depends_on('root')
    depends_on('tbb')
    depends_on('acts-core')
    depends_on('papas')
    depends_on('xerces-c')
    depends_on('tricktrack')

    patch('permissions.patch', when='@0.9')

    def setup_environment(self, spack_env, run_env):
        # Need to explicitly add DD4hep libs to the LD_LIBRARY_PATH since
        # some cmake files (MakeGaudiMap.cmake) only rely on this variable
        spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['dd4hep'].prefix.lib)

        # Geant4 datasets
        datadir='/cvmfs/geant4.cern.ch/share/data'
        spack_env.set('G4LEVELGAMMADATA', datadir + '/PhotonEvaporation3.2')
        spack_env.set('G4NEUTRONXSDATA', datadir + '/G4NEUTRONXS1.4')
        spack_env.set('G4LEDATA', datadir + '/G4EMLOW6.48')
        spack_env.set('G4NEUTRONHPDATA', datadir + '/G4NDL4.5')
        spack_env.set('G4RADIOACTIVEDATA', datadir + '/RadioactiveDecay4.3')
        spack_env.set('G4ABLADATA', datadir + '/G4ABLA3.0')
        spack_env.set('G4PIIDATA', datadir + '/G4PII1.3')
        spack_env.set('G4SAIDXSDATA', datadir + '/G4SAIDDATA1.1')
        spack_env.set('G4REALSURFACEDATA', datadir + '/RealSurface1.0')
        # Lower versions than G4ENSDFSTATE2.0 fail
        spack_env.set('G4ENSDFSTATEDATA', datadir + '/G4ENSDFSTATE2.0')
