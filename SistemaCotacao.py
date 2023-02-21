import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

janela = tk.Tk()

lista_moedas = ['USD', 'EUR', 'BTC']

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


def pegar_cotacao():
    pass


botao_buscacotacao = tk.Button(text='Buscar Cotação', command=pegar_cotacao)
botao_buscacotacao.grid(row=3, column=2, padx=10, pady=10, sticky='NSWE')


# cotação de múltiplas moedas

label_cotacaovariasmoedas = tk.Label(text='Buscar cotações de múltiplas moedas', borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky='NSWE', columnspan=3)

label_selecionararquivo = tk.Label(text='Selecione um arquivo em excel com as moedas na coluna A')
label_selecionararquivo.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='NSWE')


def selecionar_arquivo():
    pass


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


def atualizar_cotacoes():
    pass


botao_atualizarcotacoes = tk.Button(text='Atualizar cotações', command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='NSWE')

label_atualizarcotacoes = tk.Label(text='')
label_atualizarcotacoes.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky='NSWE')

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='NSWE')

janela.mainloop()