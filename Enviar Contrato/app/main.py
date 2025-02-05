from enviar_contrato import (
    EnviarContrato,
    dict_vendedores,
    nome_cliente,
    cpf_cliente,
    email_cliente,
    cod_cliente,
    cod_vendedor,
)


cliente1 = EnviarContrato(nome_cliente, cpf_cliente, email_cliente, cod_cliente, cod_vendedor)
cliente1.abrir_clicksign()
cliente1.abrir_explorador_arquivos()
cliente1.selecionar_contrato()
cliente1.adicionar_signatario_existente(nome_signatario="Distribuidora", tipo_assinatura="Comodante")
cliente1.adicionar_signatario_existente(
    nome_signatario= dict_vendedores[cod_vendedor],
    tipo_assinatura= "Testemunha"
)
cliente1.adicionar_signatario_novo(tipo_assinatura="Comodat")
