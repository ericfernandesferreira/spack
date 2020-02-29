#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install bullet
#
# You can edit this file again by typing:
#
#     spack edit bullet
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Bullet(CMakePackage):
    """This is the official C++ source code repository of the
    Bullet Physics SDK: real-time collision detection and
    multi-physics simulation for VR, games, visual effects,
    robotics, machine learning etc."""

    # Add a proper url for your package's homepage here.
    homepage = "https://bulletphysics.org/"
    url      = "https://github.com/bulletphysics/bullet3/archive/2.89.tar.gz"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['https://github.com/erwincoumans']

    version('2.89', sha256='621b36e91c0371933f3c2156db22c083383164881d2a6b84636759dc4cbb0bb8')

    # Add dependencies if required.

    def cmake_args(self):
        args = []
        return args