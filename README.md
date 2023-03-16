# python-netmiko-script-1
This script netmiko_telnet_wr+sho_run.py does telnet to Cisco routers, does "wr" and "sho run", then saves the outputs locally.

Reason for using telnet is because this script was executed within a lab environment with no access to the outside internet.

Multi-threading was used to reduce execution time.

You would need another file "devices.txt" in the same folder as the script to hold the IP addresses.

At line 29, where it says:
> 'device_type': 'cisco_ios_telnet'

This is telnet within netmiko, you could also use SSH if you change this line to:
> 'device_type': 'cisco_ios_'

After running the code, total execution time will be displayed at the bottom.

![image](https://user-images.githubusercontent.com/128099142/225773439-63a78f4c-8dca-45d3-a7e4-c4bc038be72a.png)

IP addresses are covered up because the script was executed from the company's internal network.

Execution speed depends on a lot of factors, such as system hardware resouces, number of commands to run, etc...

In this case, 27 routers were scripted and total time took was 13 seconds displayed in the screenshot above.
