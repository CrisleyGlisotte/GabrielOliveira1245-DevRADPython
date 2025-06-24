# 💱 Conversor de Moedas - Projeto RAD em Flask

Consiste em desenvolver uma plataforma para *converter moedas (USD, EUR, BRL)* em tempo real, utilizando *dados oficiais do Banco Central do Brasil (BACEN)*. O projeto inclui autenticação de usuários, armazenamento de dados em banco SQLite, e interface web com formulário de conversão.

## 🔧 Requisitos:

- Python 3.8+
- Flask
- Banco de dados: SQLite


### 🗃️ Tabela 'usuarios' com os seguintes campos:
```
id: 5ae01089-d05c-4464-a5c9-3a3004fb24d2
timestamp: Jun 11 2025, 16:15:46
nomeCompleto: text (nullable)
telefone: text (nullable)
email: text (nullable)
```

## Imagens das Capturas de Tela:
```
![Tela de Login](https://github.com/CrisleyGlisotte/GabrielOliveira1245-DevRADPython/blob/main/Tela%20de%20Login.png?raw=true)

![Tela do Conversor de Moedas](https://github.com/CrisleyGlisotte/GabrielOliveira1245-DevRADPython/blob/main/Tela%20do%20Conversor%20de%20Moedas.png?raw=true)

![Tela do Perfil de Usuário](https://github.com/CrisleyGlisotte/GabrielOliveira1245-DevRADPython/blob/main/TeladoPerfildeUsuario.png?raw=true)
```

## 🔐 Configuração de acesso ao banco de dados:
```
DATABASE_URL=sqlite:///database/conversor.db  
DATABASE_KEY="1d1f2e6f2b053c8b4b7c2d8a9f0e1c3b4a5d6e7f8g9h"
```
## 📁 Estrutura do projeto:
```
conversor_moedas_Turatti/
├── pycache/
│ ├── app.cpython-313.pyc
│ └── config.cpython-313.pyc
├── database/
│ ├── pycache/
│ │ └── db.cpython-313.pyc
│ ├── conversor.db
│ └── db.py
├── models/
│ ├── pycache/
│ │ ├── perfil.cpython-313.pyc
│ │ └── usuario.cpython-313.pyc
│ ├── perfil.py
│ └── usuario.py
├── routes/
│ ├── pycache/
│ │ ├── auth_routes.cpython-313.pyc
│ │ └── main_routes.cpython-313.pyc
│ ├── auth_routes.py
│ └── main_routes.py
├── services/
│ ├── pycache/
│ │ └── conversion.cpython-313.pyc
│ └── conversion.py
├── static/
│ └── style.css
├── templates/
│ ├── base.html
│ ├── dashboard.html
│ ├── login.html
│ ├── perfil.html
│ └── register.html
├── .env
├── app.py
├── config.py
├── init_db.py
├── requirements.txt
└── README.md
```
## 📦 Instale os requisitos do projeto:
```
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate       # macOS/Linux

pip install -r requirements.txt

```
## 🚀 Execute o projeto:
```
 python app.py
```
