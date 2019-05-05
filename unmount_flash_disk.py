#!/usr/bin/env python3.7

# Copyright © 2019 František Brožka <sentientfanda@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

"""Unmount flash disk so it can be safely removed."""

import argparse
import re
import subprocess
import sys


def parse_arguments():
    d="""
Unmount flash disk so it can be safely removed. 
Developed for Xubuntu operating system. 
Software Python version 3.7 or higher is required to be installed, because the argument 'capture_output' of the method 'subprocess.run' was added in python 3.7 . 
Software Zenity is required to be installed. 
Software lsblk is required to be installed. 
Software udisksctl is required to be installed. 
Example of usage on linux command line: python3.7 unmount_flash_disk.py; 
"""
    parser=argparse.ArgumentParser(description=d)
    parser.parse_args()

def exit_with_error(exit_code,message):
    m="""### ERROR!!! ###
### Error message:
"""+str(message)+"""
###
### Error encountered. Aborting. ###
"""
    print(m)
    subprocess.run(["zenity","--error","--ellipsize","--text",m])
    sys.exit(exit_code)

def display_message_success():
    m="""Výborně. Úspěch. Nyní můžete flešku bez obav odebrat.

Přejeme Vám hezký den.
Nezapomeňte se dnes celý den usmívat.
Dnes je nádherný den.
"""
    print(m)
    subprocess.run(["zenity","--info","--ellipsize","--icon-name","weather-clear","--text",m],capture_output=True)

def check_python_version():
    if sys.version_info[0]<3 or (sys.version_info[0]==3 and sys.version_info[1]<7):
        m="""This application requires python version 3.7 or higher to be installed and used to run this application, because the argument 'capture_output' of the method 'subprocess.run' was added in python 3.7 . 
The version of python that you used to run this application is '"""+sys.version+"'"
        exit_with_error(1,m)
    print("""### Python version 3.7 or higher is installed. ###""")

def check_if_zenity_installed():
    p=subprocess.run(["zenity","--help"],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,"""
Zenity is required to be installed 
and it appears that it is not installed 
or is not accessible using the command 'zenity'. 
""")
    print("""### Zenity is installed. ###""")

def check_if_lsblk_installed():
    p=subprocess.run(["lsblk","--help"],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,"""
Application lsblk is required to be installed 
and it seems that it is not installed 
or is not accessible using the command 'lsblk'. 
""")
    print("""### lsblk is installed. ###""")

def check_if_udisksctl_installed():
    p=subprocess.run(["udisksctl","help"],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,"""
Application udisksctl is required to be installed 
and it seems that it is not installed 
or is not accessible using the command 'udisksctl'. 
""")
    print("""### udisksctl is installed. ###""")

def check_if_flash_disk_mounted():
    print("""### Searching for mount point ###""")
    p=subprocess.run(["lsblk","-l"],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,p.stderr.decode("utf-8").rstrip('\n'))
    output=p.stdout.decode("utf-8").rstrip('\n')
    path_search=re.search("^(\w+)\W.*(/media/.*)$",output,flags=re.MULTILINE)
    if path_search is None:
        exit_with_error(1,"""
Vypadá to, že flash disk není připojen 
a můžete ho odebrat.

Nebo se může jednat o chybu.
Kontaktujte prosím svého poradce pro počítač.

Text pro poradce pro počítač:
It seems that flash disk is not mounted
or the mount point is not on an expected path
in folder '/media/' .
Run command 'lsblk -l' to see all mount points.
""")
    mount_point_block=path_search.group(1)
    print("""Mount point found under name: """+mount_point_block+"""
Flash disk mounted to path: """+path_search.group(2))
    return mount_point_block

def unmount_flash_disk(mount_point_block):
    print("""### Unmounting flash disk ###""")
    mount_point_block="/dev/"+mount_point_block
    print("""Unmounting block device """+mount_point_block)
    p=subprocess.run(["udisksctl","unmount","--block-device",mount_point_block],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,p.stderr.decode("utf-8").rstrip('\n'))
    print("""Powering off block device """+mount_point_block)
    p=subprocess.run(["udisksctl","power-off","--block-device",mount_point_block],capture_output=True)
    if p.returncode!=0:
        exit_with_error(1,p.stderr.decode("utf-8").rstrip('\n'))
    print("""### Succesfully unmounted flash disk. ###""")

def main():
    print("### Starting... ###")
    print("### Warning: This application requires Python version 3.7 or higher, and Zenity and lsblk and udisksctl to be installed. ###")
    parse_arguments()
    check_python_version()
    check_if_zenity_installed()
    check_if_lsblk_installed()
    check_if_udisksctl_installed()
    mount_point_block=check_if_flash_disk_mounted()
    unmount_flash_disk(mount_point_block)
    display_message_success()
    print("### Finished ###")
    print("### Successfully finished without an error. Exiting. ###")
    sys.exit(0)

if __name__ == "__main__":
    main()

