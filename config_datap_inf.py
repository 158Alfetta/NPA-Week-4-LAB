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

def ConfigLoopback(device_params, interface, ip_address):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = ['interface '+interface, 'ip address '+ip_address+' 255.255.255.240', 'no shut']
    ssh.send_config_set(commands)
    result = ssh.send_command('show ip int br')
    print(result)
    ssh.disconnect()

def setContent(device, interface, ip_address):
    
    ConfigLoopback({
    'device_type':'cisco_ios',
    'ip':DICT_OF_DEVICE[device],
    'username':username,
    'password':password
    }, interface, ip_address)

setContent('R1', 'g0/1', '172.31.177.17')
setContent('R1', 'g0/2', '172.31.177.33')

setContent('R2', 'g0/1', '172.31.177.18')
setContent('R2', 'g0/2', '172.31.177.49')

setContent('R3', 'g0/1', '172.31.177.34')
setContent('R3', 'g0/2', '172.31.177.50')
setContent('R3', 'g0/3', '172.31.177.66')

setContent('R4', 'g0/1', '172.31.177.67')

setContent('R5', 'g0/1', '172.31.177.65')