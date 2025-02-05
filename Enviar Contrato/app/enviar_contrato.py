import os
import time

import pyautogui
import pyscreeze
import cv2


informacoes = []

def iterar_sobre_arquivos():
    try:
        with open("dados.txt", "r", encoding= "utf-8") as arquivo:
            for info in arquivo:
                informacoes.append(info.strip())

    except Exception as erro:
        print(f"Erro ao Abrir Arquivo: {erro}")


iterar_sobre_arquivos()


# Lista de Vendedores
dict_vendedores = {
    "13": "Jose Carlos de Paula", 
    "14": "Felipe Alcantara e Silva",
    "33": "Eduardo de Matos Ribeiro",
    "35": "Gabriel Silva Alves",
    "40": "Weverton Junior Cassemiro Guedes",
    "42": "Diego Silva Santos Pinto",
    "45": "Eduardo Aparecido Lima",
    "46": "Jefferson Renan de Carvalho",
    "47": "Danilo Tadeu de Carvalho",
    "48": "Wilian de Assis de Carvalho",
}


# Declaração de variáveis
email_cliente = informacoes[0]
nome_cliente = informacoes[1]
cpf_cliente = informacoes[2]
cod_cliente = informacoes[3]
cod_vendedor = informacoes[4]
caminho_minutas = "O:\VENDAS\Equipamentos\Desenvolvimento\Minutas"


class EnviarContrato:
    def __init__(self, nome, cpf, email, cod_cliente, cod_vendedor):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.cod_cliente = cod_cliente
        self.cod_vendedor = cod_vendedor


    @staticmethod
    def procurar_imagem(imagem, nivel_de_confianca=0.8):
        """Retorna uma tupla com 4 coordenadas da imagem (esquerda, topo, largura, altura)"""
        posicao = pyscreeze.locateOnScreen(
            image=imagem, minSearchTime=10, confidence=nivel_de_confianca
        )
        if posicao:
            return posicao
        else:
            raise pyscreeze.ImageNotFoundException("Imagem não encontrada")


    @staticmethod
    def mover_para_a_imagem(caminho_imagem):
        """Move para a imagem passada como parâmetro"""
        pyautogui.moveTo(
            pyautogui.center(EnviarContrato.procurar_imagem(caminho_imagem))
        )
        time.sleep(0.500)


    @staticmethod
    def mover_para_a_imagem_e_clicar(caminho_imagem):
        """Move para a imagem passada como parâmetro e clica nela"""
        pyautogui.moveTo(
            pyautogui.center(EnviarContrato.procurar_imagem(caminho_imagem))
        )
        time.sleep(0.200)
        pyautogui.click()
        time.sleep(0.500)


    def abrir_clicksign(self):
        pyautogui.hotkey("win")
        time.sleep(0.300)
        pyautogui.write("Chrome")
        pyautogui.hotkey("enter")
        time.sleep(0.800)
        pyautogui.hotkey("win", "up")
        EnviarContrato.mover_para_a_imagem_e_clicar("logo_click_sign.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_adicionar_documentos.png")


    def abrir_explorador_arquivos(self):
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_selecionar.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("do_computador.png")


    def selecionar_contrato(self):
        teste = EnviarContrato.procurar_imagem("explorador_arquivos.png", 0.9)
        pyautogui.moveTo(teste[0] + 300, teste[1] + 15)
        time.sleep(0.300)
        pyautogui.write(caminho_minutas)
        pyautogui.hotkey("enter")
        EnviarContrato.mover_para_a_imagem_e_clicar("pesquisar_em_minutas.png")
        pyautogui.write(self.cod_cliente)
        EnviarContrato.mover_para_a_imagem_e_clicar("contrato_pdf_logo.png")
        pyautogui.doubleClick()


    def adicionar_signatario_existente(
        self, nome_signatario: str, tipo_assinatura: str
        ):

        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("signatario_da_agenda.png")
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("buscar_contato_agenda.png")
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("del")
        time.sleep(0.300)
        pyautogui.write(nome_signatario)
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("check_box_laranja.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_avancar.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("campo_como_signatario_deve_assinar.png")
        pyautogui.write(tipo_assinatura)
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("check_box_laranja.png")
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_adicionar.png")


    def adicionar_signatario_novo(self, tipo_assinatura: str):
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("signatario_novo.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("campo_digitar_email.png")
        pyautogui.write(self.email)
        EnviarContrato.mover_para_a_imagem_e_clicar("campo_digitar_nome.png")
        pyautogui.write(self.nome)
        EnviarContrato.mover_para_a_imagem_e_clicar("campo_digitar_cpf.png")
        pyautogui.write(self.cpf)
        time.sleep(0.500)
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_alterar_autenticacoes.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("selfie_com_documentos.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_alterar.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_avancar.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("campo_como_signatario_deve_assinar.png")
        pyautogui.write(tipo_assinatura)
        time.sleep(0.750)
        EnviarContrato.mover_para_a_imagem_e_clicar("check_box_laranja.png")
        EnviarContrato.mover_para_a_imagem_e_clicar("botao_adicionar.png")
