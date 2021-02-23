# Install Ansible and upgrade system

First install Ansible;
```
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

Then upgrade the system;
```
sudo ansible-playbook ubuntu-services.yml
```

To remove cowsay from Ansible output:
```
export ANSIBLE_NOCOWS=1
```

  
<br><br><br><br>

```diff
+( Author )+
```
Marius Hole  
25.02.2021