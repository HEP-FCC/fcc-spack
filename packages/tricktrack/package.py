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


class Tricktrack(CMakePackage):
    """TrickTrack aims to encapsulate the Cellular-Automaton based seeding code
    used in CMSSW in a standalone library."""

    homepage = "https://cern.ch/tricktrack"
    url      = "https://github.com/HEP-SF/TrickTrack/archive/v1.0.8.tar.gz"
    git      = "https://github.com/HEP-SF/TrickTrack.git"

    version('develop', branch='master')
    version('1.0.8', '014561e6be35f9b858dad8f9158c4746')
    version('1.0.7', '93573819088d0dee7c3a260d7c8a8a61')
    version('1.0.6', 'ef8cc9d5d9760935da2ef56aa98d9885')
    version('1.0.5', '65493aa89361c139c28f63b473459312')
    version('1.0.4', '7fefd2f94c4925d307897b483b9eb039')
    version('1.0.1', 'ec23cadf8b7fa4a343e513c7c988e27f')
    version('0.1',   'a75c6e2c7d7df5b713aa087827503e3c')

    variant('documentation',     default=False, 
            description='Build doxygen documentation')
    variant('python',            default=False, 
            description='Build python bindings')
    variant('logger',            default=False, 
            description='Use spdlog for logging')
    variant('logger_standalone', default=False, 
            description='Use spdlog standalone (as opposed to in a framework)')

    depends_on('doxygen', when="+documentation")
    depends_on('spdlog', when="+logger")
    depends_on('eigen', when="@1.0.4:")
    depends_on('python', when="+python", type=('run'))

    patch('eigen.patch', when="@1.0.4")
    patch('findeigen.patch', when="@1.0.4")

    def cmake_args(self):
  spec = self.spec

  args = [
      '-Dtricktrack_documentation:BOOL=%s' % (
    'ON' if '+documentation' in spec else 'OFF'),
      '-Dtricktrack_python:BOOL=%s' % (
    'ON' if '+python' in spec else 'OFF'),
  ]

  if '+logger' in spec:
      args.extend(['-DUSE_SPDLOG'])
  if '+logger_standalone' in spec:
      args.extend(['-DUSE_SPDLOG_STANDALONE'])

  return args
