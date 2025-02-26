# TaskManager 📝

**TaskManager** é um projeto desenvolvido para fins de estudo, focado na aplicação dos princípios da **Clean Architecture** e do **SOLID** utilizando **Flask** e **MySQL**.  

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python** (Flask)
- 🗄️ **MySQL**
- 📦 **SQLAlchemy**
- 🔄 **Flask-Migrate**
- 🛠 **Marshmallow** (para validação de dados)
- 🧪 **Pytest** (para testes)

---

## 📂 Estrutura do Projeto

```plaintext
project/
│── src/
│   ├── composer/         # Composers para montar as dependências
│   ├── presenters/       # Presenters para formatar as responses
│   ├── domain/           # Regras de negócio (Entidades e Casos de Uso)
│   │   ├── entities/
│   │   ├── use_cases/
│   ├── data/             # Interfaces dos repositórios e modelos
│   │   ├── repositories/
│   │   ├── interfaces/   # Interfaces dos repositórios
│   │   ├── models/
│   ├── infra/            # Implementações concretas (Banco de Dados, API, etc.)
│   │   ├── services/
│   │   ├── repositories/
│   ├── errors/           # Error Handler e Custom errors
│   │   ├── custom_errors/
│   │   ├── error_handle/
│   ├── presentation/     # Controllers (rotas e entrada da API)
│   ├── app.py            # Ponto de entrada da aplicação
│   ├── config.py         # Configuração do banco
│   ├── utils.py          # Instanciar módulos para evitar imports circulares
│── tests/                # Testes unitários e de integração
│── requirements.txt      # Dependências do projeto
