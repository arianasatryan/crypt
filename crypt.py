import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from AES import AESCipher
from Crypto import Random

files_path = '/home/lab6/Desktop/cryptography/open_database'
encrypted_database_path = '/home/lab6/Desktop/cryptography/encrypted_database'
files = os.listdir(files_path)


def read(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8')as fin:
        text = fin.read()
    return text


def remove_stopwords(text: str) -> str:
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words('english')]
    return ''.join(tokens_without_sw)


def key_gen():
    rndfile = Random.new()
    return rndfile.read(16)


for file in files:
    open_text = read(os.path.join(files_path, file))
    open_text = remove_stopwords(open_text)
    key = 'This is a key123'
    encrypter = AESCipher(key)
    encrypted_text = encrypter.encrypt(open_text)
    print(encrypted_text)





