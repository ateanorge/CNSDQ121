# Install Docker and run a Docker container with WSL

- Before you begin, you should make sure the VM has enough CPU and RAM (suggestion; 4xCPU and 8GB RAM)

Follow this guide: https://docs.docker.com/docker-for-windows/wsl/

## Download and install Docker desktop

https://hub.docker.com/editions/community/docker-ce-desktop-windows/

![x](/04-Marius/00-files/docker-wsl2-01.png "x")
- During installation, enable integration with WSL


## After installation, enable the WSL distro

- Find this menu;
![x](/04-Marius/00-files/docker-wsl2-02.png "x")  

- In settings, enable the WSL distro -> Apply and Restart
![x](/04-Marius/00-files/docker-wsl2-03.png "x")
- Restart computer...

## Linuxserver SmokePing Docker image at Docker hub

We use Linuxservers SmokePing Docker Image;
https://hub.docker.com/r/linuxserver/smokeping
- Which is the most popular SmokePing image on Docker Hub  

```diff
+ You don't need to pull the image manually if you add it to the bash run command (further down in this section) 
```

- Wait until Docker is started...  
- Pull with the following bash command  

```
docker pull linuxserver/smokeping
```

## Prepare run variables 

- Create data and config folder
```
cd ~
mkdir smokeping
cd smokeping
mkdir data
mkdir config
```

## Run SmokePing with run command

- Start SmokePing Docker container with the following run command and variables
```
docker run -d \
  --name=smokeping \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Oslo \
  -p 80:80 \
  -v /home/atealab/smokeping/config:/config \
  -v /home/atealab/smokeping/data:/data \
  --restart unless-stopped \
  ghcr.io/linuxserver/smokeping
```


## Verify in browser (with default config)

- Check the IP address for the Ubuntu WSL from bash (eth0)
```
ip a
```
- Open browser and open the Ubuntu IP-adress

## Stop the image

- Now stop the Docker-image
![x](/04-Marius/00-files/docker-wsl2-04.png "x")



## Delete data files

- Delete the data, before changing the config
```
cd /home/atealab/smokeping/data
rm -f -r *
```

## Edit config files (Probes)

- Configure fping probe intervals
```
nano /home/atealab/smokeping/config/Probes
```
- Add the following under the FPing probes (under binary)
```
 hostinterval = 1.5
 pings = 15
 step = 30
```

## Start container again
- Start the container again (same place as stopping it)

## Verify in browser (with new config)
- Open browser, browse to the Ubuntu-WSL IP

<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021
