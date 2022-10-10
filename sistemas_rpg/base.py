from datetime import datetime
from modulos.updater import update_base

# para mostrar o dia e tempo de atualização
tempo = datetime.now()

# variável que armazenará as bases e seus slots máximos, para depois ser buscada dentro do database, para então ser limpa no sistema_base e transformada na lista de base
base_lista = f'''
{update_base('3° Raikage', 2)}, {update_base('4° Raikage', 1)}, {update_base('Amado', 1)}, {update_base('Boruto', 1)}{update_base('Code', 1)}, {update_base('Darui', 3)}, {update_base('Deepa', 3)}, {update_base('Deidara', 3)}, {update_base('Gaara', 3)}, {update_base('Gengetsu', 3)}, {update_base('Haku', 3)}, {update_base('Hashirama', 1)}, {update_base('Hiruko', 1)}, {update_base('Hiruzen', 2)}, {update_base('Itachi', 2)}, {update_base('Jigen', 1)}, {update_base('Jiraya', 3)}, {update_base('Juugo', 3)}, {update_base('Kabuto', 1)}, {update_base('Kahyo', 2)}, {update_base('Karin', 2)}, {update_base('Kashin Koji', 2)}, {update_base('Kakashi', 2)}, {update_base('Kakuzu', 3)}, {update_base('Kawaki', 1)}, {update_base('Kidoumaru', 3)}, {update_base('Kisame', 3)}, {update_base('Konan', 3)}, {update_base('Naruto', 3)}, {update_base('Madara', 5)}, {update_base('Maito Guy', 2)}, {update_base('Mei Terumi', 2)}, {update_base('Minato', 2)}, {update_base('Muu', 2)}, {update_base('Naruto', 3)}, {update_base('Neji', 5)}, {update_base('Obito', 1)}, {update_base('Orochimaru', 1)}, {update_base('Ranmaru', 3)}, {update_base('Sakon', 3)}, {update_base('Sasori', 2)}, {update_base('Sasuke', 3)}, {update_base('Seikei', 3)}, {update_base('Shin Uchiha', 1)}, {update_base('Shinno', 1)}, {update_base('Shisui', 1)}, {update_base('Shojoji', 3)}, {update_base('Suigetsu', 5)}, {update_base('Tobirama', 1)}, {update_base('Torune', 3)}, {update_base('Tsunade', 2)}, {update_base('Utakata', 3)}, {update_base('Yakumo', 2)}
'''



