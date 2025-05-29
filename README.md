# Extension PlayStation 1 avec Raspberry Pi Zero 2 W

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![KiCad](https://img.shields.io/badge/KiCad-7.0+-blue.svg)](https://kicad.org/)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red.svg)](https://www.raspberrypi.org/)

> Interface matérielle pour connecter un Raspberry Pi Zero 2 W au port PIO de la PlayStation 1, 
> permettant l'émulation CD-ROM et des fonctionnalités de débogage avancées.

## 🎯 Objectifs du Projet

- **Remplacement du lecteur CD** par une interface plus rapide et fiable
- **Émulation CD-ROM complète** avec support des images ISO
- **Fonctionnalités de débogage** avancées pour le développement PS1
- **Interface réseau** pour le contrôle à distance et le transfert de fichiers
- **Préservation de l'intégrité** de la console PS1 (aucune modification interne)

## 🔧 Caractéristiques Techniques

### Spécifications Matérielles
- **Alimentation** : 5V (via PS1 ou RPi) avec régulation 3.3V intégrée
- **Interface** : SPI 1MHz optimisé pour performances maximales
- **Conversion de niveau** : Bidirectionnelle 3.3V ↔ 5V sécurisée
- **Bus d'adresses** : 16-bit complet (A0-A15)
- **Bus de données** : 8-bit bidirectionnel (D0-D7)
- **Signaux de contrôle** : CS0/CS1, RD/WR, RESET, IRQ

### Compatibilité PlayStation 1
- **Modèles supportés** : SCPH-1000 à SCPH-7500 (avec port PIO)
- **Modèles incompatibles** : PSone (SCPH-9000+) sans port PIO
- **Connecteur** : Port PIO 68 pins propriétaire Sony

## 📞 Contact et Communauté

### 🎥 **Chaînes YouTube**
- **DrJVTek** : [https://www.youtube.com/@DrJVTek](https://www.youtube.com/@DrJVTek)
- **Cyril 2.0** : [https://www.youtube.com/@cyril2pointzero](https://www.youtube.com/@cyril2pointzero)

### 🛒 **Matériel et Composants**
- **Orion Soft** : [https://www.orionsoft.games/retroshop/ps1usb.htm](https://www.orionsoft.games/retroshop/ps1usb.htm)

### 💬 **Support Communautaire**
- **Discord** : [https://discord.gg/TN22P8Dz8S](https://discord.gg/TN22P8Dz8S)
- **GitHub Issues** : [Signaler un problème](https://github.com/PS1Dev-Fr/ps1_extension_RPI/issues)
- **GitHub Discussions** : [Forum communautaire](https://github.com/PS1Dev-Fr/ps1_extension_RPI/discussions)

---

**⚠️ Avertissement** : Ce projet est destiné à des fins éducatives et de développement. 
L'utilisation de ROMs et d'images ISO doit respecter les lois sur le droit d'auteur de votre juridiction.
