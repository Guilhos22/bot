from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import pyperclip, sys
from time import sleep
from login import decripto_pass
from interface import mostrar_erro_popup




def producao(data_in, cte_list):
    browser = None
    try:
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 22)
        browser.get('https://guilhoslabs.com.br/') # <- visit haha 
        browser.maximize_window()
        password, email = decripto_pass()
        wait.until(EC.element_to_be_clickable((By.ID, "UserName"))).send_keys(email)
        wait.until(EC.element_to_be_clickable((By.ID, "Password"))).send_keys(password)
        
        
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "user-change-context"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='63d9553fbb611d17f84f7262']"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "send-change-company-usr"))).click()

        sleep(1) 
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                               "//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'dropdown-toggle')]"))).click()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@title='Conhecimento de Transporte Eletrônico']"))).click()
        pyperclip.copy(cte_list[0])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Número da Nota']"))).send_keys(
            Keys.CONTROL, 'v')
        search_btn = wait.until(EC.element_to_be_clickable((By.ID, "searchData")))
        browser.execute_script("arguments[0].click();", search_btn)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-ellipsis-v']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='lnk-grid edit-cte']"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(Keys.CONTROL, 'a')
        wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(Keys.BACKSPACE)
        wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(data_in)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-bb-handler='save']"))).click()

        for v in cte_list[1:]:
            pyperclip.copy(v)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Número da Nota']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Número da Nota']"))).send_keys(
                Keys.CONTROL, 'a')
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Número da Nota']"))).send_keys(
                Keys.BACKSPACE)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Número da Nota']"))).send_keys(
                Keys.CONTROL, 'v')
            search_btn = wait.until(EC.element_to_be_clickable((By.ID, "searchData")))
            browser.execute_script("arguments[0].click();", search_btn)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-ellipsis-v']"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='lnk-grid edit-cte']"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(Keys.CONTROL, 'a')
            wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(Keys.BACKSPACE)
            wait.until(EC.element_to_be_clickable((By.ID, "DateEntry"))).send_keys(data_in)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-bb-handler='save']"))).click()
            
        sleep(2)



    except WebDriverException as error:
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
    finally:
        
        if browser:
            browser.quit()