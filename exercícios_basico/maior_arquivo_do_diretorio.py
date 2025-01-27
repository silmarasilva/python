# Problema: Liste o maior arquivo dentro de um diretório.

import os

def largest_file_in_dir(directory):
    files = [(f, os.path.getsize(os.path.join(directory, f))) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return max(files, key=lambda x: x[1]) if files else None

print(largest_file_in_dir("."))  # Exemplo: ('example.txt', 1024)

"""

O módulo os fornece funções para interagir com o sistema operacional, como navegar no sistema de arquivos, obter informações de arquivos, entre outras.

A funcão "def largest_file_in_dir(directory)" recebe um parâmetro Diretório (caminho do diretório no qual queremos encontrar o maior arquivo.)

os.listdir(directory) = Lista todos os nomes (arquivos e pastas) presentes no diretório especificado.

s.path.join(directory, f) = Combina o diretório com o nome do arquivo/pasta para formar o caminho completo.

os.path.getsize(os.path.join(directory, f)) = Obtém o tamanho do arquivo (em bytes) no caminho especificado.

Lista de tuplas = Para cada arquivo encontrado no diretório, cria-se uma tupla no formato (nome_do_arquivo, tamanho_em_bytes).

Resultado
Se o diretório contém os arquivos file1.txt, file2.txt e uma pasta subdir, apenas os arquivos serão incluídos na lista:
files = [('file1.txt', 2048), ('file2.txt', 1024)]

Encontrar o maior arquivo = return max(files, key=lambda x: x[1]) if files else None

if files else None = Verifica se a lista files não está vazia. Se não houver arquivos, a função retorna None.

max(files, key=lambda x: x[1]) = Encontra o maior elemento na lista files, comparando o segundo valor de cada tupla (tamanho do arquivo).

lambda x: x[1] = é uma função anônima que retorna o tamanho (segundo elemento da tupla).

"""