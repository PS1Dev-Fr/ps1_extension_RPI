#!/usr/bin/env python3
"""
Suite de tests complète pour l'extension PS1
"""

import unittest
import sys
import os

# Ajouter le répertoire firmware au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../firmware/python'))

from test_spi import TestSPI
from test_mcp23s17 import TestMCP23S17
from test_ps1_interface import TestPS1Interface
from test_performance import TestPerformance

def run_all_tests():
    """Lance tous les tests de validation"""
    
    print("=== Tests Extension PS1 ===")
    print("Démarrage de la suite de tests complète...\n")
    
    # Créer la suite de tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajouter tous les tests
    suite.addTests(loader.loadTestsFromTestCase(TestSPI))
    suite.addTests(loader.loadTestsFromTestCase(TestMCP23S17))
    suite.addTests(loader.loadTestsFromTestCase(TestPS1Interface))
    suite.addTests(loader.loadTestsFromTestCase(TestPerformance))
    
    # Lancer les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Résumé
    print(f"\n=== Résumé des tests ===")
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Erreurs: {len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Succès: {result.testsRun - len(result.errors) - len(result.failures)}")
    
    if result.wasSuccessful():
        print("✅ Tous les tests sont passés avec succès !")
        return True
    else:
        print("❌ Certains tests ont échoué.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)