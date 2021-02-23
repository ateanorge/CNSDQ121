# Bridge WSL2 with Network-adapter

This guide will walk you through two options of exposing WSL network externally beyond the local enviroment.   

Before bridging the network adapter - assess the need. Do you need full bridge? Or are exposed ports enough?  

Be aware that this is WSL2 specific, and WSL1 operates with the same IP-stack as the comptuter. 

# Option 1; Run Windows Proxy/NAT to expose ports

Follow this guide: https://docs.microsoft.com/en-us/windows/wsl/compare-versions#accessing-a-wsl-2-distribution-from-your-local-area-network-lan

In essence; 

```  
netsh interface portproxy add v4tov4 listenport=4000 listenaddress=0.0.0.0 connectport=4000 connectaddress=192.168.101.100
```  


# Option 2; Bridge WSL eth0 with a physical adapter on the computer

### This is what the Hyper-V Virtual Switch looks like before doing any changes to it...
![x](/04-Marius/00-files/hyper-v-wsl-vswitch-normal.png "x")  

## Configure Hyper-V Virtual Switch from PowerShell
```  
set-vmswitch -name wsl -NetAdapterName Ethernet
```  
- Replace "Ethernet" with the name of the network adapter you want to bridge with

### This is what the Hyper-V Virtual Switch looks like before doing any changes to it...
![x](/04-Marius/00-files/hyper-v-wsl-vswitch-bridge.png "x")  

## Start WSL2 with Genie from CMD

```  
wsl genie -v -s
```  
-v = verbose  
-s = shell  

## Configure Network in WSL2
```  
sudo nano /etc/systemd/network/wired.network
```  
### And then add this
```  
[Match]

Name=eth0



[Network]

Description=Virtual switch

DHCP=yes

IPv6AcceptRA=true

MulticastDNS=true

LLDP=true

EmitLLDP=true



[DHCP]

CriticalConnection=true

RouteMetric=10

UseDomains=true
```  
- Save and close

## Shutdown WSL from CMD
```  
wsl --shutdown
```  

## Start WSL from CMD
```  
wsl genie -v -s
```  
-v = verbose  
-s = shell  

## Verify bridged IP
![x](/04-Marius/00-files/verify-ubuntu-bridge-ip.png "x")  


<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021