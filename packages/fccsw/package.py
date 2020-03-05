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
import llnl.util.tty as tty
import subprocess

class Fccsw(CMakePackage):
    """software framework of the FCC project"""
    homepage = "https://github.com/HEP-FCC/FCCSW/"
    url      = "https://github.com/HEP-FCC/FCCSW/archive/v0.5.tar.gz"

    version('develop', git='https://github.com/vvolkl/FCCSW.git', branch='master')
    version('0.12', sha256='a67151c12177882abd8afcf56bee47c2830c44cac749b23d08d005b45096b264')
    version('0.11', 'e3b5aa8f396cffae745305801eb8f7a38a8a7881')
    version('0.10',   '40b75f42fb51934cdc3c52049226ac39')
    version('0.9',   'fbbfc1deeaab40757d05ebfcbfa7b0f5')
    version('0.5.1', 'e2e6e6fa40373c3a14ea823bb9bc0810')
    version('0.5', 'f2c849608ac1ab175f432a5e55dbe673')

    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('lcg', default=True, description="Installed against an LCG Release")
    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('acts_core')
    depends_on('clhep')
    depends_on('dd4hep')
    depends_on('delphes')
    depends_on('gl2ps')
    depends_on('fastjet')

    # LCG Releases built with gcc7 use C++17
    depends_on('fcc-edm@0.5.5: cxxstd=17', when="%gcc@7:")
    depends_on('fcc-edm cxxstd=14', when="%gcc@:6.99")

    depends_on('gaudi')
    depends_on('geant4')
    depends_on('hepmc')
    depends_on('heppdt')

    # LCG Releases built with gcc7 or higher require C++17
    depends_on('papas@1.2.2: cxxstd=17', when="%gcc@7:")
    depends_on('papas cxxstd=14', when="%gcc@:6.99")

    depends_on('podio')
    depends_on('pythia8')
    depends_on('root')
    depends_on('tbb')

    #depends_on('tricktrack')
    depends_on('xerces-c')

    depends_on('vdt', when="+lcg")
    depends_on('python', when="+lcg")
    depends_on('davix', when="+lcg")

    patch('permissions.patch', when='@0.9')
    patch('ddeve.patch', when='@0.9 ^dd4hep@01-08')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        return args
    
    def setup_environment(self, spack_env, run_env):
        # Need to explicitly add DD4hep libs to the LD_LIBRARY_PATH since
        # some cmake files (MakeGaudiMap.cmake) only rely on this variable
        print "GAUDIi:", self.spec['gaudi'].prefix + "/lib/python2.7/site-packages/"
        spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['dd4hep'].prefix.lib)
        spack_env.prepend_path('PYTHONPATH', "/cvmfs/sft.cern.ch/lcg/releases/xenv/1.0.0-25c02/x86_64-centos7-gcc8-opt/lib/python2.7/site-packages/")

        # Gaudi automatically detects the processor if BINARY_TAG is not defined
        # in the environment. This leads to an error detecting a 'broadwell'
        # platform instead of 'x86_64'. This solves this issue.
        import platform
        binary_tag=["x86_64"]
        tty.msg(platform.linux_distribution()[0])
        if "CentOS" in platform.linux_distribution()[0]:
            binary_tag.append("centos7")
        else:
            binary_tag.append("slc6")

        compiler_labels = {
            "gcc@8.2.0": "gcc8",
            "gcc@8.3.0": "gcc8",
            "gcc@6.2.0": "gcc62"
        }

        binary_tag.append(compiler_labels[str(self.compiler.spec)])
        binary_tag.append("opt")

        spack_env.set('BINARY_TAG', "-".join(binary_tag))
        msg="Defining the following environment variable: BINARY_TAG="+"-".join(binary_tag)
        tty.msg(msg)
	
        # Set up Geant4 datasets
	# ToFix: This should be set by Geant4 itself
	geant4 = self.spec['geant4']
	geant4config = join_path(geant4.prefix.bin, "geant4-config")
        process_pipe = subprocess.Popen([geant4config, "--datasets"],
                                        stdout=subprocess.PIPE)
        result_datasets = process_pipe.communicate()[0]
        for line in result_datasets.rstrip("\n").split("\n"):
            dataset = line.split()
            # Format: directory name, environment variable, directory path
            g4variable = dataset[1]
            g4datapath = dataset[2]
            spack_env.set(g4variable, g4datapath)
