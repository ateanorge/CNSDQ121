# WSL2 and Visual Studio Code with a hint of bash  

Hva er Windows Subsystem for Linux? Hva er Visual Studio Code? Er dette relevant for deg? Håper du finner svaret i løpet av denne sesjonen :)

[Link to video recodring](https://northeuroper-notifyp.svc.ms/api/v2/tracking/method/Click?mi=3V1i5JcN-kGV565z1t_vPQ&tc=StreamVideo&cs=9ae60979bf4dcbf00b27849f919a2918&ru=https%3a%2f%2fweb.microsoftstream.com%2fvideo%2f53b338ba-415b-4a55-b342-4d4f03a8d70a) 

## Agenda 
```diff
-! Lab enviroment !-
```
#### 01-Staging-lab-env
- Koble til AteaLab med Cisco AnyConnect
- Kjøre opp en Windows 10 sandbox fra VMware-template
- Logge inn i VMware vCenter for å sjekke IP, og koble på RDP
- Installere WSL2 og Ubuntu manuelt

#### 02-Setup-Git
- Konfigurere git på WLS-Ubuntu
- Sette opp kobling mot GitHub med sertifikat (ssh)
- Hente ned et repository fra GitHub til datamaskinen

#### 03-VisualStudioCode
- Installere Visual Studio Code
- Sette opp extension for integrasjon mot WSL
- Bruk av VSC, Git og bash

#### 04-Install-Ansible
- Installere Ansible på WSL-Ubuntu

#### 05-Install-apps
- Installere apps via Ansible Playbooks

```diff
-! Tuning (hacking?) WSL2 enviroment !-
```
#### 10-Genie
- Få tilang til systemresurser for å gjøre systemendringer i WSL-Ubuntu
#### 11-Bridge-WSL-NIC-with-Host-NIC
- Sette WSL-Ubuntu nic (eth0) til å være på LAN'et (bridge LAN/WLAN NIC)

```diff
-! Some tools and demonstrations !-
```
#### 20-Run-Iperf
- Kjøre iperf3 klient på WSL-Ubuntu
- Kjøre iperf3 server på WSL-Ubuntu (med Genie)
#### 21-Run-TCP-Dump
- Kjøre TCP-dump i WSL-Ubuntu
#### 22-Setup-FTP-Server
- Sette opp FTP-server på WSL-Ubuntu

```diff
-! Tips and tricks !-
```
#### 99-General-tips
- Noen generelle tips

## Dette var en til kommentar

Bra å bruke VSC med WSL

<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021
