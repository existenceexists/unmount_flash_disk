# Unmount Flash Disk

Unmount USB flash disk so it can be safely removed.

Prepare the application for all possible situations and errors.

Developed for Xubuntu operating system in 2019-05, but it may work on other operating systems and versions too.

----
### Dependencies
- Software Python version 3.7 or higher is required to be installed, because the argument 'capture_output' of the method 'subprocess.run' was added in Python 3.7 .
- Software Zenity is required to be installed.
- Software lsblk is required to be installed.
- Software udisksctl is required to be installed.

----
### Usage
Example of usage on Linux command line:

    python3.7 unmount_flash_disk.py;

Or if you are sure that your default Python version is 3.7 or higher, then you can run:

    python unmount_flash_disk.py;

Optional argument --help or -h can be given to get description of the application:

    python3.7 unmount_flash_disk.py --help;

----
### License

Copyright © 2019 František Brožka <sentientfanda@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://www.wtfpl.net/ for more details.
