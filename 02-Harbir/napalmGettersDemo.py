import argparse
from napalm import get_network_driver
import json
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
from napalm.base.exceptions import ConnectionException
from netmiko import ConnectHandler
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Script Name napalmGettersDemo.py
#Parameters: 4
#Parameter1 : Name of Switch
#Parameter2 : Username with priviliged access
#Parameter3 : Password
#Parameter4 : Driver type, one of eos,ios,iosxr,junos,nxos,nxos_ssh
# python3 napalmGettersDemo.py -s 10.190.25.62 -u admin -p admin -o nxos 
#
switchIP = ""
userName = ""
userPassword = ""
osType = ""
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-s", "--switchip", required=True,
   help="Switch IP or FQDN")
ap.add_argument("-u", "--username", required=True,
   help="User name with Enable Access")
ap.add_argument("-p", "--pwd", required=True,
   help="Password for user with priviliged access")
ap.add_argument("-o", "--os", required=True,
   help="OsType must be Naplalm supported type, example: ios")

args = ap.parse_args()

switchIP = args.switchip
userName = args.username
userPassword = args.pwd
osType = args.os
# Procs
def printLineOfHashes():
    print(f'{"#" * 72}')
#     
#####################
########Main#########
#####################
optional_args = { }
if (osType == "nxos") :
    optional_args = {'port': '65000' }
#
driver = get_network_driver(osType)
#
switchConn=""
#
try:
    #
    switchConn = driver(switchIP, userName, userPassword, optional_args=optional_args)
    switchConn.open()
    #Lets get some information from device facts
    ios_output = switchConn.get_facts()
    print(f'Facts retrieved: \n {json.dumps(ios_output, indent=2)}')
    printLineOfHashes()
    #
    hostname = ios_output['hostname']
    model = ios_output['model']
    os_version = ios_output['os_version']
    print(f'Device has hostname: {model}; model: {model}; os_version: {os_version}')
    printLineOfHashes()
    #get_lldp_neighbors
    lldpNeighborsInfo = switchConn.get_lldp_neighbors()
    print(f'LLDP Information: \n {json.dumps(lldpNeighborsInfo, indent=2)}')
    printLineOfHashes()
    #Get BGP neighbors
    bgpNeighborsInfo = switchConn.get_bgp_neighbors()
    print(f'BGP Neighbor Information: \n {json.dumps(bgpNeighborsInfo, indent=2)}')
    printLineOfHashes()
    try:
        bgpNeighborsInfoDetail = switchConn.get_bgp_neighbors_detail()
        print(f'BGP Neighbor Detail Information: \n {json.dumps(bgpNeighborsInfoDetail, indent=2)}')
        printLineOfHashes()
    except RuntimeError as runTimeErrorException:
        print(f'Run time error, exception received from get_bgp_neighbors_detail() is: {repr(runTimeErrorException)}')
    #         
except AuthenticationException:
    print(f'Authentication failed, please verify your credentials')
except ConnectionException as connectFailure:
    print(f'Unable to establish SSH connection: {connectFailure}')
except SSHException as sshException:
    print(f'Unable to establish SSH connection: {sshException}')
except BadHostKeyException as badHostKeyException:
    print(f'Unable to verify server \'s host key {badHostKeyException}')
except RuntimeError as runTimeErrorException:
     print(f'Run time error, exception received is: {repr(runTimeErrorException)}')
finally:
    switchConn.close() 