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

def Config_ACL_SSH(device_params):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = [
        "ip access-list standard noSSH",
        "10 permit 10.253.190.0 0.0.0.255",
        "20 permit 172.31.177.0 0.0.0.15",
        "line vty 0 15",
        "transport input telnet ssh",
        "access noSSH in"
    ]
    result = ssh.send_config_set(commands)
    print(result)
    ssh.disconnect()

def main():
    
    threads = []
    
    for i in DICT_OF_DEVICE:
        thread_arg = [{
                'device_type':'cisco_ios',
                'ip':DICT_OF_DEVICE[i],
                'username':username,
                'password':password
            }]
        threads.append(threading.Thread(target=Config_ACL_SSH, args=thread_arg))

    for t in threads:
        t.start()

main()