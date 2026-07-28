from playwright.sync_api import sync_playwright
import sys
from login import decripto_pass
from interface import mostrar_erro_popup

url = 'https://guilhoslabs.com.br/'


def prod(data_in, cte_list, headless=False):
    browser = None
    try:
        with sync_playwright() as p:
            password, email = decripto_pass()
            

            browser = p.firefox.launch(headless=headless)
            page = browser.new_page()
            page.goto(url)

            page.get_by_role("textbox", name="E-mail").fill(email)
            page.get_by_role("textbox", name="Senha").fill(password)
            page.get_by_role("button", name="Entrar").click()

            page.get_by_role("link", name=" Trocar Empresa").click()
            page.get_by_role("radio", name="ROBERTET DO BRASIL INDUSTRIA E COMERCIO LTDA.-Filial 3 60.888.260/0003-").check()
            page.locator("#send-change-company-usr").click()
            page.get_by_role("button", name="   Q-Drive").click()
            page.get_by_role("menuitem", name="Listar CT-e", exact=True).click()

            for cte in cte_list:
                page.get_by_role("textbox", name="Número da Nota").fill(cte)
                page.get_by_role("button", name=" Buscar").click()
                page.get_by_role("listitem").filter(has_text="Editar Download XML Download").locator("i").click()
                page.get_by_role("link", name="Editar").click()

                campo_data = page.get_by_role("textbox", name="Data de Entrada")
                campo_data.click()
                campo_data.press("Control+a")
                campo_data.press("Backspace")
                campo_data.type(data_in, delay=1)
                page.keyboard.press("Tab")
                page.get_by_role("button", name="Salvar").click()

    ############## Não me orgulho disto aqui, mas sério, NÃO ESTAVA INDO A DATA DO ÚLTIMO CTE MEU DEUS!!!###################
            page.get_by_role("textbox", name="Número da Nota").fill(cte_list[-1])
            page.get_by_role("button", name=" Buscar").click()
            page.get_by_role("listitem").filter(has_text="Editar Download XML Download").locator("i").click()
            page.get_by_role("link", name="Editar").click()

            campo_data = page.get_by_role("textbox", name="Data de Entrada")
            campo_data.click()
            campo_data.press("Control+a")
            campo_data.press("Backspace")
            campo_data.type(data_in, delay=1)
            page.keyboard.press("Tab")

            page.get_by_role("button", name="Salvar").click()

    except Exception as error:
        if "ERR_INTERNET_DISCONNECTED" in str(error):
            mostrar_erro_popup("Erro de Conexão", "Sem acesso à internet. Verifique sua rede e tente novamente.")
            sys.exit(1)
        else:
            mostrar_erro_popup(
                "Erro Grave!",
                "Algum grave erro aconteceu. Tente novamente mais tarde ou entre em contato com o Adm:\n"
                "guilherme@guilhoslabs.com.br\n\n"
                f"{error}"
            )
        sys.exit(1)

