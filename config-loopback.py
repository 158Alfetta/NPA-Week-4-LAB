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

IP_ADDR = {
    "R0":"172.20.177.1",
    "R1":"172.20.177.4",
    "R2":"172.20.177.5",
    "R3":"172.20.177.6",
    "R4":"172.20.177.7",
    "R5":"172.20.177.9",
    "S0":"172.20.177.2",
    "S1":"172.20.177.3",
    "S2":"172.20.177.8"
}


username = "admin"
password = "cisco"

def ConfigLoopback(device_params, ip_address):
    ssh = netmiko.ConnectHandler(**device_params)
    commands = ['interface lo0', 'ip address '+ip_address+' 255.255.255.255']
    ssh.send_config_set(commands)
    result = ssh.send_command('show ip int br')
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
            }, IP_ADDR[i]]
        threads.append(threading.Thread(target=ConfigLoopback, args=thread_arg))

    for t in threads:
        t.start()

main()