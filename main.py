
"""
This script was created with the idea of automating the process of uploading CT-es (Electronic Transport Documents) online in the department where I work.
The code will remain open, with some parts replaced, such as the website used for submission, for example.

If you have suggestions for improvements, feel free to contact me below :)

Creator: Guilherme Henrique Alves De Oliveira  
LinkedIn: https://www.linkedin.com/in/guilherme-henrique-205083316?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app  
GitHub: https://github.com/Guilhos22  
Email/Contact: guilherme@guilhoslabs.com.br

best regards,

Guilherme Henrique! 

"""

from time import sleep
from selenium import webdriver
import openpyxl
import pyperclip
from interface.gui import iniciar_interface
from interface.error_pop_up import mostrar_erro_popup

cte_list = []

branch, data_in = iniciar_interface()

def excel_list(sheet):
    for cte in sheet.iter_rows(min_row=2):
        cte_value = str(cte[0].value).strip()
        if cte_value:
            cte_list.append(cte_value)
    if not cte_list:
        mostrar_erro_popup("Error", f'A filial: "{branch}" selecionada está vazia')
        import sys
        sys.exit(1)
    for v in cte_list:      # v == value
        pyperclip.copy(v)
            #print(v) debug
try:
    excel_file_name = "data_base.xlsx".lower()
    excel = openpyxl.load_workbook(excel_file_name)
    sheet_xml = excel[branch]
    excel_list(sheet_xml)
except Exception as excel_error:
    mostrar_erro_popup("Excel Error", f"Não foi possivel encontrar nenhuma planilha '{excel_file_name}' ")
    import sys; sys.exit(1)

if branch == "matriz":
    from branch.fragrance import fragrance
    fragrance(data_in,cte_list)

elif branch == "aromas":
    from branch.aromas import aromas
    aromas(data_in,cte_list)

elif branch == "produção":
    from branch.producao import producao
    producao(data_in,cte_list)


