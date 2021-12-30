#!/usr/bin/bash
#    ___             _                  _  _    _                               
#   / _ \  ___    __| | ___  _ __ ___  (_)| |_ | |__                            
#  / /_\/ / _ \  / _` |/ __|| '_ ` _ \ | || __|| '_ \                           
# / /_\\ | (_) || (_| |\__ \| | | | | || || |_ | | | |                          
# \____/  \___/  \__,_||___/|_| |_| |_||_| \__||_| |_|                          
#

# Swap capslock and esc keys
gsettings set org.gnome.desktop.input-sources xkb-options "['caps:swapescape']"

#Turn off gnome animations
gsettings set org.gnome.desktop.interface enable-animations false

#Set desktop font
gsettings set org.gnome.desktop.interface font-name 'VictorMono Nerd Font Medium 13'

#Set document font
gsettings set org.gnome.desktop.interface document-font-name 'VictorMono Nerd Font Medium 13'

#Set monospace font
gsettings set org.gnome.desktop.interface monospace-font-name 'VictorMono Nerd Font Mono Medium 13'

#Set title bar font
gsettings set org.gnome.desktop.wm.preferences titlebar-font 'VictorMono Nerd Font Medium 11'

#Set gnome-terminal font
gsettings set org.gnome.Terminal.Legacy.Profile:/:b1dcc9dd-5262-4d8d-a863-c897e6d979b9/ font 'VictorMono Nerd Font Mono Medium 15'

