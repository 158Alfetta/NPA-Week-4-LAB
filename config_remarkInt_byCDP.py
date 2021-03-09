import netmiko
import threading
import re

# Management Plane content
DICT_OF_DEVICE = {
    "R0":"172.31.177.1",
    "R1":"172.31.177.4",
    "R2":"172.31.177.5",
    "R3":"172.31.177.6",
    "R4":"172.31.177.7",
    "R5":"172.31.177.9",
    "S0":"172.31.177.2",
    "S1":"172.31.177.3",
    "S2":"172.31.177.8"
}

username = "admin"
password = "cisco"


def collectData(device):
    device_params = {
        'device_type':'cisco_ios',
        'ip':DICT_OF_DEVICE[device],
        'username':username,
        'password':password
    }

    ssh = netmiko.ConnectHandler(**device_params)
    result = ssh.send_command("show cdp neighbors detail")
    print(result)
    ssh.disconnect()

    return result

def searchDataofNext(cdp_detail):
    regex = re.compile("Device\sID: \w*")
    n_hostname = regex.findall(cdp_detail)
    list_n_host = [x.split(' ')[-1] for x in n_hostname]
    print("Next Hostname ", list_n_host)
    
    regex = re.compile("Interface:.+,")
    l_interface = regex.findall(cdp_detail)
    list_l_interface = [x.split(' ')[-1].strip(',') for x in l_interface]
    print("Local Interface ", list_l_interface)

    regex = re.compile("Port ID \(outgoing port\).+")
    n_interface = regex.findall(cdp_detail)
    list_n_interface = [x.split(' ')[-1] for x in n_interface]
    print("Local Interface ", list_n_interface)
    
    return list_n_host, list_l_interface, list_n_interface

def settingDesc(device, local_int, Desc):
    device_params = {
        'device_type':'cisco_ios',
        'ip':DICT_OF_DEVICE[device],
        'username':username,
        'password':password
    }

    ssh = netmiko.ConnectHandler(**device_params)
    result = ssh.send_config_set(["interface "+local_int, "description "+Desc])
    print(result)
    ssh.disconnect()

def setContent(device):
    next_host = searchDataofNext(collectData(device))

    n_hostname = next_host[0]
    l_interface = next_host[1]
    n_interface = next_host[2]

    dict_of_interface = {}
    for i in range(len(l_interface)):

        if l_interface[i] in dict_of_interface:
            dict_of_interface[l_interface[i]] += "connect to "+n_interface[i]+" of "+n_hostname[i]+", "
        else:
            dict_of_interface[l_interface[i]] = ""
            dict_of_interface[l_interface[i]] += "connect to "+n_interface[i]+" of "+n_hostname[i]+", "
    for j in dict_of_interface:
        settingDesc(device, j, dict_of_interface[j])

setContent('R0')
setContent('R1')
setContent('R2')
setContent('R3')
setContent('R4')
setContent('R5')
setContent('S0')
setContent('S1')
setContent('S2')
