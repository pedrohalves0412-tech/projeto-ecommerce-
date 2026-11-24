terraform {
  required_version = ">= 1.4.0"
}

variable "replicas" {
  type    = number
  default = 1
}

resource "terraform_data" "loja_facil" {
  input = {
    aplicacao = "Loja Facil"
    imagem    = "loja-facil:1.0"
    porta     = 5000
    replicas  = var.replicas
    ambiente  = "desenvolvimento"
  }
}

output "infraestrutura" {
  value = terraform_data.loja_facil.output
}