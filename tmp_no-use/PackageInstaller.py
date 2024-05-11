import subprocess

class PackageInstaller:
    """Cette classe gère l'installation de paquets sur différentes plateformes."""

    def __init__(self):
        """Initialise une instance de PackageInstaller."""
        pass

    def install_linux(self, package_list):
        """Installe les paquets spécifiés sur un système Linux à l'aide de la commande 'apt install'.

        Args:
            package_list (list): Une liste contenant les noms des paquets à installer.
        """
        for package in package_list:
            try:
                subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
                print(f"Package {package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to install package {package}.")

    def download_windows(self, package_list):
        """Télécharge les installateurs des paquets spécifiés pour Windows.

        Args:
            package_list (dict): Un dictionnaire contenant les noms des paquets et leurs URL d'installation.
        """
        for package, url in package_list.items():
            destination = f"downloads/{package}-installer.exe"
            if self._download_file(url, destination):
                print(f"Package {package} downloaded successfully.")

    def _download_file(self, url, destination):
        """Télécharge un fichier depuis une URL donnée à l'aide de la commande 'curl'.

        Args:
            url (str): L'URL du fichier à télécharger.
            destination (str): Le chemin où enregistrer le fichier téléchargé.

        Returns:
            bool: True si le téléchargement a réussi, False sinon.
        """
        try:
            subprocess.run(["curl", "-o", destination, url], check=True)
            return True
        except subprocess.CalledProcessError:
            print(f"Failed to download file from {url}.")
            return False
    def download_macos(self, package_list):
        """
        Télécharge les installateurs des paquets spécifiés pour macOS.
        
        Args:
            package_list (dict): Un dictionnaire contenant les noms des paquets et leurs URL d'installation.
        """

        for package, url in package_list.items():
            destination = f"downloads/{package}-installer.dmg"
            if self._download_file(url, destination):
                print(f"Package {package} downloaded successfully.")

# Exemple d'utilisation
#installer = PackageInstaller()

# Liste de packages pour Linux à installer avec apt
#linux_packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "net-tools"]

# Liste de packages avec leurs URL pour Windows
#windows_packages = {
#   "aircrack-ng": "https://example.com/aircrack-ng-installer.exe",
#    "nmap": "https://example.com/nmap-installer.exe",
    # Ajoutez d'autres paquets avec leur nom et URL d'installateur pour Windows
#}

# Installation des packages pour chaque système d'exploitation
#installer.install_linux(linux_packages)
#installer.download_windows(windows_packages)
