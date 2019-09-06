# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class GuineaPig(Package):
    """Generator of Unwanted Interactions for Numerical Experiment 
    Analysis Program Interfaced to GEANT (C++ version)"""

    homepage = "https://gitlab.cern.ch/clic-software/guinea-pig"
    url      = "https://gitlab.cern.ch/clic-software/guinea-pig/-/archive/v1.2.2rc/guinea-pig-v1.2.2rc.zip"

    version('1.2.2rc', 'fec0d1b6aa72523eec4e7c71bca2c1ff', )

    variant('fftw2', default=False)
    variant('fftw3', default=False)

    depends_on('fftw@2.0.0:2.9.9', when="+fftw2")
    depends_on('fftw@3.0.0:', when="+fftw3")

    def install(self, spec, prefix):
	if '+fftw2' in spec:
            configure("--prefix=%s" % prefix,
                      "-enable-fftw2",
                      "-with-fftwdir=%s" % spec['fftw'])
        elif '+fftw3' in spec:
            configure("--prefix=%s" % prefix,
                      "-enable-fftw3",
                      "-with-fftwdir=%s" % spec['fftw'].prefix)
        else:
            configure('--prefix=%s' % prefix)
	
        make()
        make('install')

    def cmake_args(self):
        args = []

        if '+fftw2' in self.spec:
            args.append('-enable-fftw2')

        if '+fftw3' in self.spec:
            args.append("-enable-fftw3")
        return args
