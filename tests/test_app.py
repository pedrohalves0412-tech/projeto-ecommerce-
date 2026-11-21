
from src.app import app

def test_pagina_inicial():
    cliente = app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert b"Loja" in resposta.data

def test_listar_produtos():
    cliente = app.test_client()
    resposta = cliente.get("/produtos")
    assert resposta.status_code == 200
    assert len(resposta.get_json()) == 3

def test_buscar_produto():
    cliente = app.test_client()
    resposta = cliente.get("/produtos/1")
    assert resposta.status_code == 200
    assert resposta.get_json()["nome"] == "Notebook"

def test_produto_inexistente():
    cliente = app.test_client()
    resposta = cliente.get("/produtos/999")
    assert resposta.status_code == 404
