# Prédiction de Médailles avec un Arbre de Décision 🏅

## Description du Projet 📖

Ce projet utilise un **arbre de décision** pour prédire si un athlète remportera une médaille ou non, basé sur des données démographiques comme l'âge et le genre. Le modèle permet d'identifier des critères significatifs qui influencent les performances des athlètes.

Le projet suit plusieurs étapes essentielles, notamment :

- **Prétraitement des données** : Nettoyage et préparation des données pour les rendre exploitables.
- **Construction d'un modèle prédictif** : Utilisation d'un arbre de décision pour analyser les variables influentes.
- **Visualisation des résultats** : Création d'une visualisation claire et interprétable de l'arbre de décision.

---

## Fonctionnalités principales 🚀

### Prétraitement des données 🧹

1. **Conversion des variables catégoriques :**

   - La colonne `gender` a été transformée en valeurs numériques :
     - `0` pour les hommes.
     - `1` pour les femmes.

2. **Calcul de l'âge :**

   - L'âge des athlètes a été calculé automatiquement à partir de leur date de naissance (`birth_date`).
   - Les lignes contenant des dates invalides ou manquantes ont été supprimées.

3. **Gestion des valeurs manquantes :**
   - Les observations sans âge ou avec des valeurs manquantes dans d'autres colonnes importantes ont été supprimées.
   - **Nombre total de lignes supprimées :** Calculé et affiché pour documenter la qualité du nettoyage des données.

### Construction d'un arbre de décision 🌳

- **Bibliothèque utilisée :**
  - Le modèle est construit à l'aide de `DecisionTreeClassifier` de la bibliothèque Scikit-learn.
- **Critères utilisés pour la prédiction :**

  - `age` : L'âge des athlètes, qui est la variable la plus influente.
  - `gender` : Le genre des athlètes, avec des interactions spécifiques influençant les performances.

- **Profondeur de l'arbre :**

  - L'arbre de décision est limité à une profondeur maximale de 5 pour éviter le surapprentissage tout en conservant une interprétabilité optimale.

- **Variable cible :**
  - `is_medallist` : Indique si un athlète a remporté une médaille (`1`) ou non (`0`).

### Visualisation et export 📷

- **Visualisation de l'arbre :**

  - L'arbre de décision est affiché avec des nœuds colorés pour indiquer la classe prédite (`Medal` ou `No Medal`) et les informations telles que :
    - Les règles de séparation (`age <=`, `gender =`, etc.).
    - La pureté de chaque nœud (indice de Gini).
    - Le nombre d'échantillons dans chaque groupe (`samples`).
    - Les prédictions de classe (`class`).

- **Exportation :**
  - La visualisation est exportée sous forme d'image haute résolution au format **JPG**.

---

## Résultats obtenus 📊

### Critères décisifs 🧐

- L'analyse a montré que :
  - L'âge est la **variable la plus influente** pour prédire les chances de remporter une médaille.
  - Le genre joue également un rôle important mais intervient principalement en combinaison avec l'âge.

### Interprétation de l'arbre 🌟

- **Athlètes âgés (> 45,5 ans) :**
  - Ces athlètes ont une probabilité faible de remporter une médaille, ce qui est souvent lié aux exigences physiques des compétitions.
- **Jeunes athlètes (âgés de 16,5 ans ou moins) :**
  - Les jeunes athlètes combinés à d'autres caractéristiques (comme le genre) peuvent également avoir des chances plus faibles de remporter une médaille.
- **Groupes spécifiques :**
  - L'arbre révèle des combinaisons particulières où certains sous-groupes, en fonction de leur âge et de leur genre, ont des probabilités élevées ou faibles de gagner une médaille.

### Visualisation des résultats :

L'arbre montre des séparations claires et facilement interprétables, avec des décisions basées principalement sur l'âge et le genre.

---

## Améliorations possibles 🔧

### Optimisation des hyperparamètres :

- Ajuster des paramètres comme :
  - La **profondeur maximale** (`max_depth`) de l'arbre.
  - Le **nombre minimum d'échantillons** nécessaires pour une division (`min_samples_split`).
- Cela pourrait permettre d'améliorer la précision tout en évitant le surapprentissage.

### Enrichissement des données :

- Ajouter des variables supplémentaires pour capturer davantage de facteurs influents, par exemple :
  - Le type de sport ou discipline (`event` ou `discipline`).
  - Le pays d'origine (`country`) pour représenter les différences culturelles et structurelles.
  - Les performances passées ou l'expérience des athlètes.

### Validation croisée :

- Mettre en œuvre une validation croisée pour évaluer la robustesse du modèle sur plusieurs sous-ensembles des données.

### Analyse de l'équilibre des classes :

- Si le jeu de données est déséquilibré (beaucoup plus de "No Medal" que de "Medal"), des techniques comme :
  - **Sur-échantillonnage** des classes minoritaires.
  - **Pondération des classes** dans le modèle.
  - Ces approches pourraient améliorer les prédictions pour les cas minoritaires (médaille).

---

## Technologies utilisées 🛠️

- **Python** : Langage de programmation principal.
- **Bibliothèques Python :**
  - `pandas` pour la manipulation des données.
  - `scikit-learn` pour la construction du modèle et l'arbre de décision.
  - `matplotlib` pour la visualisation de l'arbre.

---

## Installation et Exécution 🖥️

1. **Cloner le projet :**

   ```bash
   git clone https://github.com/votre_utilisateur/decision-tree-medals.git
   cd decision-tree-medals
   ```

2. **Installez les dépendances Python :**

```bash
pip install pandas matplotlib scikit-learn
```

## Auteur ✍️

Nom : BENMAMMAR HOUSSAM
GitHub : HoussemBenmammar

## Licence 📜

Vous pouvez directement copier ce contenu dans votre fichier `README.md`. Si vous avez des questions ou souhaitez des ajustements, n'hésitez pas ! 😊
