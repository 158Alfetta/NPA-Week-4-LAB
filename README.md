# Network Programability 
### _Presented by UDOMEAK CHUMTHONGMA 60070120_

Link Youtube: www.youtube.com/watch?v=2OfNUqU-VZs
(์NOTE: ใน Video ผมลืมเทส ping ไปยัง www.google.com ครับ แต่สามารถทำได้ครับ)

## Files Description
| Name | Description |
| ------ | ------ |
| all_around_save.py | use this files to write memory on current configuration (Implement with threading SPEED++!) |
| config_loopback.py | config IP of all loopback interface to all devices in network (Requirement #1) |
| config_datap_inf.py | config IP of all data plane/control plane interface in network (Requirement #2) |
| config_acl_mgnaccess.py | config access list to filter traffic from Data Plane to Management Network (Requirement #4) |
| config_acl_ssh.py | config devices to allow telnet/ssh trafic initiate from specific network  (Requirement #5) |
| config_ospf.py | config ospf in dataplane network (Requirement #6) |
| config_remarkInt_byCDP.py | config interface desc. by using the data from CDP (Requirement #8) |
| config_NAT.py | config NAT (inside, outside, ACL, NAT) (Requirement #9) |