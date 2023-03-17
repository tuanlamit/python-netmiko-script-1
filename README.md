# Part 1) netmiko_telnet_wr+sho_run.py

**"Notes: other scripts in this repo provides similar approach, just different commands and outputs."**

Everything mentioned in this repo is running on Ubuntu 22.04.

The **netmiko_telnet_wr+sho_run.py** script uses telnet to access Cisco routers, sends "wr" and "sho run", and saves the outputs locally.

Reason for using telnet is because the script was executed from the company's internal lab with no access to the outside internet.

Multi-threading was used to reduce execution time.

Another file named "devices.txt" is needed in the same folder as the script to hold the IP addresses.

At line 29 in the script:
```
'device_type': 'cisco_ios_telnet'
```

This is telnet within netmiko, ssh could also be used if this line is changed to:
```
'device_type': 'cisco_ios'
```

After running the code, total execution time will be displayed at the bottom.

![image](https://user-images.githubusercontent.com/128099142/225773439-63a78f4c-8dca-45d3-a7e4-c4bc038be72a.png)

Execution speed depends on many factors, such as system hardware resouces, number of commands to run, etc...

In this case, 27 routers were scripted and the total time took was 13 seconds displayed in the screenshot above.

# Part 2) (optional) outputs saved locally</summary>

At line 14:
```
out_file_name = f"/var/www/shared/back-up-configs/TS-18/show_running-config/wr+sho_run-{ip}.txt"
```

Outputs could be retrieved here (or any preferred directory).

However, to have those outputs automatically uploaded to a web server (with directory view) on the same Ubuntu system, install apache2:

1) install apache2:
```
sudo apt update
sudo apt install apache2
```

2) modify apache2's default config file to:
```
sudo nano /etc/apache2/sites-available/000-default.conf
```

```
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/shared

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
Alias /shared /var/www/shared
<Directory /var/www/shared>
    Options Indexes FollowSymLinks MultiViews
    AllowOverride All
    Order allow,deny
    allow from all
    Require all granted
</Directory>
```

3)  restart apache2 service and verify that apache2 is active:
```
sudo systemctl restart apache2
sudo systemctl status apache2
```

4) the outputs are now accessible via http://x.x.x.x (input local system's IP address)

Below is an example of the outputs that were uploaded to the web server displayed via directory view.

![image](https://user-images.githubusercontent.com/128099142/225777290-702eb9a0-6fa1-4ca3-8d18-41284e59ac21.png)
