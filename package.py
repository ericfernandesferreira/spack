from spack import *


class Spek(AutotoolsPackage):
    """Spek is an acoustic spectrum analyser written in C and C++.
    It uses FFmpeg libraries for audio decoding and wxWidgets
    for the GUI."""

    # Add a proper url for your package's homepage here.
    homepage = "https://spek.cc"
    url      = "https://github.com/alexkay/spek/archive/v0.8.3.tar.gz"
    git      = "https://github.com/alexkay/spek.git"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['https://github.com/alexkay']

    version('0.8.3', sha256='f5c09d0062aaafe882e2e617f6d5db2ab540e2a657c1bee38260f7f0567bf175')
    version('master', branch='master')

    depends_on('autoconf',   type='build')
    depends_on('automake',   type='build')
    depends_on('libtool',    type='build')
    depends_on('m4',         type='build')
    depends_on('gettext',    type='build')

    # Add additional dependencies if required.
    depends_on('ncurses@6.1+termlib')
    depends_on('ncurses termlib=true')
    depends_on('ffmpeg@3.2.4')
    depends_on('perl@5.8.1:5.26.3')
    depends_on('mesa llvm=false')
    depends_on('wxwidgets@3.0.4')

    def autoreconf(self, spec, prefix):
        # Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # Add arguments other than --prefix
        # If not needed delete this function
        args = []
        return args