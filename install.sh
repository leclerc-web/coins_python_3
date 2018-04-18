#!/bin/bash
# INSTALLATION PACKAGE 

pip install colorama
echo -ne '#####                     (50%)\r'
sleep 1

pip install simplejson
echo -ne '#############             (100%)\r'
echo -ne '\n'

clear
python coins3.py