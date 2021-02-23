# Configure FTP server

## Run as root
```
sudo su
```
## Configure FTP server
```
ansible-playbook proftpd-config.yml
```
## Copy file from root directory with FTP client 
```
wget ftp://atealab:labetuss@10.203.15.152/VSC.exe
```
- atealab:labetuss is username:password on the FTP-server

<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021