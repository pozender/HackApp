from modules.Verif_install_noyau_ask import ask_user_choices
from modules.Install_packet import install_packages

# Obtenir les choix de l'utilisateur
os_var, kernel_var, windows_version_var = ask_user_choices()

# Installer les paquets en fonction des choix de l'utilisateur
install_packages(os_var, kernel_var, windows_version_var)
