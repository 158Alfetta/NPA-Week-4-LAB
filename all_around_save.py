import netmiko
import threading

# Management Plane content
dict_of_device = {
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

def save(device_params):
    ssh = netmiko.ConnectHandler(**device_params)
    result = ssh.send_command('wr', expect_string=r"#")
    print(result)
    print("saved config in IP: "+device_params['ip'])
    ssh.disconnect()

def main():
    threads = []
    
    for i in dict_of_device:
        thread_arg = [{
                'device_type':'cisco_ios',
                'ip':dict_of_device[i],
                'username':username,
                'password':password
            }]
        threads.append(threading.Thread(target=save, args=thread_arg))

    for t in threads:
        t.start()
main()