import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

#  construir as funcionalidadades
# @app.route('/vendas')
# def homepage():
#     return "A API está no ar"
#
# @app.route('/erro')
# def pegarvendas():
#     tabela = pd.read_csv('advertising.csv')
#     total_vendas = tabela['Vendas'].sum()
#     resposta = {'total_vendas':total_vendas}
#
#     return jsonify(resposta)
#
# # rodar a nossa api
# app.run(host='0.0.0.0')



# tabela = pd.read_csv('advertising.csv')
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)