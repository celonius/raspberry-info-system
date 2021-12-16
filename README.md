# raspberry-info-system
Informations sur le status des composants de la Raspberry Pi.

#### Informations:
- Temperature processeur
- Utilisation processeur
- Frequence processeur
- Memoire ram disponible
- Memoire SD disponible

Developer sous [Python3](https://www.python.org/) avec les modules [Psutil](https://psutil.readthedocs.io/en/latest/), [Gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html).

#### Installation:
Copiez-coller les commandes suivantes dans votre shell favorit:

> git clone https://github.com/celonius/raspberry-info-system.git 

> cd RPI_info_system 

> bash install.sh  

Le script install.sh met a jour votre RPi et verifie que que vous possedez tout ce au'il faut pour l'execution du programme.
A la fin de l'installation, un raccourci pour lancer l'application apparaitra sur votre bureau.

Si en cliquant sur executer rien ne se passe, faites un clic droit sur le raccourci > Text editor > remplacer le mot **pi** de la ligne Exec=python3  /home/**pi**/raspberry-info-system/RPi_info_system.1.0.py par votre nom d'utilisateur

#### Fenetre:
La fenetre du programme se place automatiquement en dessus a droite de votre ecran. 
Pour le moment les resolution supportees sont:
- 1920x1080
- 1440x900
- 1240x1024
- 800x600
- 640x480

##### Prochaine mise a jour:
- Option de placement de la fenetre
- Option d'overclocking du CPU
- Graphiques des diffentes donnees
- ... 

