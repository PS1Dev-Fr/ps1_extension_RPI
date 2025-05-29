# Guide de Contribution

Merci de votre intérêt pour contribuer au projet PS1 Extension ! 

## 🚀 Comment contribuer

### 1. Signaler un bug
- Utilisez les [issues GitHub](https://github.com/PS1Dev-Fr/ps1_extension_RPI/issues)
- Décrivez le problème en détail
- Incluez les informations système (modèle RPi, version PS1, etc.)
- Ajoutez les logs si possible

### 2. Proposer une fonctionnalité
- Ouvrez une issue avec le tag "enhancement"
- Décrivez clairement la fonctionnalité souhaitée
- Expliquez pourquoi elle serait utile

### 3. Contribuer au code
1. Forkez le repository
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`)
3. Commitez vos changements (`git commit -am 'Ajoute ma fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/ma-fonctionnalite`)
5. Créez une Pull Request

## 📋 Standards de code

### Python
- Suivez PEP 8
- Utilisez des docstrings pour les fonctions
- Ajoutez des tests unitaires
- Maximum 88 caractères par ligne

### KiCad
- Utilisez des noms de composants explicites
- Commentez les schémas complexes
- Respectez les règles de routage définies

## 🧪 Tests

Avant de soumettre une PR :
```bash
# Tests automatiques
python3 -m pytest tests/
python3 tests/test_all.py

# Vérification du code
flake8 firmware/
black firmware/ --check
```

## 📝 Messages de commit

Format : `[type]: description courte`

Types :
- `feat`: nouvelle fonctionnalité
- `fix`: correction de bug
- `docs`: documentation
- `style`: formatage
- `refactor`: refactorisation
- `test`: ajout de tests
- `chore`: maintenance

Exemple : `feat: ajoute support des images BIN/CUE`