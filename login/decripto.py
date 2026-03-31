import keyring
import sys
from interface import mostrar_erro_popup

_SERVICE = "AquamarineBot"



def decripto_pass():
    try:

        if isinstance(keyring.get_keyring(), keyring.backends.fail.Keyring):
            raise RuntimeError("Backend de cofre de senhas inseguro ou inexistente no SO.")

        senha = keyring.get_password(_SERVICE, "password")
        email = keyring.get_password(_SERVICE, "email")

        if not senha or not email:
            from interface import solicitar_credenciais
            salvo = solicitar_credenciais()
            if not salvo:
                sys.exit(0)

            senha = keyring.get_password(_SERVICE, "password")
            email = keyring.get_password(_SERVICE, "email")
            
        return senha, email

    except Exception as error:

        mostrar_erro_popup("Erro de Segurança", "Falha na integridade do cofre de credenciais. Acesso negado.")
        sys.exit(1)


if __name__ == "__main__":
    decripto_pass()