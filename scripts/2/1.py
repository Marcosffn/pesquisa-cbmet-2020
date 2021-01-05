import pandas as pd
import os

arquivos_path = "/home/marcos/Python/pesquisa/arquivos"

regioes = os.scandir(arquivos_path)

lista = [("campo_grande", "campo_grande"),
         ("campo_grande", "nova_alvorada_do_sul"),
         ("campo_grande", "ribas_do_rio_pardo"),
         ("campo_grande", "bandeirantes"),
         ("campo_grande", "sidrolandia"),
         ("norte", "costa_rica"),
         ("norte", "camapua"),
         ("norte", "sao_gabriel_do_oeste"),
         ("norte", "coxim"),
         ("norte", "pedro_gomes"),
         ("norte", "sonora"),
         ("sudoeste", "bela_vista"),
         ("sudoeste", "porto_murtinho"),
         ("sudoeste", "jardim"),
         ("sudoeste", "bonito"),
         ("grande_dourados", "fatima_do_sul"),
         ("grande_dourados", "maracaju"),
         ("grande_dourados", "dourados"),
         ("grande_dourados", "caarapo"),
         ("grande_dourados", "itapora"),
         ("grande_dourados", "rio_brilhante"),
         ("leste", "ivinhema"),
         ("leste", "nova_andradina"),
         ("leste", "angelica"),
         ("leste", "bataguassu"),
         ("regiao_cone_sul", "iguatemi"),
         ("regiao_cone_sul", "itaquirai"),
         ("regiao_cone_sul", "juti"),
         ("pantanal", "aquidauana"),
         ("pantanal", "miranda"),
         ("pantanal", "corumba"),
         ("pantanal", "nhumirim"),
         ("bolsao", "paranaiba"),
         ("bolsao", "agua_clara"),
         ("bolsao", "santa_rita_do_pardo"),
         ("bolsao", "chapadao_do_sul"),
         ("bolsao", "tres_lagoas"),
         ("bolsao", "brasilandia"),
         ("bolsao", "selviria"),
         ("bolsao", "cassilandia"),
         ("sul-fronteira", "sete_quedas"),
         ("sul-fronteira", "ponta_pora"),
         ("sul-fronteira", "laguna_carapa"),
         ("sul-fronteira", "amambai"),
         ("sul-fronteira", "aral_moreira")]

df = pd.DataFrame(lista, columns=["regiao", "municipio"])

df.to_csv("/home/marcos/Python/pesquisa/scripts/here_we_go_again/regiao_municipio.csv",
          sep=";", index=False)