# FastAPI - CRUD Simples

![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/Uvicorn-%23D42029.svg?style=for-the-badge&logo=gunicorn&logoColor=white)


Uma API simples para exemplificar o uso de [FastAPI](https://www.fastapi.tiangolo.com/) realizando um CRUD de um menu de uma cafeteria e servindo os dados usando [Uvicorn](https://www.uvicorn.org/).

- menu.py: contém os dados do menu da cafeteria
- api.py: contém a API com suas rotas e BaseModels para o CRUD
- scripts.py: contém os códigos para executar o servidor


## Instalação

```sh
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Como usar

- **Desenvolvimento**

  ```sh
  $ python script.py -dev
  ```

- **Produção**
  ```sh
  $ python script.py -start
  ```

Após o servidor iniciar, acesse a URL: http://localhost:8000/docs/ para visualizar o documentação.