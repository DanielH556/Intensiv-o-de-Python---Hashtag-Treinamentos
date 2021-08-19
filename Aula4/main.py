import pandas as pd
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import numpy as np

df = pd.read_csv('Aula4/advertising.csv')

# sns.pairplot(df)
# sns.heatmap(df.corr(), cmap = 'Wistia', annot = True)
x = df.drop('Vendas', axis=1)
y = df['Vendas']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# AI Treino
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

rf_reg = RandomForestRegressor()
rf_reg.fit(x_train, y_train)

# AI Teste
test_pred_lin = lin_reg.predict(x_test)
test_pred_rf = rf_reg.predict(x_test)

r2_lin = metrics.r2_score(y_test, test_pred_lin)
rmse_lin = np.sqrt(metrics.mean_squared_error(y_test, test_pred_lin))
print(f"R² da Regressão Linear: {r2_lin}")
print(f"RMSE da Regressão Linear: {rmse_lin}")

r2_rf = metrics.r2_score(y_test, test_pred_rf)
rmse_rf = np.sqrt(metrics.mean_squared_error(y_test, test_pred_rf))
print(f"R² do Random Forest: {r2_rf}")
print(f"RMSE do Random Forest: {rmse_rf}")

# Análise Gráfica
df_resultado = pd.DataFrame()
df_resultado['y_teste'] = y_test
df_resultado['y_previsao_rf'] = test_pred_rf
df_resultado['y_previsao_lin'] = test_pred_lin
df_resultado = df_resultado.reset_index(drop=True)

fig = plt.figure(figsize=(15, 5))

sns.lineplot(data = df_resultado)
plt.show()
display(df_resultado)

# plt.show()