# 🤖 Bot de Automação de CT-e

## 📌 Descrição (PT-BR)

Este é um projeto de um bot de automação desenvolvido com o objetivo de facilitar o lançamento de CT-e's (Conhecimentos de Transporte Eletrônico) em um sistema web interno, utilizando como parâmetros a **filial** e a **data**.

O código foi pensado especificamente para o ambiente onde trabalho, porém permanecerá **aberto e livre**, para que qualquer pessoa possa visualizar, sugerir melhorias ou utilizá-lo como base para outros projetos.  
> ⚠️ Vale ressaltar que o uso prático deste código por terceiros é limitado, pois ele foi feito para interagir com um site muito específico, com comportamentos particulares.

Sinta-se à vontade para explorar o código-fonte (`src`) e enviar sugestões!

---

## 🚀 Como usar

Há duas formas principais de utilizar o projeto:

### 1. Executando com Python diretamente
Você pode instalar as dependências via "requirements.txt" e rodar o script com Python:

pip install -r requirements.txt
python3 main.py

⚠️ Não recomendado para uso em produção com pessoas não técnicas, pois requer instalação do Python e familiaridade com terminal ou algum editor de codigo, como VIM, Vscode, Pycharm etc!

### 2. Utilizando um executável (.exe)

A forma mais indicada é gerar um binário .exe usando PyInstaller:
pyinstaller --onefile --noconsole main.py

Dessa forma, qualquer pessoa poderá rodar o bot sem precisar instalar nada.
Obs: a compatibilidade com sistemas Unix-like ainda será implementada no futuro (pode haver problemas devido ao uso de .xlsx como base de dados).

⚠️ Observações
    Como o executável é gerado localmente e sem assinatura digital, alguns antivírus/EDRs como Windows Defender ou SentinelOne podem gerar alertas iniciais. Isso ocorre pelo tamanho do binário e pela inclusão do interpretador Python embutido.
    Após análise, a maioria dos AVs reconhece o arquivo como legítimo.
    Bugs e falhas podem ocorrer. Em caso de erro grave, a própria aplicação mostra o contato do administrador. Para melhorias, há um link na interface gráfica que leva ao GitHub deste projeto.


📬 Contribuições
Mesmo que eu não esteja mais na empresa futuramente, o código continuará open-source para quem herdar a função ou quiser contribuir com melhorias.

###############################


📌 Description (EN)

This is a CT-e automation bot project, developed to simplify the process of submitting transport documents (CT-e) to a specific internal web system, using branch and date as parameters.

The code was tailored for my workplace environment, but it will remain open-source, allowing anyone to explore, suggest improvements, or adapt it for other contexts.

    ⚠️ Please note: practical usage outside of my organization is unlikely, as the automation targets a specific and customized web platform.

Feel free to explore the src and contribute!
🚀 How to use

There are two main ways to run this project:
1. Run with Python directly

Install dependencies from requirements.txt and run the script:

pip install -r requirements.txt
python main.py

    ⚠️ Not ideal for production use by non-technical users, as it requires Python and basic CLI knowledge.

2. Build an executable (.exe)

The preferred method is compiling the script using PyInstaller:

pyinstaller --onefile --noconsole main.py

This allows anyone to run the bot without installing Python.
Note: Compatibility with Unix-like systems will be added later, though .xlsx usage might cause issues.
⚠️ Notes

    As the binary is unsigned and generated locally, security tools like Windows Defender or SentinelOne may flag it initially. This is expected and due to Python interpreter being bundled in the .exe.
    After analysis, most AVs mark it as safe.

    Bugs may exist. In case of major issues, the GUI will show the administrator's contact. For improvements, the GUI also includes a link to this GitHub repository.

🤝 Contributions

Even if I leave the company, this project will remain open-source for others to improve or use in the future.
