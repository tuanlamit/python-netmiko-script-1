# Save the config locally

Code executed on Ubuntu 22.04 to script approximately 100 Cisco terminal servers (routers).

As team requested, telnet was used to script the routers in the lab. Below is the topology:

![image](https://user-images.githubusercontent.com/128099142/233894228-dbb6538b-ac53-4065-860b-3afb16e1979c.png)

This line in the netmiko_telnet_wr+sho_run.py specifies telnet usage
```
'device_type': 'cisco_ios_telnet'
```

Modify value to 'cisco_ios' if you prefer to use SSH
```
'device_type': 'cisco_ios'
```

# Example 1: Workspace

![example1](https://github.com/tuanlamit/python-netmiko-script-1/assets/128099142/12835855-ea8f-4c3c-af51-78d39e86f6d9)

# Example 2: Result

![example2](https://github.com/tuanlamit/python-netmiko-script-1/assets/128099142/e3b27d2b-6e83-4ba1-80d1-a5d590c786d2)

