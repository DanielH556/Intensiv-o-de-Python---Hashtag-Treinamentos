import pandas as pd
import pyautogui
import time
import pyperclip
from IPython.display import display

# Automação do pyautogui
pyautogui.PAUSE = 1
# Abrir navegador
pyautogui.press("winleft")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.alert("O processo de envio de e-mails será iniciado, não faça nada após pressionar o botão OK")
pyautogui.hotkey('ctrl', 't')
pyautogui.write("mail.google.com")
pyautogui.press("enter")

time.sleep(12)

pyautogui.click(121,205)

time.sleep(12)

pyautogui.write("kasaipkm.contato@gmail.com")
pyautogui.press('tab')
pyautogui.press('tab')

assunto = "Relatório de Vendas de Ontem"

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press('tab')

df = pd.read_excel(r'C:\Users\User\Desktop\Estudos\Intesivão de Python - Hashtag Treinamentos\Exportar\Vendas - Dez.xlsx')
# display(df)

# Faturamento e Qtd de vendas
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: R${qtde_produtos:,}

Obrigada pela atenção
Dani"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')