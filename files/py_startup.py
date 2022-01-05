#    ___             _                  _  _    _                               
#   / _ \  ___    __| | ___  _ __ ___  (_)| |_ | |__                            
#  / /_\/ / _ \  / _` |/ __|| '_ ` _ \ | || __|| '_ \                           
# / /_\\ | (_) || (_| |\__ \| | | | | || || |_ | | | |                          
# \____/  \___/  \__,_||___/|_| |_| |_||_| \__||_| |_|                          
#    

# this file will load on python startup if the PYTHONSTARTUP 
# environment variable is set to point to it. You can add this 
# "export"  to the end of your .bashrc or .zshrc file for example.
# export PYTHONSTARTUP=~/environment_setup/files/py_startup.py
# add tab completion
try:
    import readline
except ImportError:
    print ("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")

# append current dir to path
# import sys, os
# sys.path.append(os.getenv("PWD"))

# make rich repl
try:
    from rich import pretty
except ImportError:
    print ("Module readline not available.")
else:
    from rich import pretty
    pretty.install()
