import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np


# lista de moedas com awesome API
r = requests.get('https://economia.awesomeapi.com.br/json/all')
dict_r = r.json()
lista_moedas = list(dict_r.keys())


# função pegar cotação
def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    data_cotacao_sep = calendario_moeda.get().split('/')
    dia = data_cotacao_sep[0]
    mes = data_cotacao_sep[1]
    ano = data_cotacao_sep[2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?' \
           f'start_date={ano}{mes}{dia}&' \
           f'end_date={ano}{mes}{dia}'
    requisicao = requests.get(link)
    dict_requisicao = requisicao.json()
    valor_cotacao = dict_requisicao[0]['bid']
    label_resultadocotacao['text'] = f'A cotação do {moeda} no dia {data_cotacao} foi de: R${valor_cotacao}'


# função que abre a janela para seleção do arquivo Excel contendo as moedas que quer puxar a cotação
def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione um arquivo em excel para abrir")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo selecionado: {caminho_arquivo}'


# função que gera arquivo Excel com as cotações das moedas contidas no arquivo que você selecionou
def atualizar_cotacoes():
    df = pd.read_excel(var_caminhoarquivo.get())
    moedas = df.iloc[:, 0]  # todas as linhas, coluna indice 0

    data_inicial = calendario_datainicial.get()
    ano_inicial = data_inicial[-4:]
    mes_inicial = data_inicial[3:5]
    dia_inicial = data_inicial[:2]

    data_final = calendario_datafinal.get()
    ano_final = data_final[-4:]
    mes_final = data_final[3:5]
    dia_final = data_final[:2]

    for moeda in moedas:
        link = f'https://economia.awesomeapi.com.br/{moeda}-BRL/100?' \
            f'start_date={ano_inicial}{mes_inicial}{dia_inicial}&' \
            f'end_date={ano_final}{mes_final}{dia_final}'

        requisicao_moeda = requests.get(link)
        cotacoes = requisicao_moeda.json()
        for cotacao in cotacoes:
            timestamp = int(cotacao['timestamp'])
            bid = float(cotacao['bid'])
            data = datetime.fromtimestamp(timestamp)
            data = data.strftime('%d/%m/%Y')
            if data not in df:
                df[data] = np.nan

            df.loc[df.iloc[:, 0] == moeda, data] = bid

        df.to_excel('Moedas.xlsx')
        label_atualizarcotacoes['text'] = f'Arquivo atualizado com sucesso'


# janela do programa
janela = tk.Tk()

janela.title('Sistema de Busca de Cotações de Moedas')

label_cotacaomoeda = tk.Label(text='Buscar cotação de uma única moeda', borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky='NSWE', columnspan=3)

label_selecionarmoeda = tk.Label(text='Selecionar moeda', anchor='e')
label_selecionarmoeda.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky='NSWE')

label_selecionardata = tk.Label(text='Selecionar data', anchor='e')
label_selecionardata.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

calendario_moeda = DateEntry(year=2023, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='NSWE')

label_resultadocotacao = tk.Label(text='')
label_resultadocotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_buscacotacao = tk.Button(text='Buscar Cotação', command=pegar_cotacao)
botao_buscacotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSWE')

# cotação de múltiplas moedas

label_cotacaovariasmoedas = tk.Label(text='Buscar cotações de múltiplas moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSWE', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo em excel com as moedas na coluna A')
label_selecionararquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text='Clique para selecionar', command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky='NSWE')

label_arquivoselecionado = tk.Label(text='Nenhum arquivo selecionado', anchor='e')
label_arquivoselecionado.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky='NSWE')

label_datainicial = tk.Label(text='Data inicial', anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky='NSWE')

calendario_datainicial = DateEntry(year=2023, locale='pt_br')
calendario_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSWE')

label_datafinal = tk.Label(text='Data inicial', anchor='e')
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky='NSWE')

calendario_datafinal = DateEntry(year=2023, locale='pt_br')
calendario_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='NSWE')

botao_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='NSWE')

label_atualizarcotacoes = tk.Label(text='')
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSWE')

janela.mainloop()