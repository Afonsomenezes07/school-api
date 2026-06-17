# School API

API REST para gerenciamento de alunos, matérias e notas.

## Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- Django Filter
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
- Busca de alunos por nome e e-mail
- Busca de matérias por nome
- Filtros de notas por aluno
- Filtros de notas por matéria
- Integração com PostgreSQL
- Containerização com Docker

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
git clone https://github.com/Afonsomenezes07/school-api.git
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

## Parar containers

```bash
docker compose down
```

---

## Visualizar logs

```bash
docker compose logs -f
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

# Acessar Admin

```text
http://localhost:8000/admin/
```

---

# Endpoints

## Students

| Método | Endpoint |
|----------|----------|
| GET | /api/students/ |
| POST | /api/students/ |
| PUT | /api/students/{id}/ |
| DELETE | /api/students/{id}/ |

---

## Subjects

| Método | Endpoint |
|----------|----------|
| GET | /api/subjects/ |
| POST | /api/subjects/ |
| PUT | /api/subjects/{id}/ |
| DELETE | /api/subjects/{id}/ |

---

## Grades

| Método | Endpoint |
|----------|----------|
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
  "name": "João Silva",
  "email": "joao@email.com"
}
```

---

# Paginação

A API possui paginação habilitada com 5 registros por página.

Exemplos:

```text
/api/students/?page=1
```

```text
/api/students/?page=2
```

---

# Busca

## Buscar alunos por nome

```text
/api/students/?search=joao
```

---

## Buscar alunos por e-mail

```text
/api/students/?search=gmail
```

---

## Buscar matérias por nome

```text
/api/subjects/?search=mat
```

---

# Filtros

## Filtrar notas por aluno

```text
/api/grades/?student=1
```

---

## Filtrar notas por matéria

```text
/api/grades/?subject=2
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

# Executar migrations

```bash
python manage.py migrate
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
- Permissões de usuário
- Deploy em nuvem

---

# Autor

Afonso Menezes

GitHub:
https://github.com/Afonsomenezes07