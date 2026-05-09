import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import warnings

warnings.filterwarnings('ignore')

os.makedirs('images', exist_ok=True)
df = pd.read_csv('local_data/dataset_limpo.csv', sep=';')
sns.set_theme(style="whitegrid")

# 1. IAN
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='IAN_2022', kde=True, color='teal')
plt.title('Perfil de Adequacao ao Nivel (IAN) - 2022')
plt.savefig('images/ian_dist.png', bbox_inches='tight', dpi=150)
plt.close()

# 2. IDA por Fase
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='FASE', y='IDA_2022', palette='viridis')
plt.title('Desempenho Academico (IDA) por Fase')
plt.savefig('images/ida_fase.png', bbox_inches='tight', dpi=150)
plt.close()

# 3. IEG vs IDA
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x='IEG_2022', y='IDA_2022', hue='PONTO_VIRADA_2022', alpha=0.6)
plt.title('Engajamento vs Desempenho')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.savefig('images/ieg_ida.png', bbox_inches='tight', dpi=150)
plt.close()

# 4. IAA vs IDA
plt.figure(figsize=(7, 4))
sns.kdeplot(df['IAA_2022'].dropna(), label='Autoavaliacao (IAA)', fill=True)
sns.kdeplot(df['IDA_2022'].dropna(), label='Nota Real (IDA)', fill=True)
plt.title('Autoavaliacao vs Desempenho Real')
plt.legend()
plt.savefig('images/iaa_ida.png', bbox_inches='tight', dpi=150)
plt.close()

# 5. IPS vs INDE
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x='REC_PSICOLOGIA_2022', y='INDE_2022', palette='Set2')
plt.title('Impacto do Suporte Psicologico no Indice Global (INDE)')
plt.savefig('images/ips_inde.png', bbox_inches='tight', dpi=150)
plt.close()

# 6. Efetividade Pedras
pedra_order = ['Quartzo', 'Ágata', 'Ametista', 'Topázio']
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x='PEDRA_2022', y='INDE_2022', order=pedra_order, palette='coolwarm')
plt.title('Media do INDE por Categoria de Pedra')
plt.savefig('images/pedra_inde.png', bbox_inches='tight', dpi=150)
plt.close()

# ML
df['RISCO_DEFASAGEM'] = np.where(df['IAN_2022'] <= 5.0, 1, 0)
features = ['FASE', 'IDADE_2022', 'IAA_2022', 'IEG_2022', 'IPS_2022', 'QTD_AVALIACOES_2022', 'DEFASAGEM_2022']
X = df[features].fillna(df[features].median())
y = df['RISCO_DEFASAGEM']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 7. Confusion Matrix
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Baixo Risco', 'Alto Risco'], yticklabels=['Baixo Risco', 'Alto Risco'])
plt.title('Matriz de Confusao')
plt.ylabel('Realidade')
plt.xlabel('Previsao')
plt.savefig('images/confusion_matrix.png', bbox_inches='tight', dpi=150)
plt.close()

# 8. Feature Importance
importances = model.feature_importances_
feat_df = pd.DataFrame({'Feature': features, 'Importancia': importances}).sort_values(by='Importancia', ascending=False)
plt.figure(figsize=(8, 4))
sns.barplot(data=feat_df, x='Importancia', y='Feature', palette='rocket')
plt.title('Importancia das Variaveis (Feature Importance)')
plt.savefig('images/feature_importance.png', bbox_inches='tight', dpi=150)
plt.close()
