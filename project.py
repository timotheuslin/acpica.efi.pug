#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

"""
This is the project configuration file as well the starter script for iPug.
"""

import os

DEFAULT_EDK2_TAG = 'edk2-stable201905'

CODETREE = {
    'acpica'            : {
        'path'          : os.path.join(os.getcwd(), 'AcpiPkg'),
        'source'        : {
            'url'       : 'https://github.com/acpica/acpica.git',
            'signature' : '',
        },
        'multiworkspace': True,
        'patch'         : 'git apply --directory=AcpiPkg AcpiPkg.patch',
    },

    # edk2-libc is a new edk2 repo since edk2-stable201905. StdLib resides in this repo.
    'edk2-libc'    : {
        'path'          : os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2-libc'),
        'source'        : {
            'url'       : 'https://github.com/tianocore/edk2-libc.git',
            'signature' : '6168716',   # 61687168fe02ac4d933a36c9145fdd242ac424d1 @ Apr/25/2019
        },
        'multiworkspace': True,
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

if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    PKG_DSC = 'efi/AcpiPkg_stdlib.dsc'
    IPUG_CMD = 'ipug {0} -p {1}'.format(' '.join(sys.argv[1:]), PKG_DSC)
    print(IPUG_CMD)
    os.system(IPUG_CMD)
