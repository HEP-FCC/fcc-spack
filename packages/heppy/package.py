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

class Heppy(Package):
    """High Energy Physics with PYthon (HEPPY) is a modular python framework
    for the analysis of collision events."""

    homepage = ""
    url      = "heppy"

    version('develop', git='https://github.com/HEP-FCC/heppy.git')

    depends_on('py-pyyaml')
    depends_on('py-gitpython')
    depends_on('root')
    depends_on('python@2.6:')

    patch('init.patch')

    def install(self, spec, prefix):
        source_directory = self.stage.source_path

        cp = which('cp')
        mkdirp('%s/lib/python2.7/site-packages' % prefix)
        cp('-r', source_directory, '%s/lib/python2.7/site-packages/heppy' % prefix)

        env['HEPPY'] = prefix + "/heppy"

    def setup_environment(self, spack_env, run_env):
        run_env.set('HEPPY', self.prefix + "/heppy")
