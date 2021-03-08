from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.177.4',
    'username': 'admin',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()

config_commands = ['int loop 2', 'no ip address 1.1.1.1 255.255.255.255', 'int loop 3', 'no ip address 2.2.2.2 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command('show ip int brief')
print(output)

