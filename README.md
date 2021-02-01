acpica.efi.pug
===
**acpica.efi.pug** provides a handier way to build [AcpiPkg/acpidump.efi from ACPICA](https://github.com/acpica/acpica.git) using [iPug](https://github.com/timotheuslin/ipug).


## Prerequisites:
1. Python 3.7.0+
2. git 2.25.0+


## Generic prerequisites for the UDK/Edk2 build:
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or newer)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
6. motc (Xcode)
7. iPug (a PyPI package, installed through pip)
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)


## Tool installation for any Debian-Based Linux:
- `sudo apt update && sudo apt install nasm iasl build-essential uuid-dev python3-pip python-is-python3 && pip install "ipug>=0.2.3" --user`


## Usage: 
1. `git clone https://github.com/timotheuslin/acpica.efi.pug.git`
2. change-directory to folder **acpica.efi.pug** .
3. To build the code, run `python project.py setup`, then `python project.py` <br>
    For the 1st time setup, following code trees would be automatically git-cloned:
    - the [EDK2 code tree](https://github.com/tianocore/edk2)
        -  the openssl repo and some other submodules
    - [ACPICA's AcpiPkg](https://github.com/acpica/acpica.git)
4. Browse to folder **Build/Acpi** for the build results.
5. Browse to folder **Build/Conf** for CONF_PATH setting files.
6. Run `python project.py cleanall` to clean all the intermediate files. 
* You may have to figure out the correct way to launch a python script on your system. e.g. maybe through `python3`, or `py -3` using the python launcher.


## Build Status:
1. Built with Linux/GCC and Windows/VS2017.
2. Mock-up with ACPICA's code tag: `R01_10_20` and `R01_05_21`.


## Tech Notes:
1. By iPug, the full [EDK2 code tree](https://github.com/tianocore/edk2) is git-cloned-checked-out to:
    - %USERPROFILE%\.cache\pug\edk2 (Windows)
    - $HOME/.cache/pug/edk2 (Linux)
2. On Windows, the default MSVC tool chain tag is "vs2017x86". Before launching the build, you have to launch the VS's console through `x64 Native Tools Command Prompt for VS 2017` in the Windows start menu or call `vcvars32.bat` in CMD.exe console.
3. The folder **acpica.efi.pug**, as the current working directory, is assigned as the "WORKSPACE" directory. **[PACKAGES_PATH a.k.a. MULTIPLE-WORKSPACE](https://github.com/tianocore/tianocore.github.io/wiki/Multiple_Workspace)** is used here to implicitly reference other standard packages outside the current working directory tree.
4. A patch file, `AcpiPkg.patch` has been applied automatically in order to build acpidump_nostdlib.efi.
