# Save the config locally

Code executed on Ubuntu 22.04 to script approximately 100 Cisco terminal servers (routers).

As team requested, telnet was used to script the routers in the lab.

Below is the topology:

![image](https://user-images.githubusercontent.com/128099142/233894228-dbb6538b-ac53-4065-860b-3afb16e1979c.png)

This line in the code specifies telnet usage
```
'device_type': 'cisco_ios_telnet'
```

Change value to 'cisco_ios' if you prefer to use SSH
```
'device_type': 'cisco_ios'
```


# Storing outputs

At line:
```
out_file_name = f"/var/www/shared/BUILDING-ABC/terminal_servers_backup_configs/show_running-config/sho_run-{ip}.txt"
```

You can save the back-ups to your desired destination, I prefer to use the above path because I wanted the changes to reflect on the web browser (apache2 is needed).
