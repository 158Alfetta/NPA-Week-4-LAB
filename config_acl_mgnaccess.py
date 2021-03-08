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

def config_acl_mgnaccess(device_params, interface):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = [
        "ip access-list extended noaccessMGN",
        "10 deny ip any 172.31.177.0 0.0.0.15",
        "20 permit ip any any",
        "interface "+interface,
        "ip access-group noaccessMGN in"
    ]
    result = ssh.send_config_set(commands)
    print(result)
    ssh.disconnect()

def setContent(device, interface):
    
    config_acl_mgnaccess({
            'device_type':'cisco_ios',
            'ip':DICT_OF_DEVICE[device],
            'username':username,
            'password':password
        }, interface)


# attach to every interface that is a surface of dataplane
setContent('R1', 'g0/1')
setContent('R1', 'g0/2')

setContent('R2', 'g0/1')
setContent('R2', 'g0/2')

setContent('R3', 'g0/1')
setContent('R3', 'g0/2')
setContent('R3', 'g0/3')

setContent('R4', 'g0/1')

setContent('R5', 'g0/1')