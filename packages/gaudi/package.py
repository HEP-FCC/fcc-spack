from spack import *
import llnl.util.tty as tty


class Gaudi(CMakePackage):
    """Gaudi framework."""
    homepage = "https://gaudi.cern.ch"
    url      = "https://gaudi.cern.ch"

    version('v27r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v27r1')
    version('v28r0', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r0')
    version('v28r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r1')
    version('v28r2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r2')
    version('v29r2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v29r2')
    version('30.1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r1')
    version('30.2', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r2')
    version('30.3', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r3')
    version('30.4', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r4')
    version('30.5', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v30r5')
    version('32.0', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v32r0')

    # Minimal Gaudi build
    depends_on("boost")
    depends_on('cppgsl', when='@32.0:')
    depends_on("intel-tbb")
    depends_on("libuuid")
    depends_on("python")
    depends_on('py-xenv@develop_2018-12-20:')
    depends_on('range-v3' )
    depends_on("root")
    depends_on("vdt", when="@32.0:, root@6.16:")
    depends_on("zlib")

    # optional
    # depends_on("py-qmtest")
    depends_on("clhep")
    depends_on("cppunit")
    depends_on("aida")
    depends_on("gperftools")
    depends_on("heppdt")

    depends_on('gsl')
    depends_on('relax')
    depends_on('xerces-c')

    patch('rt.patch', when="@30.1:30.5 ^boost@1.67:")
    patch('lcg95-gaudiv29v5.patch', when="@v29r2 ^boost@1.67:")
    patch('cxx17.patch', when="@:30.4 %gcc@8:")
    patch('BoostAllPython.patch', when="@v29r2 ^boost@1.67:")


    # In LCG_96 ROOT is installed with an external xz rather than the builtin,
    # so the genreflex binary needs to find it.
    # As root is installed as an external package we cannot modify its
    # setup_dependent_environment function to add the xz lib folder to the
    # LD_LIBRARY_PATH hence we need to do it here.
    depends_on('xz', when='^root@6.16:')

    def cmake_args(self):
        spec = self.spec
        options = []
        if '^boost@1.69:' in spec:
            options = [
                # Otherwise find_package(Boost) finds the wrong directories
                '-DBoost_NO_BOOST_CMAKE=TRUE',
            ]
        return options

    def setup_environment(self, spack_env, run_env):
        if 'xz' in self.spec:
            spack_env.prepend_path('LD_LIBRARY_PATH', self.spec['xz'].prefix.lib)

        # Gaudi automatically detects the processor if BINARY_TAG is not defined
        # in the environment. This leads to an error detecting a 'broadwell'
        # platform instead of 'x86_64'. This solves this issue.
        import platform
        binary_tag=["x86_64"]
        if "CentOS" in platform.linux_distribution():
            binary_tag.append("centos7")
        else:
            binary_tag.append("slc6")

        compiler_labels = {
            "gcc@8.2.0": "gcc8",
            "gcc@6.2.0": "gcc62"
        }

        binary_tag.append(compiler_labels[str(self.compiler.spec)])
        binary_tag.append("opt")

        spack_env.set('BINARY_TAG', "-".join(binary_tag))
        msg="Defining the following environment variable: BINARY_TAG="+"-".join(binary_tag)
        tty.msg(msg)
