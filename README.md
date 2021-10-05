# Manual da API
Aplicação para armazenar e registrar cartões de vacinação  utilizando SQLAlchemy, Dataclass, Blueprint, Migrations e Padrão Flask Factory.

## Cadastrar cartão do usuário:
POST http://{BASE_URL}/api/vaccination

```json
{
    "cpf": "32132132100",
    "name": "Humberto Silva",
    "vaccine_name": "Coronavac",
    "health_unit_name": "Santa Madalena"
}

```
#

## Ver todos os cartões:
GET http://{BASE_URL}/api/vaccination

```json
[
  {
    "cpf": "32132132100",
    "name": "Humberto Silva",
    "first_shot_date": "Fri, 10 Sep 2021 00:00:00 GMT",
    "second_shot_date": "Thu, 09 Dec 2021 00:00:00 GMT",
    "vaccine_name": "Coronavac",
    "health_unit_name": "Santa Madalena"
  },
  {
    "cpf": "12312312300",
    "name": "Matheus Humberto",
    "first_shot_date": "Fri, 11 Sep 2021 00:00:00 GMT",
    "second_shot_date": "Thu, 10 Dec 2021 00:00:00 GMT",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
  },
]

```
#
