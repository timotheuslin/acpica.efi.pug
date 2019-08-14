acpica.pug
===
**acpica.pug** provides another way to build [ACPICA's AcpiPkg](https://github.com/acpica/acpica.git) using [iPug](https://github.com/timotheuslin/ipug).


## Prerequisites:
1. Python 3.6.0+
2. git 2.19.0+


## Generic prerequisites for the UDK build:
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or newer)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
6. motc (Xcode)
7. iPug (a Python package, installed through pip)
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)


## Tool installation for any Debian-Based Linux:
- `sudo apt update; sudo apt install nasm iasl build-essential uuid-dev; pip install "ipug>=0.1.4" --user`


## Usage: 
1. `git clone https://github.com/timotheuslin/acpica.pug.git`
2. In the command console, change-directory to folder **acpica.pug** .
3. To build the code, run `python project.py`. <br>
    For the 1st time setup, following code trees would be automatically git-cloned:
    - the [UDK code tree](https://github.com/tianocore/edk2)
    - the openssl repo (and some other CryptoPkg's submodules maybe)
    - [ACPICA's AcpiPkg](https://github.com/acpica/acpica.git)
4. Browse to folder **Build/Acpi** for the build results.
5. Browse to folder **Build/Conf** for CONF_PATH setting files.
6. Run `python project.py {clean, cleanall}` to clean (all) the intermediate files.


## Known issues:
1. Working for Linux/GCC only. Windows/MSVC seems having some C99 incompatibility issues to deal with. Xcode is not tested.


## Tech notes:
1. The full [UDK code tree](https://github.com/tianocore/edk2) is git-cloned-checked-out to:
    - %USERPROFILE%\.cache\pug\edk2 (Windows)
    - $HOME/.cache/pug/edk2 (Linux)
2. On Windows, the default MSVC tool chain tag is "vs2012x86". The following command should be run first in the command console:
    - "C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x86
3. The folder **acpica.pug**, as the current working directory, is assigned as the "WORKSPACE" directory. **[PACKAGES_PATH a.k.a. MULTIPLE-WORKSPACE](https://github.com/tianocore/tianocore.github.io/wiki/Multiple_Workspace)** is used here to implicitly reference other standard packages outside the current working directory tree.
4. A patch file, `AcpiPkg.patch` has been applied automatically to build acpidump_stdlib.efi and acpidump_nostdlib.efi at the same time.

## Have Fun!
