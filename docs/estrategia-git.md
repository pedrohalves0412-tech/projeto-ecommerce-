# Estratégia de Git – Loja Fácil

## Estratégia escolhida

Foi adotado um fluxo de trabalho baseado em branches de funcionalidades, utilizando uma versão simplificada do Gitflow.

A branch `main` contém a versão principal do projeto. Novas funcionalidades são desenvolvidas em branches separadas.

## Justificativa

Essa estratégia foi escolhida porque facilita a organização das alterações, permite revisar o código antes da integração e reduz o risco de modificar diretamente a versão principal.

## Fluxo utilizado

1. Criação do repositório no GitHub.
2. Criação da branch `feature/listar-produtos`.
3. Desenvolvimento da funcionalidade de busca de produtos por ID.
4. Registro da alteração utilizando Conventional Commits.
5. Envio da branch ao GitHub.
6. Abertura do Pull Request #1.
7. Integração da funcionalidade à branch `main`.

## Padronização dos commits

Foram utilizados os padrões `chore`, `feat` e `docs`, seguindo a convenção Conventional Commits.

## Responsabilidades

O desenvolvimento, a organização do repositório, a documentação e a integração das alterações foram realizados individualmente.