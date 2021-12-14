#!/bin/bash
sudo apt update -y && sudo apt upgrade -y && sudo apt install gcc python3-dev && pip3 install psutil && sudo apt autoremove -y && cp /home/$USER/raspberry-info-system/RPi_info_system.1.0.desktop /home/$USER/Desktop/RPi_info_system.1.0.desktop && chmod +x /home/$USER/Desktop/RPi_info_system.1.0.desktop  
