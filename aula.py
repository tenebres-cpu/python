#ex1
import pandas as pd
dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

#Estrutura de repetição

for indice, linha in df.iterrows():
    print(f"Indice:{indice}, Nome: {linha['Nome']}, Idade: {linha['Idade']}")

#ex2

dados = {
    'Aluno': ['joão', 'maria', 'pedro'],
    'Nota1': [7.5, 8.0, 6.5],
    'Nota2': [8.0, 9.0, 7.0],
    }
df1 = pd.DataFrame(dados)

# calcular a média de notas dos aulunos

for indice, linha in df1.iterrows():
    media = (linha["Nota1"] + linha["Nota2"] / 2)
    print(f"{linha['Aluno']} tem média {media:.1f}")

#ex3

import pandas as pd
dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)


#for indice, linha in df.iterrows():
#    df.at[indice, 'Idade'] = linha['Idade'] + 1  
#print(df)

df['Idade_Nova'] = df['Idade'] + 1
df
print(df)

# Estrura de repetição com while

dados = {
    dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH'],
}

df = pd.DataFrame(dados)
indice = 0
encontrou = False

while indice < len(df) and not encontrou:
    if df.loc[indice, "Nome"] == 'bruno':
    print(f"Bruno encontradono indice {indice}")
    encontrou = True
    indice += 1
}


# ex: função apply

dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH'],
}

df = pd.DataFrame(dados)

df ['Nome1'] = df['Nome'].apply(lambda x: x.upper())
df

# Função para aplicar descontos 

dados = {
    "Ptoduto": ['caneta', 'caderno', 'livro'],
    "Preço": [5, 30, 45],
}

df = pd.DataFrame(dados)

def aplica_desconto(preso):
    desconto = preso * 0.9
    return desconto
df['Preço com Desconto'] = df['Preço'].apply(aplica_desconto)
df

#para importar
import pandas as pd 
df = pd.read_csv('/content/manutencao_preditiva.csv')

#calcular min, max, mean, median

#calculo basico estatistico da variavel temperatura do ar

print(df['Temperatura Ar [K]'].min())
print(df['Temperatura Ar [K]'].max())
print(df['Temperatura Ar [K]'].mean())
print(df['Temperatura Ar [K]'].median())


# Uso do matplotlip
import matplotlib.pyplot as plt

y - df['Temperatura Ar [K]']
x - df['UDI']

plt.plot(x, y1, x, y2)
plt.legend(['ar', 'Processo'])
plt.xlabel('ocorrências')
plt.xlabel('Temperaturas')
plt.show()



#Categorizar informações

def categorizar_torque(torque):
    if torque < 20:
        return 'baixo'
    elif torque < 40:
        return'medio'
    else:
        return'alto'

df['Torque 1'] = df['Torque [Nm]'].apply(categorizar_torque)
df['Torque 1'].value_counts()
