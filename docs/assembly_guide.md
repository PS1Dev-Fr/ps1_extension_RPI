# Guide d'Assemblage PCB

## 🔧 Outils Nécessaires

- Station de soudage (25-40W)
- Soudure (0.6-0.8mm, sans plomb)
- Flux de soudage
- Tresse à dessouder
- Multimètre
- Loupe/microscope (optionnel)
- Pince à épiler

## 📋 Ordre d'Assemblage

### Étape 1 : Composants SMD 0805
1. **Résistances** (R1-R12) - 10kΩ
2. **Condensateurs céramiques** (C3-C18) - 100nF

**Technique :**
- Appliquer flux sur les pads
- Pré-étamer un pad
- Positionner le composant
- Souder le second pad
- Reprendre le premier pad

### Étape 2 : Circuits Intégrés SMD
1. **Régulateur U1** (AMS1117-3.3, SOT-223)
2. **Convertisseurs U2-U4** (TXB0108, TSSOP-20)  
3. **Expandeurs U5-U6** (MCP23S17, SOIC-28)

**Technique SOIC/TSSOP :**
- Flux abondant sur les pads
- Pré-étamer les pads d'angle
- Aligner le composant avec le repère pin 1
- Souder les pins d'angle
- Souder toutes les pins avec soudure fine
- Nettoyer les courts-circuits avec tresse

### Étape 3 : Composants Traversants
1. **Condensateurs électrolytiques** (C1-C2)
2. **LED de statut** (D1)
3. **Connecteurs** (J1, J2)

### Étape 4 : Tests Intermédiaires
Après chaque étape, vérifier :
- **Continuité** des connexions importantes
- **Courts-circuits** entre pistes
- **Orientation** des composants polarisés

## 🧪 Tests de Validation

### Test d'Alimentation
```bash
# Mesures multimètre
- Pin VIN U1 : 5V ±0.25V
- Pin VOUT U1 : 3.3V ±0.1V  
- Consommation totale : <200mA