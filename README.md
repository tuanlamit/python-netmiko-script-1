# Save the config and export it as a back-up.

Code executed on Ubuntu 22.04 to script Cisco terminal servers (routers)

Telnet was used instead of SSH because this is a testing environment running in the company's internal network; firewall was also disabled.  Below is the topology:



You'll need to create a .txt file to store IP addresses in the same folder.

At line:
```
'device_type': 'cisco_ios_telnet'
```

This is telnet within netmiko, ssh could also be used if this line is changed to:
```
'device_type': 'cisco_ios'
```


# Outputs sync to apache</summary>

At line:
```
out_file_name = f"/var/www/shared/BLD-18/terminal_servers_backup_configs/show_running-config/sho_run-{ip}.txt"
```

You can save the back-ups to your desired destination, I prefer to use the above path because I wanted the changes to reflect on the web browser (apache2 is needed).
