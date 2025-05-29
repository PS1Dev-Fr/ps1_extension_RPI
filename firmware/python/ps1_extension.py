#!/usr/bin/env python3
"""
Extension PS1 - Firmware Raspberry Pi Zero 2 W
Interface SPI vers PlayStation 1 via port PIO
"""

import time
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PS1Interface:
    """Interface principale pour la communication avec la PS1"""
    
    def __init__(self):
        logger.info("Interface PS1 initialisée")
    
    def start_interface(self):
        """Démarre l'interface PS1"""
        logger.info("Interface PS1 démarrée")
        
        try:
            while True:
                time.sleep(1)
                logger.debug("Interface active...")
                
        except KeyboardInterrupt:
            logger.info("Arrêt demandé par l'utilisateur")

def main():
    """Fonction principale"""
    print("=== Extension PS1 avec Raspberry Pi Zero 2 W ===")
    print("Initialisation de l'interface...")
    
    try:
        ps1 = PS1Interface()
        ps1.start_interface()
        
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
