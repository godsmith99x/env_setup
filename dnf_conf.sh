#!/usr/bin/bash                                                                 
#    ___             _                  _  _    _                               
#   / _ \  ___    __| | ___  _ __ ___  (_)| |_ | |__                            
#  / /_\/ / _ \  / _` |/ __|| '_ ` _ \ | || __|| '_ \                           
# / /_\\ | (_) || (_| |\__ \| | | | | || || |_ | | | |                          
# \____/  \___/  \__,_||___/|_| |_| |_||_| \__||_| |_|                          
#      

echo 'fastestmirror=1' | sudo tee -a /etc/dnf/dnf.conf
echo 'max_parallel_downloads=10' | sudo tee -a /etc/dnf/dnf.conf
echo 'deltarpm=true' | sudo tee -a /etc/dnf/dnf.conf
