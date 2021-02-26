# Opprette Windows 10 VM fra template via Ansible

Her går vi igjennom; 
- Hva du må gjøre om du skal installere manuelt
- Hva er de forskjellige templatene
- Hvordan du oppretter du VM fra template via Ansible

<br><br>

## Manuell installasjon?

Om du ønsker å kjøre manuell installasjon av VM, så må du huske følgende;
 - WSL1 krever ikke hardware virtualiesring
 - WSL2 krever hardware virtualisering, da må du slå på følgende i VMware;
![Spawn](/04-Marius/00-files/vm-iommu.png "Spawn")
- Dette tillatter VM'en å kjøre "nested" virtualisering (e.g. Hyper-V, Sandbox og WSL2) 
- Du kan kjøre opp en novirtWin10.yml (se under) for å teste dette selv.

<br><br>

## Ansible Templates

Lese igjennom, og vurdere hvilket template du ønsker å starte fra;

<br>

### novirtWin10.yml
Dette er et template som har ren Windows 10, uten hardware virtualisering. Kan kun kjøre WSL1.

Template i VMware heter;
```
ComSecDay21Q1-Jump-Template-WO-VT
```

For å spawn dette, kjør kommandoen;
```
ansible-playbook novirtWin10.yml
```

<br><br>

### win10.yml  
Vanilla Windows10 med hardware virtualisation lagt til for å støtte WSL2.

Template i VMware heter;
```
ComSecDay21Q1-Jump-Template
```

For å spawn dette, kjør kommandoen;
```
ansible-playbook win10.yml
```

For å installere WLS2 og Ubuntu manuelt, [følg denne guiden;](d-win10-wsl2.md)

<br><br>

### WLS2.yml  
Windows 10 med WSL2 pre-installed.  

Template i VMware heter;
```
ComSecDay21Q1-Jump-Template-WSL2
```

For å spawn dette, kjør kommandoen;
```
ansible-playbook WLS2.yml
```

<br><br>

### Ubuntu.yml  
Windows 10 med WSL2 og Ubuntu 20.04 pre-installed.  

Template i VMware heter;
```
ComSecDay21Q1-Jump-Template-WSL2-Ubuntu 
```

For å spawn dette, kjør kommandoen;
```
ansible-playbook Ubuntu.yml  
```

<br><br>

## Logg inn på "SPAWN-STATION"

|T1|E1| 
| :------------- | :----------: |
|Login (SSH)|10.203.15.140|  
|username|lab|  
|password|James Bond!|  

<br><br>

### Kjør Anisble Playbook for å opprette din lab-jumpstation

Kjør en av overnevnte Ansible Playbooks for å sette opp ønsket Windows10-miljø;

Her får du spørsmål om å fylle inn dine initialer, one-brukernavn og passord:
![Spawn](/04-Marius/00-files/ansible-playbook.png "Spawn")

<br><br><br><br>

```diff
+( Author )+
Marius Hole  
25.02.2021
```