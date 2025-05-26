📖 Calculadora de Custos para Marketplace

📌 Descrição

Este projeto é uma aplicação web desenvolvida em Django para calcular custos de vendas em marketplaces, levando em consideração preço de custo, taxas e impostos, e fornecendo lucro e percentual de lucro.

✅ Pré-requisitos

Antes de rodar o projeto, certifique-se de que o ambiente está configurado corretamente.

🔹 Softwares e dependências necessárias
- Python (versão 3.8 ou superior)
- Django (última versão estável)
- Visual Studio Code (VS Code) (opcional, mas recomendado)  
- Extensões do VS Code recomendadas:
- Python
- Django
- Pylance

🏗 Passo a Passo - Instalação e Configuração

1️⃣ Clonar o Repositório
git clone https://github.com/estevaoIA/SAAS.git
Pasta do projeto
cd marketplace_calculator


Se estiver usando um ZIP, basta extrair a pasta do projeto.

2️⃣ Criar e Ativar um Ambiente Virtual
Criar um ambiente virtual (opcional, mas recomendado):
python -m venv venv


Ativar o ambiente virtual:
- Windows:
venv\Scripts\activate
- Mac/Linux:
source venv/bin/activate



3️⃣ Instalar Dependências
Instale as dependências com:
pip install -r requirements.txt


4️⃣ Configurar o Banco de Dados
Execute as migrações para configurar o banco de dados SQLite:
python manage.py migrate


Isso criará as tabelas necessárias no banco.
Opcionalmente, você pode criar um superusuário para acessar o painel administrativo do Django:
python manage.py createsuperuser

![image](https://github.com/user-attachments/assets/13d4a9d5-7491-4804-b5f5-0145390776f6)

Defina um nome de usuário, e-mail e senha.

5️⃣ Rodar o Servidor
Agora, execute o servidor local:
python manage.py runserver


Acesse a aplicação pelo navegador em:
http://127.0.0.1:8000/







📜 Funcionamento da Aplicação
- O usuário preenche os campos na página inicial (calculate.html):
- Preço de custo
- Preço de venda
- Taxa percentual do marketplace
- Taxa fixa do marketplace
- Imposto percentual
- Ao clicar em “Calcular”, os dados são enviados para a função calculate_cost no views.py.
- O Django processa os cálculos e exibe os resultados no result.html, mostrando:
- Receita Bruta
- Lucro
- Percentual de Lucro (formatado corretamente com duas casas decimais)
