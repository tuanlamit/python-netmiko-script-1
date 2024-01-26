# import configparser to use the config file
from configparser import ConfigParser

# import the ConnectHandler class from the netmiko library to establish SSH connection and send commands
from netmiko import ConnectHandler

# import these modules to record and speed up execution time and to parse the json file
import time, threading, json

# mark starting time at the beginning of the script
start = time.time()

# create a config object and store it in the variable 'config'
config = ConfigParser()

# read from the config file
config.read('config.ini')

# create variables to reference the config file and the json file
command1 = config.get('commands', 'wr')
command2 = config.get('commands', 'sho run')
html_path = config.get('paths', 'html_path')
json_path = config.get('paths', 'json_path')

# open the devices.json file to use the terminal servers' IP addresses and credentials
with open(json_path + 'devices.json') as json_file:
    devices = json.load(json_file)

# define a function to save configs locally
def backup(device_info, successful_backups):
    try:
        # access the device via SSH and pass it to the variable 'connection'
        connection = ConnectHandler(**device_info)

        # first save the config
        connection.send_command(command1)
        
        # then obtain outputs from command2 and store it in the variable 'output'
        output = connection.send_command(command2)

        # write the output into a .txt file and save it into the html directory
        # directory is referenced to the config file using variable 'path'
        with open(html_path + "sho_run-{}.txt".format(device_info['host']), "w") as out_file:
            out_file.write(output)

        # close the SSH connection
        connection.disconnect()
        print('Done with {}'.format(device_info['host']))

        # store the IP address of a completed backup to a variable
        # we'll use the built-in len() function to count the number of completed backup after
        successful_backups.append(device_info['host'])

    # continue running the script even if there's an error
    except Exception as e:
        print('Backing-up for {} failed.'.format(device_info['host']))
        print('~~~~~', e, '~~~~~')

# create an empty list named threads
threads = list()

# create an empty list named successful_backups
successful_backups = []

# create a variable to count devices that will be scripted, starting from 0
scripted_devices = 0

# write a for loop to loop over each device with IP address and credential
for device_info in devices:
    
    # link the backup function to the Thread class and assign a variable 'th'
    # this does not run our backup function yet, we'll need to invoke it with th.start() later
    th = threading.Thread(target=backup, args=(device_info, successful_backups))
    
    # append the linking to variable 'threads'
    threads.append(th)

    # start the main thread, it will then call the backup function
    th.start()

    # number of each device that was scripted is incremented by 1 every loop
    scripted_devices += 1

# the join() method finishes all the threads before executing the remaining codes
for th in threads:
    th.join()

# mark ending time of the entire script
end = time.time()

print('Total Devices Scripted: {}'.format(scripted_devices))
print('Total Devices Successfully Backed Up: {}'.format(len(successful_backups)))
print('Total Execution Time: {}s'.format(round(end - start, 2)))


