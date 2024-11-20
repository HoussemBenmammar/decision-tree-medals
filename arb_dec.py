# Charger les bibliothèques nécessaires
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.preprocessing import LabelEncoder

# Charger les données des médailles (ajustez le chemin vers votre fichier CSV)
data = pd.read_csv('medals_dataset.csv')

# Afficher les premières lignes pour comprendre la structure des données
print(data.head())

# Préparer les données pour l'arbre de décision
# Sélection des caractéristiques à utiliser pour l'arbre de décision
# Par exemple : 'age', 'gender', 'event', 'country', etc.

# Conversion de la colonne 'gender' (M/F) en valeurs numériques (0 et 1)
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])

# Extraire l'âge (calculé à partir de l'année de naissance si nécessaire)
data['birth_date'] = pd.to_datetime(data['birth_date'], errors='coerce')
data['age'] = 2024 - data['birth_date'].dt.year

# Avant de supprimer les lignes sans âge
num_rows_before = data.shape[0]

# Suppression des lignes avec des âges manquants
data.dropna(subset=['age'], inplace=True)

# Après avoir supprimé les lignes
num_rows_after = data.shape[0]


# Sélectionner les caractéristiques X et la variable cible y
X = data[['age', 'gender']]  # Utilisez ici les colonnes qui vous intéressent
y = data['is_medallist']  # 0 = Pas de médaille, 1 = Médaille

# Créer un arbre de décision
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X, y)

# Afficher le nombre de lignes supprimées
print(f"Nombre de lignes supprimées (sans âge) : {num_rows_before - num_rows_after}")


# Afficher l'arbre de décision et l'enregistrer en JPG
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['No Medal', 'Medal'], filled=True)
plt.title("Arbre de décision pour prédire la médaille")
plt.savefig("decision_tree_medal.jpg", format='jpg', dpi=300)  # Enregistrer sous format JPG avec une bonne résolution
plt.show()
