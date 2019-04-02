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


class Delphes(CMakePackage):
    """ Delphes is a C++ framework, performing a fast multipurpose detector
    response simulation."""

    homepage = "https://cp3.irmp.ucl.ac.be/projects/delphes"
    url      = "https://github.com/delphes/delphes/archive/3.4.1.tar.gz"

    version('3.4.2pre05', '829f221135ec27afba2a1ac57da29858')
    version('3.4.1',      '630182fc0cf96c6ca0a96dcddc0f702e')

    depends_on('root')
    depends_on('tcl')
