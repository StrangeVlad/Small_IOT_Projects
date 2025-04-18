import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

# Charger le dataset
file_path = '50_lines_data.csv'
data = pd.read_csv(file_path)


# Convertir 'Timestamp' en datetime pour un tri temporel
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data_sorted = data.sort_values('Timestamp')

# Verifier le type des données 
data.info()

# Supprimer la colonne 'Flags' à cause des valeurs manquantes
data = data.drop('Flags', axis=1)


# Afficher les premières lignes pour vérifier
print(data.head(5))


# Utiliser un encodage avec LabelEncoder
label_encoder = LabelEncoder()
data['Device_Type'] = label_encoder.fit_transform(data['Device_Type'])
data['Protocol'] = label_encoder.fit_transform(data['Protocol'])
data['Activity'] = label_encoder.fit_transform(data['Activity'])
data['Src_IP'] = label_encoder.fit_transform(data['Src_IP'])
data['Dst_IP'] = label_encoder.fit_transform(data['Dst_IP'])

data.head(5)

# Séparer les features (X) et la cible (y)
X = data.drop(['Label','Timestamp'], axis=1)  # Les features
y = data['Label']  # La Target


# Séparer les données en training et test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# 1. Random Forest
# ------------------------------

# Initialiser le classificateur Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# Prédictions sur le jeu de test
y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("==== Random Forest ====")
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

print(y.value_counts())

# Définir la grille des hyperparamètres à tester
param_grid = {
    'n_estimators': [50, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10,20],
    'min_samples_leaf': [1, 2, 4]
}

# GridSearchCV avec validation croisée
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Afficher les meilleurs hyperparamètres trouvés
print(f"Meilleurs paramètres : {grid_search.best_params_}")

# ------------------------------
# 2. Gradient Boosting Model (GBM)
# ------------------------------
gbm_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
gbm_model.fit(X_train, y_train)

# Prédictions sur le jeu de test
y_pred_gbm = gbm_model.predict(X_test)

# Évaluer le modèle GBM
accuracy_gbm = accuracy_score(y_test, y_pred_gbm)

print("==== Gradient Boosting Model (GBM) ====")
print(f"Accuracy: {accuracy_gbm}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_gbm))
print("Classification Report:")
print(classification_report(y_test, y_pred_gbm))

# -------------------------------
# 3. Logistic Regression Model
# -------------------------------

log_reg_model = LogisticRegression(max_iter=1000, random_state=42)
log_reg_model.fit(X_train, y_train)

# Prédictions sur le jeu de test
y_pred_log_reg = log_reg_model.predict(X_test)

# Évaluer le modèle Logistic Regression
accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)
roc_auc_log_reg = roc_auc_score(y_test, y_pred_log_reg)

print("==== Logistic Regression Model ====")
print(f"Accuracy: {accuracy_log_reg}")
print(f"ROC AUC: {roc_auc_log_reg}")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_log_reg))
print("Classification Report:")
print(classification_report(y_test, y_pred_log_reg))


rf_model = RandomForestClassifier(
    max_depth=10,
    min_samples_leaf=4,
    min_samples_split=10,
    n_estimators=50,
    random_state=42
)

# Entraîner le modèle
rf_model.fit(X_train, y_train)

# Prédictions sur le jeu de test
y_pred_rf = rf_model.predict(X_test)

# Évaluation du modèle
accuracy_rf = accuracy_score(y_test, y_pred_rf)
roc_auc_rf = roc_auc_score(y_test, y_pred_rf)
print(f"Accuracy: {accuracy_rf}")