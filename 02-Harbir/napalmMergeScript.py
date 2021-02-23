import argparse
import os
import re
from napalm import get_network_driver
import json
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
from napalm.base.exceptions import ConnectionException
from datetime import datetime
from netmiko import ConnectHandler
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Script Name napalmMergeScript.py
#Parameters: 4
#Parameter : Name of Switch
#Parameter : Username with priviliged access
#Parameter : Password
#Parameter : Driver type, one of eos,ios,iosxr,junos,nxos,nxos_ssh
# python3 napalmMergeScript.py -s 10.190.25.62 -u dnac-device-admin -p y4NS 
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
def importFile(switchConn, switchFacts, fileNameAbsolutePath):
    print(f'Entering importFile, switch hostname: {switchFacts["hostname"]}.  File to import: {fileNameAbsolutePath}')
    #
    switchConn.load_merge_candidate(filename=fileNameAbsolutePath)
    diffs = switchConn.compare_config()
    if diffs == "":
        print("Configuration already applied")
        switchConn.discard_config()
    else:
        print(f'Following changes will be applied: \n{diffs}')
        switchConn.commit_config()
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
    #
    switchConn.open()
    #Lets get some information from device facts
    ios_output = switchConn.get_facts()
    #
    #Change config to add one loopback and advertise it in BGP
    newConfigNexus = "/root/scripts/rtr2_config.txt"
    newConfigIOS = "/root/scripts/rtr1_config.txt"
    #
    if (osType == "nxos") :
        importFile(switchConn, ios_output, newConfigNexus)
    elif(osType == "ios") :
        importFile(switchConn, ios_output, newConfigIOS)
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