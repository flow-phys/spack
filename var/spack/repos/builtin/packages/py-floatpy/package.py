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


class PyFloatpy(PythonPackage):
    """Flow physics toolbox
    """
    homepage = "https://github.com/flow-phys/FloATPy"
    url      = "https://github.com/flow-phys/FloATPy"

    version('develop', git='https://github.com/flow-phys/FloATPy.git', branch='master')

    depends_on('python@2.7:2.8,3.3:')
    depends_on('py-setuptools', type='build')
    depends_on('mpi')
    depends_on('py-mpi4py')
    depends_on('py-numpy')
    depends_on('py-matplotlib')
    depends_on('py-f90wrap')


    def install_args(self, spec, prefix):
        """Arguments to pass to install."""
        args = ['--prefix={0}'.format(prefix)]

        # This option causes python packages (including setuptools) NOT
        # to create eggs or easy-install.pth files.  Instead, they
        # install naturally into $prefix/pythonX.Y/site-packages.
        #
        # Eggs add an extra level of indirection to sys.path, slowing
        # down large HPC runs.  They are also deprecated in favor of
        # wheels, which use a normal layout when installed.
        #
        # Spack manages the package directory on its own by symlinking
        # extensions into the site-packages directory, so we don't really
        # need the .pth files or egg directories, anyway.
        if ('py-setuptools' == spec.name or          # this is setuptools, or
            'py-setuptools' in spec._dependencies):  # it's an immediate dep
            args += ['--root=/']

        return args
