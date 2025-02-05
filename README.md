# **Sistema de Envio de Contratos de Comodatos**

## **Descrição**

O código "refaz" os passos de como alguem enviaria o contrato pelo clicksign, de uma forma mais rápida e com muito menos sucessão a falhas. Ele usa imagens para se localizar em vez de pontos fixos na tela.

Para criar um novo signatario ele usa o arquivo "dados.txt" que vem de uma planiha excel externa, ele é gerado junto com o contrato e vem direto para a pasta do código.


---

## **Funcionalidades**

- *iterar_sobre_arquivos()*
- *procurar_imagem()*
- *mover_para_a_imagem()*
- *mover_para_a_imagem_e_clicar()*
- *abrir_clicksign()*
- *abrir_explorador_arquivos()*
- *selecionar_contrato()*
- *adicionar_signatario_existente()*
- *adicionar_signatario_novo()*

---

## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **PyAutoGUI 0.9.54**
- **PyScreeze 0.1.30**
- **Opencv-Python 4.9.0.80**

---

## **Estrutura do Projeto**

```
.
├── app
│   ├── enviar_contrato.py
│   └── main.py
│
├── botao_adicionar_documentos.png
├── botao_adicionar.png
├── botao_alterar_autenticacoes.png
├── botao_alterar.png
├── botao_avancar.png
├── botao_selecionar.png
├── buscar_contato_agenda.py
├── campo_como_signatario_deve_assinar.png
├── campo_digitar_cpf.png
├── campo_digitar_email.png
├── campo_digitar_nome.png
├── check_box_laranja.png
├── contrato_pdf_logo.png
├── do_computador.png
├── explorador_arquivos.png
├── logo_click_sign.png
├── pesquisar_em_minutas.png
├── selfie_com_documentos.png
├── signatario_da_agenda.png
├── signatario_novo.png
|
├── dados.txt
├── README.md
```

---

## **Como Executar**

1. Acesse o arquivo `main.py`.
2. Execute o programa:
   ```bash
   python main.py
   ```

___


## **Autoria**
- Lucas Pereira Silva Mello

<br>

Fique à vontade para contribuir!
