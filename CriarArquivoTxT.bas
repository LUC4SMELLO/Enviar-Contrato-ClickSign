Attribute VB_Name = "Módulo1"
Public Sub CriarArquivoTxT()
    
    ' DECLARAÇÃO DE VARIÁVEIS
    Dim caminho_arquivo     As String
    Dim email               As String
    Dim nome                As String
    Dim cpf                 As String
    Dim cod_cliente         As String
    Dim cod_vendedor        As String
    Dim numero_arquivo      As Integer
    
    ' CAMINHO DO ARQUIVO
    caminho_arquivo = "C:\Users\IAGO\Desktop\Enviar Contrato\" & "\dados.txt"

    
    ' VALORES DAS LINHAS
    email = Range("H31").Value
    nome = Range("H28").Value
    cpf = Range("H29").Value
    cod_cliente = Range("H4").Value
    cod_vendedor = Range("H16").Value
    
    ' PRÓXIMO ARQUIVO
    numero_arquivo = 1
    
    ' ABRIR ARQUIVO
    Open caminho_arquivo For Output As #numero_arquivo
    
    ' ESCREVER OS DADOS NO ARQUIVO
    Print #numero_arquivo, email
    Print #numero_arquivo, nome
    Print #numero_arquivo, cpf
    Print #numero_arquivo, cod_cliente
    Print #numero_arquivo, cod_vendedor
    
    ' FECHA O ARQUIVO
    Close #numero_arquivo
    
    ' MENSAGEM DE CONFIRMAÇÃO
    MsgBox "Arquivo 'dados.txt' criado com sucesso no caminho: " & caminho_arquivo, vbInformation
    
End Sub
