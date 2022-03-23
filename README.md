# Setup Laptop with Ansible

## Steps

### (_Assumes starting from home dir in Fedora 35_)

1. Clone this repo  
   `git clone --recursive https://github.com/godsmith99x/env_setup.git`
1. Execute bootstrap script  
   `~/env_setup/bootstrap.py`
1. Save ssh public key to github
1. Change remote url to ssh vice https  
   `cd env_setup/ && git remote set-url origin git@github.com:godsmith99x/env_setup.git`  
1. Run asible-playbook to configure the localhost  
   `sudo ansible-playbook ~/env_setup/local.yml`
