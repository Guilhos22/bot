from cryptography.fernet import Fernet
from interface import mostrar_erro_popup
import os

def decripto_pass():
    try:
        base_dir = os.path.dirname(__file__) 
        key_path = os.path.join(base_dir, "your.key") 

        with open(key_path, 'rb') as arq:
            key = arq.read()
        fernet = Fernet(key)
        pass_cripto = b"cripto_password" # <- example
        mail_cripto = b'cripto_mail' # <- example
        decripto_senha = fernet.decrypt(pass_cripto)
        decripto_email = fernet.decrypt(mail_cripto)
        
        return decripto_senha.decode(), decripto_email.decode()
    
    except Exception as error:
        mostrar_erro_popup("Error" f"Erro grave ao tentar ler e descriptografar a senha. Por favor, entre em contato com o adm: guilherme@guilhoslabs.com.br\n guilherme.oliveira@robertet.com \n {error}")