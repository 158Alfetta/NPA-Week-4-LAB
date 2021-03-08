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

def implement_cmd(device, commands):

    device_params = {
    'device_type':'cisco_ios',
    'ip':DICT_OF_DEVICE[device],
    'username':username,
    'password':password
    }

    ssh = netmiko.ConnectHandler(**device_params)
    commands = commands
    result = ssh.send_config_set(commands)
    print(result)
    ssh.disconnect()

def activateInside(device, inInt):
    implement_cmd(device, ["interface "+inInt,"ip nat inside"])

def activateOutside(device, outInt):
    implement_cmd(device, ["interface "+outInt, "ip nat outside"])

def createACL(device, name, network, wildcard):
    implement_cmd(device, ["ip access-list standard "+name, "10 permit "+network+" "+wildcard])

def createIPNAT(device, name, interface):
    implement_cmd(device, ["ip nat inside source list "+name+" interface "+interface+" overload"])

activateInside("R5", "g0/1")
activateOutside("R5", "g0/2")
createACL("R5", "TRINITY", "172.31.177.0", "0.0.0.255")
createIPNAT("R5", "TRINITY", "g0/2")