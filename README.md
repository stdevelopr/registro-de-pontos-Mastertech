# Instruções:

\*\*Desenvolvido em python 3.6.9.

Instalar os requerimentos:

- pip install -r requirements.txt

Exportar a variável de ambinte:

- export FLASK_APP=flaskr


Gerar o banco de dados:
*** Caso realize o clone deste repositório esse passo já está feito e o banco de dados encontra-se na pasta instance.
- flask db init
- flask db migrate -m "Initial migration."
- flask db upgrade

Para os testes unitários rodar na raiz aplicação:

- python -m unittest

Para rodar a API

- flask run

Para realizar os teste de aceitação basta acessar o próprio navegador:
http://127.0.0.1:5000/

# Registro de Pontos MasterTech API

# Gestão de Usuários

## Criação:

### Post [/users/register]

Executa a operação de criar um novo usuário

- Parâmetros

  - full_name(string) - Nome completo.
  - email(string) - Email.
  - cpf(string) - CPF.

* Response 200 (application/json)

  - Body

          { "message": "success" }

## Consulta:

### Post [/users/[id]]

Executa a operação de consulta dos dados de um usuário com dado id

- Response 200 (application/json)

  - Body

          {
          "id": [id],
          "full_name": "teste",
          "email": "teste@teste"
          "cpf": "TESTE-XXX-XXX",
          }

## Edição:

### Post [/users/edit/[id]]

Executa a operação de edição dos dados de um usuário com dado id

- Parâmetros

  - full_name(string) - Nome completo.
  - email(string) - Email.
  - cpf(string) - CPF.

* Response 200 (application/json)

  - Body

          {
          "id": [id],
          "full_name": "new_teste",
          "email": "new_teste@teste"
          "cpf": "new_TESTE-XXX-XXX",
          }

## Listagem:

### Post [/users/all]

Executa a operação de listagem de todos os usuários

- Response 200 (application/json)

  - Body

          [{
          "id": "user_1,
          "full_name": "new_teste",
          "email": "new_teste@teste"
          "cpf": "new_TESTE-XXX-XXX",
          },
          ...,
          {
          "id": "user_x,
          ...
          }]

# Batidas de Ponto

## Criação:

### Post [/clock/punch/[user_id]]

Cadastra uma batida de ponto para um usuário específico, de acordo com o id [user_id] informado. O controle de sequência é feito automaticamente para entrada e saída.

- Response 200 (application/json)

  - Body

          { "message": "success" }

## Listagem:

### Post [/clock/get_punches/[user_id]

Listagem de todas as batidas de ponto, assim como o total de horas trabalhadas, de um único usuário identificado pelo id [user_id].

- Response 200 (application/json)

  - Body

          {
            "punches": [
                {
                    "exit_type": false,
                    "time": "2020-09-22T17:31:35.498408",
                    "user_id": [id]
                },
                {
                    "exit_type": true,
                    "time": "2020-09-22T17:31:47.302765",
                    "user_id": [id]
                }
            ],
            "total_hours": "0:00:11.804357"
        }
