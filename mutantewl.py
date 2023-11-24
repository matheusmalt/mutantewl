import json
import sys

banner = '''
__  __        _                _              __      __ _    
|  \/  | _  _ | |_  __ _  _ _  | |_  ___       \ \    / /| |   
| |\/| || || ||  _|/ _` || ' \ |  _|/ -_)       \ \/\/ / | |__ 
|_|  |_| \_._| \__|\__/_||_||_| \__|\___|        \_/\_/  |____|

Autor: Matheus Malta
Linkedin: https://www.linkedin.com/in/matheus-malta-contato/
GitHub: https://github.com/matheusmalt/
Version: 1.0
'''
print(banner)

try:
    wordlist = sys.argv[1]
    wordlist_mutante = sys.argv[2]
except IndexError:
    print("( *,_*,)")
    print("Por favor, forneça os argumentos corretos:")
    print("Exemplo: python3 mutantewl.py wl.txt wlmutante.txt")
    sys.exit(1)

def leet_speak(senha, leet_dict):
    return ''.join(leet_dict.get(c.upper(), c) for c in senha)

def case_variations(senha):
    return [senha.lower(), senha.upper(), senha.capitalize()]

def uppercase(senha):
    variacoes = []
    for i in range(len(senha)):
        if senha[i].isalpha():
            mutated_word = senha[:i] + senha[i].upper() + senha[i+1:]
            variacoes.append(mutated_word)
    return variacoes

def add_suffix_prefix(senha, prefixos, sufixos):
    wordlist_mutacao = []
    for prefi in prefixos:
        senha_prefixo = prefi + senha
        wordlist_mutacao.append(senha_prefixo)
    for sufi in sufixos:
        senha_sufixo = senha + sufi
        wordlist_mutacao.append(senha_sufixo)
    return wordlist_mutacao

def escrever_em_arquivo(senhas, wordlist_mutante):
    with open(wordlist_mutante, 'w') as file:
        for senha in senhas:
            file.write(f"{senha}\n")

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    leet_dict = config['leet_dict']
    prefixos = config['prefixos']
    sufixos = config['sufixos']

wordlist_mutacao = set()  # Armazenar senhas mutadas em um conjunto para evitar duplicatas
with open(wordlist, 'r') as file:
    for line in file:
        senha = line.strip()
        # Adicionando senhas mutadas ao conjunto
        wordlist_mutacao.add(leet_speak(senha, leet_dict))
        wordlist_mutacao.update(case_variations(senha))
        wordlist_mutacao.update(uppercase(senha))
        wordlist_mutacao.update(add_suffix_prefix(senha, prefixos, sufixos))

# Convertendo para lista apenas no momento de escrita no arquivo
wordlist_mutacao = list(wordlist_mutacao)

# Escrevendo senhas mutadas no arquivo
escrever_em_arquivo(wordlist_mutacao, wordlist_mutante)
print(f"[!] Número de senhas geradas após mutações: {len(wordlist_mutacao)}")
