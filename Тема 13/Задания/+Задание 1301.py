# Решение
from ipaddress import ip_network

count = 0
for mask in range(32, 0, -1):
    net1 = ip_network(f'157.220.185.237/{mask}', False)
    net2 = ip_network(f'157.220.184.230/{mask}', False)
    if net1.network_address == net2.network_address:
        for ip in net1:
            print(bin(int(ip)), f'{ip:b}')
            if f'{ip:b}'.count('1') == 15:
                count += 1
        break

print(count)

answer = 9

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(13, 1301, answer, '45c48cce2e2d7fbdea1afc51c7c6ad26'))