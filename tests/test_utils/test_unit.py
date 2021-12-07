import pytest
from rest_framework.exceptions import ValidationError

from utils.validators import cnpj_validator, cpf_validator

def test_cnpj_caminho_feliz():
  assert cnpj_validator('58060621000140') == None

def test_cnpj_tamanho_certo_valor_errado():
  with pytest.raises(ValidationError):
    assert cnpj_validator('12345678910111') == None

def test_cnpj_tamanho_errado():
  with pytest.raises(ValidationError):
    assert cnpj_validator('1234567891011') == None

def test_cnpf_com_um_algarismo():
  with pytest.raises(ValidationError):
    assert cnpj_validator('22222222222222') == None

def test_cpf_caminho_feliz():
  assert cpf_validator('42246244005') == None

def test_cpf_tamanho_certo_valor_errado():
  with pytest.raises(ValidationError):
    assert cpf_validator('12345678910') == None

def test_cpf_tamanho_errado():
  with pytest.raises(ValidationError):
    assert cpf_validator('123456789') == None

def test_cpf_com_um_algarismo():
  with pytest.raises(ValidationError):
    assert cpf_validator('22222222222') == None
