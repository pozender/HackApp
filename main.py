from modules.Verif_install_noyau_ask import * 
from modules.Install_packet import install_packages

# Installer les paquets en fonction des choix de l'utilisateur
install_packages(os_var, kernel_var, windows_version_var)
