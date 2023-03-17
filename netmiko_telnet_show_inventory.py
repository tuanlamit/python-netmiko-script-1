from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()


def backup(device, ip):
    connection = ConnectHandler(**device)

    send_sho_run = connection.send_command('sho inv')
    out_file_name = f"/var/www/shared/back-up-configs/TS-18/show_inventory/sho_inv-{ip}.txt"
    out_file = open(out_file_name, "w")
    out_file.write(send_sho_run)
    out_file.close()
    connection.disconnect()
    print(f'Done with {ip}')


with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()

for ip in devices:
    device = {
        'device_type': 'cisco_ios_telnet',
        'host': ip,
        'username': 'lab',
        'password': 'lab',
        'secret': 'cisco',
        'verbose': True,
    }
    th = threading.Thread(target=backup, args=(device, ip))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print(f'Total Execution Time: {end-start}')

















