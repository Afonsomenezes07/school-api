# School API

API REST para gerenciamento de alunos, matérias e notas.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Git/GitHub

---

# Funcionalidades

- CRUD completo de alunos
- CRUD completo de matérias
- CRUD completo de notas
- Endpoints RESTful
- Paginação
- Integração com PostgreSQL
- Containerização com Docker
- Filtros na API

---

# Estrutura do Projeto

```bash
school-api/
│
├── core/
├── school/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── manage.py
└── README.md
```

---

# Como executar o projeto

## Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/school-api.git
```

```bash
cd school-api
```

---

# Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
DB_NAME=schooldb
DB_USER=schooluser
DB_PASSWORD=schoolpass
DB_HOST=db
DB_PORT=5432
```

---

# Executar com Docker

## Subir containers

```bash
docker compose up --build
```

---

# Executar migrations

```bash
docker compose exec web python manage.py migrate
```

---

# Criar superusuário

```bash
docker compose exec web python manage.py createsuperuser
```

---

# Acessar API

```text
http://localhost:8000/api/
```

---

# Endpoints

## Students

| Método | Endpoint |
|---|---|
| GET | /api/students/ |
| POST | /api/students/ |
| PUT | /api/students/{id}/ |
| DELETE | /api/students/{id}/ |

---

## Subjects

| Método | Endpoint |
|---|---|
| GET | /api/subjects/ |
| POST | /api/subjects/ |
| PUT | /api/subjects/{id}/ |
| DELETE | /api/subjects/{id}/ |

---

## Grades

| Método | Endpoint |
|---|---|
| GET | /api/grades/ |
| POST | /api/grades/ |
| PUT | /api/grades/{id}/ |
| DELETE | /api/grades/{id}/ |

---

# Exemplo de requisição

## Criar aluno

### POST

```http
POST /api/students/
```

### Body

```json
{
  "name": "João",
  "email": "joao@email.com"
}
```

---

# Paginação

A API possui paginação habilitada.

Exemplo:

```text
/api/students/?page=2
```

---

# Rodando sem Docker

## Criar ambiente virtual

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Executar servidor

```bash
python manage.py runserver
```

---

# Melhorias futuras

- Autenticação JWT
- Swagger/OpenAPI
- Deploy em nuvem
- Permissões de usuário

---
# Autor

Afonso Menezes

GitHub:
https://github.com/Afonsomenezes07