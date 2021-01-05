import pandas as pd

bolsao_path = "/home/marcos/Python/pesquisa/arquivos/novos/bolsao.csv"

bolsao = pd.read_csv(bolsao_path, sep=";")
bolsao = bolsao.sort_values(by=['DATA (YYYY/MM/DD)'])
fevereiro_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][278:921]
março_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][921:]
abril_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
maio_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
junho_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
julho_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
agosto_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
setembro_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
outubro_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
novembro_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
dezembro_bolsao = bolsao[[
    "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:]
print(bolsao.type())

# campo_grande_path = "/home/marcos/Python/pesquisa/arquivos/novos/campo_grande.csv"
#
# x = pd.read_csv(campo_grande_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# grande_dourados_path = "/home/marcos/Python/pesquisa/arquivos/novos/grande_dourados.csv"
#
# x = pd.read_csv(grande_dourados_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# leste_path = "/home/marcos/Python/pesquisa/arquivos/novos/leste.csv"
#
# x = pd.read_csv(leste_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# norte_path = "/home/marcos/Python/pesquisa/arquivos/novos/norte.csv"
#
# x = pd.read_csv(norte_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# pantanal_path = "/home/marcos/Python/pesquisa/arquivos/novos/pantanal.csv"
#
# x = pd.read_csv(pantanal_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# regiao_cone_sul_path = "/home/marcos/Python/pesquisa/arquivos/novos/regiao_cone_sul.csv"
#
# x = pd.read_csv(regiao_cone_sul_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# sudoeste_path = "/home/marcos/Python/pesquisa/arquivos/novos/sudoeste.csv"
#
# x = pd.read_csv(sudoeste_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
#
# sul_fronteira_path = "/home/marcos/Python/pesquisa/arquivos/novos/sul-fronteira.csv"
#
# x = pd.read_csv(sul_fronteira_path, sep=";")
# janeiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# fevereiro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# março_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# abril_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# maio_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# junho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# julho_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# agosto_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# setembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# outubro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# novembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
# dezembro_bolsao = bolsao[[
#     "DATA (YYYY/MM/DD)", "PRECIPITACÃO TOTAL. HORARIO (mm)"]][:278]
