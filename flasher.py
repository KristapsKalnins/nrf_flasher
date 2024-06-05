import sys
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
        if port.description.startswith("nRF52 SDFU USB"):
            resultPorts.append(port.name)

    return resultPorts

def flash_firmware(firmware_path, nrf_ports):
    flash_procs = []
    for port in nrf_ports:
        flash_procs.append(subprocess.Popen("nrfutil dfu usb-serial -pkg {} -p {}".format(firmware_path, port), shell=True));
    for proc in flash_procs:
        proc.wait()


if __name__ == '__main__':
    nrf_ports = listPorts()
    path = sys.argv[1]
    flash_firmware(path, nrf_ports)