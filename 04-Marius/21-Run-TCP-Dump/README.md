# Run tcpdump with Anisble

## Run ping.yml
Run a continous ping from a screen window (in the backgroun)
```
sudo ansible-playbook ping.yml
```
## Run the tcpdump.yml
Run the tcpdump.yml to make a packet dump of the running between the two hosts
```
ansible-playbook tcpdump.yml
```
- the two hosts being the ICMP-source host (WSL2) and the ICMP-destination host 
- the ping running in the background in a screen... 

<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021