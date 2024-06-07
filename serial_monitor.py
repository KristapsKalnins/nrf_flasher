import sys
import os
import glob
import serial
import serial.tools.list_ports
import subprocess

def listPorts():
    """!
    @brief Provide a list of names of serial ports that can be opened as well as a
    a list of Arduino models.
    @return A tuple of the port list and a corresponding list of device descriptions
    """

    ports = list( serial.tools.list_ports.comports() )

    resultPorts = []
    descriptions = []
    for port in ports:
        if port.description.startswith("USB Serial Device"):
            resultPorts.append(port.name)

    return resultPorts

def open_serial_monitors(serial_ports):
    flash_procs = []
    for port in serial_ports:
        subprocess.Popen("start /wait cmd /c \"C:\\msys64\\usr\\bin\\env MSYSTEM=MSYS /usr/bin/bash -lc \"tio -b 115200 {}\"\"".format(port), shell=True)


if __name__ == '__main__':
    serial_ports = listPorts()
    open_serial_monitors(serial_ports)