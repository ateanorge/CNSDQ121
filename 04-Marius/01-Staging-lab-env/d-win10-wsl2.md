# Enable WSL2 and install Linux distro

Følg guide: https://docs.microsoft.com/en-us/windows/wsl/install-win10

## Enable Virtual Machine feature
I PowerShell;
```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

## Download the Linux kernel update package
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

## Set WSL 2 as your default version
I PowerShell;
```
wsl --set-default-version 2
```

## Install your Linux distribution of choice
1. Fra windows store 
2. Deretter "create a user account and password for your new Linux distribution"

<br><br><br><br>

```diff
+( Author )+
Marius Hole  
25.02.2021
```