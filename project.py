#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019-2021 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

"""
This is the project configuration file as well the starter script for iPug.
"""

import os

DEFAULT_EDK2_TAG = 'edk2-stable202011'

CODETREE = {
    'acpica'            : {
        'path'          : os.path.join(os.getcwd(), 'AcpiPkg'),
        'source'        : {
            'url'       : 'https://github.com/acpica/acpica.git',
            'signature' : 'R01_05_21',
        },
        'multiworkspace': True,
        'patch'         : 'git apply --directory=AcpiPkg AcpiPkg.patch',
    },
}
CODETREE['acpica-efi'] = {
        'path'          : os.path.join(os.getcwd(), 'AcpiPkg', 'generate'),
        'multiworkspace': True,
    }
CODETREE['source-tools'] = {
        'path'          : os.path.join(os.getcwd(), 'AcpiPkg', 'source'),
        'multiworkspace': True,
    }

DEFAULT_ACTIVE_PLATFORM = 'efi/AcpiPkg_nostdlib.dsc'

if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    import runpy
    runpy.run_module('ipug')

