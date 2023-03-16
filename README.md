# python-netmiko-script-1
This script netmiko_telnet_wr+sho_run.py was created to telnet to Cisco routers, do "wr" and "sho run" then save outputs locally.

The reason telnet was used was because this script was executed within a lab environment with no access to the outside internet.

Multi-threading was used to reduce execution time.

You would need another file called "devices.txt" in the same folder as the script to hold the IP addresses.

At line 29, where it says:
> 'device_type': 'cisco_ios_telnet'

This is telnet within netmiko, you could also use SSH if you change this line to:
> 'device_type': 'cisco_ios_'
