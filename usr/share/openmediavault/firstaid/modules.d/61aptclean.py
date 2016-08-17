#!/usr/bin/env python3
#
# @license   http://www.gnu.org/licenses/gpl.html GPL Version 3
# @author    Volker Theile <volker.theile@openmediavault.org>
# @copyright Copyright (c) 2009-2016 Volker Theile
#
# OpenMediaVault is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# OpenMediaVault is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenMediaVault. If not, see <http://www.gnu.org/licenses/>.
import sys
import subprocess
import openmediavault as omv

class Module:
	def get_description(self):
		return "Clean apt"

	def execute(self):
		try:
			print("Cleaning apt.  Please wait ...")
			subprocess.call([ "apt-get", "clean" ])
			subprocess.call([ "dpkg", "--clear-avail" ])
			subprocess.call([ "rm", "-rfv", "/var/lib/apt/lists/*" ])
			#subprocess.call([ "omv_purge_internal_cache" ])
			subprocess.call([ "rm", "-fv", "/var/cache/openmediavault/archives/*" ])
			subprocess.call([ "touch", "/var/cache/openmediavault/archives/Packages" ])
			subprocess.call([ "apt-get", "update" ])
		except Exception as e:
			omv.log.error(str(e))
			return 1
		return 0

if __name__ == "__main__":
	module = Module();
	sys.exit(module.execute())