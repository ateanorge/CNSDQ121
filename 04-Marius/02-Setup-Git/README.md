# Stage VM and setup Git

<br>
<br>
<p align="center">
<b> Endre hostname på Windows10 VM </b>  
</p>  
    
For ren hygiene, endre hostname til å samsvare VMWare-hostname
- På grunn av NETBIOS-begrensning på 15 tegn, start med initialer og legg på forkortet VM-navn bak
  -  e.g. ComSecDay21Q1-MH-WSL2-Ubuntu = MH-CSD21Q1
- Kjør PowerShell som administrator
```
Rename-Computer -NewName "[YOURINITIALS]-CSD21Q1" -LocalCredential atealab -Restart
```


Åpne WSL2/Ubuntu:

![x](/04-Marius/00-files/wsl2-ubuntu2004.png "x")  

  
<br>
<br>  

<p align="center">
<b> Legg inn Git-brukerinformasjon </b>  
</p>

E.g.:  

    git config --global user.name "mariushole"  
    git config --global user.email marius.hole@atea.no  


<p align="center">
<b> Generere personlig sertifikat </b>  
</p>  
  
Endre "YourEmail" og kjør kommando  
```
ssh-keygen -t rsa -b 4096 -C "YourEmail"
```
  
<br>  
  
![x](/04-Marius/00-files/ssh-generate.png "x")  
  
<br>
<br>

<p align="center">
<b> Sikre deg om at ssh-agent kjører </b>    
</p>  
  
Kjør kommando:  
```
eval "$(ssh-agent -s)"
```
  
<br>
  
![x](/04-Marius/00-files/ssh-run-agent.png "x")  
  
<br>
<br>

<p align="center">
<b> Legg til nøkkel til ssh-agent </b>  
</p>
  
Kjør kommando:  
```
ssh-add ~/.ssh/id_rsa
```
  
<br>
  
![x](/04-Marius/00-files/ssh-bind-key.png "x")  
  
<br>  
<br>

<p align="center">  
<b> Kopiere sertifikat </b>  
</p>
  
Åpne sertifikat-fil med VIM, ved å kjøre kommando:  
```
vim ~/.ssh/id_rsa.pub 
```  
Merk tekst og kopier til clipboard    
<br>
  
![x](/04-Marius/00-files/ssh-copy-key.png "x")  
  
Gå ut av VIM med  

    :q
  
<br>
<br>

<p align="center">
<b> Installere på GitHub </b>  
</p>
  
<b>Gå til settings:</b>  
![x](/04-Marius/00-files/github-Settings.png "x")  
<br>
<br>
<b>Gå til SSH:</b>  
![x](/04-Marius/00-files/github-ssh.png "x")  
<br>
<br>
<b>Skriv inn fornuftig navn og legg til nøkkel:</b>  
![x](/04-Marius/00-files/github-add-key.png "x")  
<br>
<br>
<b>Og bekrefte med passord (til din private github konto):</b>  
![x](/04-Marius/00-files/github-confirm-key.png "x")  
<br>
<br>
<b>Og nå skal du se nøkkel knyttet til din konto:</b>  
![x](/04-Marius/00-files/github-key-voila.png "x")  

* Ja. Du kan slette dette når som helst.  

<br>
<br>
<p align="center">
<b> Koble sertifikat til Atea </b>
</p>

<b>Velg enable SSO:</b>  
![x](/04-Marius/00-files/github-enable-sso.png "x")  
<br>
<br>
<b>Logg inn (med Atea konto):</b>  
![x](/04-Marius/00-files/github-enable-sso-sign-in.png "x")  
<br>
<br>
<b>Success:</b>  
![x](/04-Marius/00-files/github-enable-sso-success.png "x")  

* Ja. Du kan fjerne denne koblingen når som helst.

<br>
<br>
<p align="center">
<b> Clone master repo til jump </b>
</p>
  
<br>
Clone master:  

```  
git clone git@github.com:ateanorge/CNSDQ121.git  
```  

<b>Akseptere GitHub sertifikat - så laster den ned repo lokalt</b>  
![x](/04-Marius/00-files/clone-git-repo.png "x")  
<br>
  
<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021