from netmiko import ConnectHandler
from datetime import datetime
import time
import threading
start = time.time()


def backup(device, ip, successful_backups):
    try:
        connection = ConnectHandler(**device)
        send_sho_run = connection.send_command('sho ip int br')
        out_file_name = f"/var/www/shared/BLD-18/terminal_servers_backup_configs/show_ip_interface_brief/sho_ip_int_br-{ip}.txt"
        out_file = open(out_file_name, "w")
        out_file.write(send_sho_run)
        out_file.close()
        connection.disconnect()
        print(f'Done with {ip}')
        successful_backups.append(ip)
    except Exception as e:
        print(f'Backing-up for {ip} failed.')


with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()
successful_backups = []
scripted_devices = 0

for ip in devices:
    device = {
        'device_type': 'cisco_ios_telnet',
        'host': ip,
        'username': 'lab',
        'password': 'lab',
        'secret': 'cisco',
        'verbose': True,
    }
    th = threading.Thread(target=backup, args=(device, ip, successful_backups))
    threads.append(th)
    th.start()
    scripted_devices += 1

for th in threads:
    th.join()

end = time.time()
print(f'Total Devices Successfully Backed Up: {len(successful_backups)}')
print(f'Total Execution Time: {end - start}')

