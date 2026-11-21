# Loja Fácil – Projeto de E-commerce

## 1. Descrição do projeto

O Loja Fácil é uma aplicação de e-commerce desenvolvida em Python com Flask. O sistema permite visualizar produtos disponíveis na loja e consultar informações de um produto pelo seu identificador.

## 2. Objetivos

- Desenvolver uma aplicação simples de comércio eletrônico.
- Organizar o código e os arquivos do projeto.
- Utilizar Git e GitHub para controle de versão.
- Aplicar práticas de integração e colaboração.

## 3. Funcionalidades iniciais

- Página inicial da loja.
- Listagem de produtos.
- Busca de produto pelo ID.
- Retorno de mensagem de erro quando o produto não é encontrado.

## 4. Tecnologias utilizadas

- Python
- Flask
- Git
- GitHub
- Visual Studio Code

## 5. Estrutura do projeto

```text
projeto-ecommerce/
├── src/
│   └── app.py
├── tests/
├── docs/
├── README.md
├── .gitignore
└── requirements.txt
```

## 6. Como executar o projeto

1. Instale o Python.
2. Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python src/app.py
```

4. Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 7. Estratégia de Git

Foi escolhida a estratégia Gitflow simplificada, utilizando a branch `main` como principal e branches de funcionalidades para desenvolver alterações.

A funcionalidade de busca de produto por ID foi desenvolvida na branch `feature/listar-produtos` e integrada à `main` por meio de Pull Request.

## 8. Equipe e responsabilidades

Projeto desenvolvido individualmente para fins acadêmicos. As responsabilidades de desenvolvimento, testes, documentação e organização do repositório são realizadas pelo estudante.

## 9. Backlog inicial

- [x] Criar página inicial.
- [x] Listar produtos.
- [x] Buscar produto pelo ID.
- [ ] Criar testes automatizados.
- [ ] Configurar integração contínua.
