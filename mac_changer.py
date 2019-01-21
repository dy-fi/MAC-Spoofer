#!/usr/bin/env python
# insures python can connect to the enviroment it's in

import subprocess as sp
import platform

# gets the identity of the os or returns 0
def identity():
    if platform.system():
        return platform.system()
    else:
        return 0


# changes the MAC address on Linux machines or returns an
def linux_changer(interface, mac):
    try:
        sp.call('ifconfig ' + interface + ' down', shell='True')
        sp.call('ifconfig ' + interface +  ' hw ether ' + mac, shell='True')
        sp.call('ifconfig ' + interface + ' up', shell='True')

        return 'Success!'

    except:
        return 'Could not change MAC'

    except KeyboardInterupt:
        return 'Operation was cancelled by the user'


# changes the MAC address assuming the Darwin system uses bash
def darwin_changer(interface):
    try:
        sp.call('ifconfig ' + interface + ' down' shell=)
        sp.call('ifconfig ' + interface + ' ether ' + mac, shell='True')
        sp.call('ifconfig ' + interface + ' up', shell='True')

        return 'Success!'

    except:
        return 'Could not change MAC'

    except KeyboardInterupt:
        return 'Operation was cancelled by the user'
        

def run_loop():
    '''
        Determine the system and execute the appropriate shell script
    '''

    new_mac = input('Enter the name of the desired MAC address or enter nothing to have one randomly generated for you: \n')
    interface = input('Manually set the interface to be changed (optional): \n')

    if new_mac == 'none':
        # generate random MAC using regex on the host machine to ensure security.
        new_mac == sp.call('openssl rand -hex 6 | sed ‘s/\(..\)/\1:/g; s/.$//’', shell='True')

    # decide which system is being used

    # Linux
    if identity() == 'Linux':
        if interface == 'none':
            interface == 'eth0'

        return linux_changer(interface, new_mac)

    # Darwin
    if identity() == 'Darwin':
        if interface == 'none':
            interface == 'en0'

        option = input('Are you running on a MAC OS distribution? (y/n)')

        if option.lower() == 'n':
            print('This Darwin system might not be supported yet, but you can try anyways')

        return darwin_changer(interface, new_mac)
