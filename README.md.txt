# **Projeto de Análise de Dados em Python**

# **Instruções para o Projeto de Análise de Dados em Python**

Este projeto consiste no desenvolvimento de um aplicativo Python para análise de dados. 
Para garantir a independência das dependências, utilizaremos um ambiente virtual. 
As instruções abaixo fornecem um passo a passo para configurar o ambiente e executar o aplicativo.

## **Passo 1: Configuração do Ambiente de Desenvolvimento**

1. Crie um novo diretório para o projeto em sua máquina.
2. Navegue até o diretório do projeto usando o Visual Studio Code.

## **Passo 2: Criação e Ativação do Ambiente Virtual**

1. No Visual Studio Code, abra o terminal integrado.
2. Execute o seguinte comando para criar um ambiente virtual com o nome desejado:

```
Copy code
python -m venv venvcristiano

```

1. Ative o ambiente virtual usando o comando apropriado de acordo com seu sistema operacional:
    - No Windows:
        
        ```
        Copy code
        venvcristiano\Scripts\activate
        
        ```
        
    - No macOS e Linux:
        
        ```bash
        bashCopy code
        source venvcristiano/bin/activate
        
        ```
        

## **Passo 3: Instalação das Dependências**

1. Com o ambiente virtual ativado, instale as bibliotecas necessárias executando o seguinte comando:

```
Copy code
pip install pandas matplotlib numpy

```

1. Após a instalação, utilize o comando **`pip freeze > requirements.txt`** para gerar o arquivo **`requirements.txt`** com as dependências do projeto.

## **Passo 4: Desenvolvimento do Aplicativo**

1. Crie um arquivo Python chamado **`data_analysis.py`** dentro do diretório do projeto.
2. Escreva o código Python dentro deste arquivo para realizar a análise de dados desejada, utilizando as bibliotecas instaladas.

Exemplo de uso de variável de ambiente:

```python
pythonCopy code
import os
import pandas as pd

data_path = os.environ.get('DATA_PATH')
# Utilize 'data_path' para carregar os dados necessários para análise

```

## **Passo 5: Configuração do Variável de Ambiente**

1. No Visual Studio Code, abra o terminal integrado.
2. Execute o seguinte comando para criar uma variável de ambiente com o nome DATA_PATH com  o caminho do arquivo dados.csv:

```
Copy code
set DATA_PATH C:\Users\Professor\Desktop\Django\Exe1.1\dados.csv

```

## **Passo 6: Compartilhamento do Arquivo `requirements.txt`**

Compartilhe o arquivo **`requirements.txt`** com outros desenvolvedores. Eles poderão configurar o ambiente de desenvolvimento executando o comando abaixo:

```
Copy code
pip install -r requirements.txt

```

## **Passo 7: Execução do Aplicativo**

1. Após a instalação das dependências, o aplicativo Python pode ser executado dentro do ambiente virtual.
2. Execute o arquivo **`data_analysis.py`** utilizando o interpretador Python dentro do ambiente virtual.

---

Siga essas instruções para configurar o ambiente de desenvolvimento, instalar as dependências e executar o aplicativo Python para análise de dados.