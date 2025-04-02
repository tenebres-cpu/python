#ex1
import pandas as pd
dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)

#Estrutura de repetição

for indice, linha in df.interrows():
    print(f"Indice:{indice}, Nome: {Linha['Nome']}, Idade: {linha['idade']}")

#ex2

dados = {
    'Aluno': ['joão', 'maria', 'pedro'],
    'Nota1': [7.5, 8.0, 6.5],
    'Nota2': [8.0, 9.0, 7.0],
    }
df1 = pd.DataFrame(dados)

# calcular a média de notas dos aulunos

for indice, linha in df.iterrows():
    media = (linha["Nota1"] + linha["Nota2"] / 2)
    print(f"{linha['Aluno']} tem média {media:.1f}")

#ex3
dados = {
    "Nome": ['ana', 'brono', 'carlos'],
    "Idade": [25, 30, 22],
    "Cidade": ['SP', 'RJ', 'BH']
}

df = pd.DataFrame(dados)


#for indice, linha in df.interrows():
#    df.at[indice, 'idade'] = linha['idade'] + 1  
#print(df)

df['Idade_Nova'] = df['idade'] + 1
df

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

