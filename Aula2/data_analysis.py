import pandas as pd
from IPython.display import display
import plotly.express as px

df = pd.read_csv("Aula2/telecom_users.csv")

# Retirar coluna Unnamed: 0
df = df.drop(["Unnamed: 0"], axis=1) 
# Axis -> 1 = coluna / 0 = linha

df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how='all', axis=1)
df = df.dropna()

for coluna in df:
  if coluna != 'IDCliente':
    # Cria figura
    fig = px.histogram(df, x=coluna, color='Churn')
    # Exibe figura
    fig.show()
    display(df.pivot_table(index='Churn', columns=coluna, aggfunc='count')['IDCliente'])

# Quantos cancelaram o contrato e quantos estão ativos
display(df['Churn'].value_counts())
display("==========")
display(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))