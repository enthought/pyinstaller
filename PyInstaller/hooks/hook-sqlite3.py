#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


from PyInstaller.hooks.hookutils import collect_submodules

hiddenimports = []

for mod in collect_submodules('sqlite3'):
    if not mod.startswith('sqlite3.test'):
        hiddenimports.append(mod)
