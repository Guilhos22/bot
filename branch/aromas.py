from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep
from login import decripto_pass
from interface import mostrar_erro_popup
senha, email = decripto_pass()

def aromas(data_in,cte_list):

    
    try:
        browser = webdriver.Chrome()
        browser.get('https://www.pudim.com.br/') # <- i love this site hahaha (it's example!)
        browser.maximize_window()

        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID, "UserName")))
        browser.find_element(By.ID, "UserName").send_keys(email)

        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID, "Password")))
        browser.find_element(By.ID, "Password").send_keys(senha)

        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID, "login-button")))
        browser.find_element(By.ID, "login-button").click()
        
        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID, "user-change-context")))
        browser.find_element(By.ID, "user-change-context").click()



        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@value='63d954fabb611d17f84f71f1']"))) #
        browser.find_element(By.XPATH, "//input[@value='63d954fabb611d17f84f71f1']").click()

        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.ID, "send-change-company-usr")))
        browser.find_element(By.ID, "send-change-company-usr").click()


        sleep(1)
        # WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'dropdown-toggle')]" ))) this is not working, and i dont know why ;-;
        browser.find_element(By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-default') and contains(@class, 'dropdown-toggle')]").click() 

        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@title='Conhecimento de Transporte Eletrônico']")))        
        browser.find_element(By.XPATH, "//*[@title='Conhecimento de Transporte Eletrônico']").click()

        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Número da Nota']")))  
        browser.find_element(By.XPATH, "//input[@placeholder='Número da Nota']").send_keys(Keys.CONTROL, 'v')


        browser.find_element(By.ID, "searchData").click()

        WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH, "//i[@class='fa fa-ellipsis-v']")))
        browser.find_element(By.XPATH, "//i[@class='fa fa-ellipsis-v']").click()
        browser.find_element(By.XPATH, "//a[@class='lnk-grid edit-cte']").click()

        
        WebDriverWait(browser,2).until(EC.presence_of_element_located((By.ID, "DateEntry")))
        browser.find_element(By.ID, "DateEntry").click()
        browser.find_element(By.ID, "DateEntry").send_keys(Keys.CONTROL, 'a')
        browser.find_element(By.ID, "DateEntry").send_keys(Keys.BACKSPACE)
        browser.find_element(By.ID, "DateEntry").send_keys(data_in)
        browser.find_element(By.XPATH,"//button[@data-bb-handler='save']").click()
        sleep(1)

        for i,v in enumerate(cte_list[1:], start=2):
                pyperclip.copy(v)
                WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Número da Nota']")))  
                browser.find_element(By.XPATH, "//input[@placeholder='Número da Nota']").send_keys(Keys.CONTROL, 'a')
                browser.find_element(By.XPATH, "//input[@placeholder='Número da Nota']").send_keys(Keys.BACKSPACE)
                browser.find_element(By.XPATH, "//input[@placeholder='Número da Nota']").send_keys(Keys.CONTROL, 'v')
                browser.find_element(By.ID, "searchData").click()
                WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH, "//i[@class='fa fa-ellipsis-v']")))
                browser.find_element(By.XPATH, "//i[@class='fa fa-ellipsis-v']").click()
                browser.find_element(By.XPATH, "//a[@class='lnk-grid edit-cte']").click()
                WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, "DateEntry")))
                browser.find_element(By.ID, "DateEntry").click()
                browser.find_element(By.ID, "DateEntry").send_keys(Keys.CONTROL, 'a')
                browser.find_element(By.ID, "DateEntry").send_keys(Keys.BACKSPACE)
                browser.find_element(By.ID, "DateEntry").send_keys(data_in)
                browser.find_element(By.XPATH,"//button[@data-bb-handler='save']").click()
                sleep(1)
    except Exception as error:
         mostrar_erro_popup("Error", f"Algum grave erro aconteceu. Tente novamente mais tarde, ou entre em contato com o Adm: guilherme@guilhoslabs.com.br\n\n{error}")

    browser.quit()