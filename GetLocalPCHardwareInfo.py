import subprocess


def get_hardware_info():
    # 获取CPU信息
    cpu_info = subprocess.check_output(['lscpu'])
    print("CPU Info:")
    print(cpu_info.decode('utf-8'))

    # 获取内存信息
    mem_info = subprocess.check_output(['free', '-m'])
    print("\nMemory Info:")
    print(mem_info.decode('utf-8'))

    # 获取磁盘信息
    disk_info = subprocess.check_output(['lsblk', '-o', 'NAME,ROTA,SIZE,TYPE,MOUNTPOINT'])
    print("\nDisk Info:")
    print(disk_info.decode('utf-8'))

    # 获取PCI设备信息
    pci_info = subprocess.check_output(['lspci'])
    print("\nPCI Devices:")
    print(pci_info.decode('utf-8'))

    # 获取主板和BIOS信息, 注意需要Root权限才能运行这段程序
    motherboard_info = subprocess.check_output(['dmidecode', '-t', 'baseboard'])
    bios_info = subprocess.check_output(['dmidecode', '-t', 'bios'])
    print("\nMotherboard Info:")
    print(motherboard_info.decode('utf-8'))
    print("\nBIOS Info:")
    print(bios_info.decode('utf-8'))

get_hardware_info()