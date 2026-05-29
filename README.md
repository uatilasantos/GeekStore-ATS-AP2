# 🛒 GeekStore ATS - AP2

Projeto desenvolvido para a atividade de **Automação e Testes de Software (ATS)**.

O sistema simula uma loja virtual simples utilizando **FastAPI** e **SQLite**, com foco em testes automatizados e integração contínua.

---

# 🚀 Tecnologias Utilizadas

* Python
* FastAPI
* SQLite
* Pytest
* Selenium
* Tavern
* GitHub Actions

---

# 📂 Estrutura do Projeto

```bash
GEEKSTORE-ATS-AP2/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── main.yml
│
├── tests/
│   ├── features/
│   ├── selenium/
│   ├── steps/
│   ├── tavern/
│   ├── test_api.py
│   ├── test_gateway.py
│   └── test_services.py
│
├── conftest.py
├── database.py
├── gateway.py
├── index.html
├── main.py
├── requirements.txt
└── services.py
```

---

# ⚙️ Como Executar o Projeto

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Iniciar aplicação

```bash
uvicorn main:app --reload
```

A aplicação ficará disponível em:

```bash
http://127.0.0.1:8000
```

---

# 🧪 Executando os Testes

## Rodar todos os testes

```bash
pytest -v
```

---

## Rodar testes com cobertura

```bash
pytest --cov=. --cov-fail-under=90
```

---

# ✅ Testes Implementados

* Testes Unitários
* Testes de API
* Testes com Mock
* Testes BDD
* Testes Tavern
* Testes E2E com Selenium

---

# 🔄 Integração Contínua

O projeto utiliza GitHub Actions para executar os testes automaticamente a cada push no repositório.

---

# 📄 Objetivo da Atividade

Aplicar conceitos de:

* Qualidade de Software
* Testes Automatizados
* Cobertura de Código
* Integração Contínua
* Testes de API
* Testes End-to-End

---

# 👨‍💻 Autor

Uatila Dos Santos Silva
