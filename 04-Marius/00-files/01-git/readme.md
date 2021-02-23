<p align="center">
<b> Logge inn på Jumpstation </b>  
</p>  

Logge inn på Jumpstation med root:  

|T1|E1|  
| :------------- | :----------: |  
|username|root|  
|password|Labetuss1|    

* Vi er klar over at root ikke er best practice, dette er en lab: bruk unike brukere og sudo i prod!

<br>
<br>
<p align="center">
<b> Endre hostname på jump </b>  
</p>  
    
For ren hygiene, endre hostname til å samsvare VMWare-hostname (e.g. TC19-3001-jump) på jumpstation:  
```
echo "TC19-[LABNUMBER]-jump" > /etc/hostname
```
  
<br>  
  
Og reboot for at det skal tre i kraft:  
```
reboot
```
  
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
  
Først gå til mappen /tc19/git/:  

```  
cd /tc19/git  
```  

<br>
Deretter clone master:  

```  
git clone git@github.com:ateanorge/tc19-spor6.git  
```  

<b>Akseptere GitHub sertifikat</b>  
![x](/04-Marius/00-files/git-clone-accept-github-cert.png "x")  
<br>

<b>Success:</b>  
![x](/04-Marius/00-files/git-clone-voila.png "x")  

<br>
  
[Tilbake til neste steg i 02-guides](../../02-guides/readme.md#03---intro-til-ansible)

