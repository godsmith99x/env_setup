# Setup Server with Ansible

## Steps

### (_Assumes starting from home dir in Ubuntu 20.04_)

1. Clone this repo  
   `git clone https://github.com/godsmith99x/env_setup.git`
1. Change into env_setup dir
   `cd env_setup`
1. Checkout the Ubuntu Sever branch
   `git checkout ubuntu_server`
1. Execute bootstrap script  
   `~/env_setup/bootstrap.py`
1. Run asible-playbook to configure the localhost  
   `sudo ansible-playbook ~/env_setup/local.yml`
