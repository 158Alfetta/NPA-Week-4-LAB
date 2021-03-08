import netmiko
import threading

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

def config_ospf(device_params, network, wildcard, area):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = [
        "router ospf 1",
        "network "+network+" "+wildcard+" area "+area
    ]
    result = ssh.send_config_set(commands)
    print(result)
    ssh.disconnect()

def setContent(device, network, wildcard, area):
    
    config_ospf({
            'device_type':'cisco_ios',
            'ip':DICT_OF_DEVICE[device],
            'username':username,
            'password':password
        }, network, wildcard, area)

def passiveInt(device_params, interface):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = [
        "router ospf 1",
        "passive-interface "+interface
    ]
    result = ssh.send_config_set(commands)
    print(result)
    ssh.disconnect()

def setContent2(device, interface):
    
    passiveInt({
            'device_type':'cisco_ios',
            'ip':DICT_OF_DEVICE[device],
            'username':username,
            'password':password
        }, interface)


# add network of ospf process id 1 
# use in order --> setContent('HOSTNAME', 'NETWORK', 'WILDCARD', 'AREA')
setContent('R1', '172.31.177.16', '0.0.0.15', '0')
setContent('R1', '172.31.177.32', '0.0.0.15', '0')

setContent('R2', '172.31.177.16', '0.0.0.15', '0')
setContent('R2', '172.31.177.48', '0.0.0.15', '0')

setContent('R3', '172.31.177.32', '0.0.0.15', '0')
setContent('R3', '172.31.177.48', '0.0.0.15', '0')
setContent('R3', '172.31.177.64', '0.0.0.15', '0')

setContent('R4', '172.31.177.48', '0.0.0.15', '0')
setContent('R4', '172.31.177.64', '0.0.0.15', '0')

setContent('R5', '172.31.177.64', '0.0.0.15', '0')


setContent('R5', '172.31.177.64', '0.0.0.15', '0')

setContent('R0', '172.20.177.1', '0.0.0.0', '0')
setContent('R1', '172.20.177.4', '0.0.0.0', '0')
setContent('R2', '172.20.177.5', '0.0.0.0', '0')
setContent('R3', '172.20.177.6', '0.0.0.0', '0')
setContent('R4', '172.20.177.7', '0.0.0.0', '0')
setContent('R5', '172.20.177.9', '0.0.0.0', '0')


#set passive interface 
# use in order --> setContent2('HOSTNAME', 'INTERFACE')


setContent2('R1', 'g0/0')
setContent2('R2', 'g0/0')
setContent2('R3', 'g0/0')
setContent2('R4', 'g0/0')
setContent2('R5', 'g0/0')