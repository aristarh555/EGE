#17
from ipaddress import ip_network

for mask in range(32, 0, -1):
    net = ip_network(f'143.131.211.37/{mask}', False)
    count = 0
    for ip in net:
        if f'{ip:b}'.count('1') == 10:
            count += 1
    if count == 15:
        print(mask)




