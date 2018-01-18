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

class PyGitpython(PythonPackage):
    """GitPython is a python library used to interact with git repositories,
    high-level like git-porcelain, or low-level like git-plumbing.."""

    homepage = "https://github.com/gitpython-developers/GitPython"
    url      = "https://pypi.python.org/packages/1c/08/a2b5ba4ad43c4c33066ced2c45958593ab2554bb0d09f7ecb9bf9092e5f6/GitPython-2.1.8.tar.gz#md5=7a94ee1b923fb772a2a0c6649430a17c"

    version('2.1.8', '7a94ee1b923fb772a2a0c6649430a17c')

    depends_on('git', type=('build', 'run'))
