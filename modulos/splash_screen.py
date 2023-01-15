from time import sleep
from modulos.info import *


def splash_screen(segundos = 3):
    print(f'''一 ◇───────◇
    - {name} {version}({date_version})
    •{objective}
''')

    sleep(segundos)
    return

    