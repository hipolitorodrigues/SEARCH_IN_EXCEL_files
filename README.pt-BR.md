<div align="center">
   <img height="30" width="40" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-ico.svg">
   <a href="./README.md">
      <img height="30" width="120" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-en.svg">
   </a>
   <a href="./README.pt-BR.md">
      <img height="30" width="60" src="https://github.com/hipolitorodrigues/assets-for-github/blob/985021e61af3982fd9f28be446b106b958f24696/images/01/img-readme-pt-br.svg">
   </a>
</div>

# Search in Excel Files

## Sobre o Projeto

O **Search in Excel Files** é uma aplicação desktop desenvolvida em **Python 3.13.1** utilizando a biblioteca **Tkinter** para a interface gráfica. Seu objetivo é permitir que o usuário carregue múltiplos arquivos **.xlsx** e realize buscas em todas as suas planilhas, exibindo os resultados de forma organizada.

![alt text](https://github.com/hipolitorodrigues/assets-for-github/blob/d34a7a288e52f24ee194872375c59bf88b02abc6/images/01/screenshot-02.png)

## Funcionalidades

- **Carregar vários arquivos Excel (.xlsx) simultaneamente**
- **Buscar um termo em todas as planilhas de todos os arquivos carregados**
- **Exibir os resultados formatados na interface gráfica**
- **Interface responsiva e de fácil utilização**

## Tecnologias Utilizadas

- **Python 3.13.1**
- **Tkinter** - Interface gráfica
- **Pandas** - Manipulação de dados dos arquivos Excel
- **Pyinstaller** - Criação da versão exe portátil

## Como Executar

**MODO 1**
1. Certifique-se de ter o Python 3.13.1 instalado.
2. Instale as dependências necessárias executando:
   ```sh
   pip install pandas openpyxl tk
   ```
3. Execute o aplicativo com o comando:
   ```sh
   python main.py
   ```
**MODO 2**
1. Abra a pasta `portable_exe_version`.
2. Dois cliques no exe portátil `Search_in_Excel_Files.exe`.

## Como Utilizar

1. **Abrir o aplicativo** - Execute o script `main.py` ou o exe portátil `Search_in_Excel_Files.exe`.
2. **Carregar arquivos** - Clique no botão **"Load Excel Files"** e selecione os arquivos desejados.
3. **Realizar uma busca** - Digite um termo no campo de busca e clique no botão **"Search"**.
4. **Visualizar resultados** - Os resultados serão exibidos na área de texto da interface, indicando:
   - O arquivo onde o termo foi encontrado
   - A planilha correspondente
   - A linha contendo o termo encontrado

## Estrutura do Código

O projeto segue os princípios **SOLID**, utilizando o padrão **MVC (Model-View-Controller)**:

- **Model:** Classe `ExcelSearchApp`, que gerencia os arquivos carregados e a lógica de busca.
- **View:** Módulo `create_widgets()`, que define os elementos da interface gráfica.
- **Controller:** Métodos `load_files()` e `search()`, que lidam com as interações do usuário e a busca nos arquivos.

## Possíveis Melhorias Futuras

- Adição de suporte para arquivos **.csv** e **.xls**.
- Opção de exportar os resultados da busca para um arquivo de texto ou Excel.
- Melhorias na interface utilizando **ttk** para um design mais moderno.

## Autor

- **Desenvolvedor**: Hipolito Rodrigues
- **Data de Criação**: 04/02/2025
- **Última Atualização**: 06/02/2025
- **Versão Atual**: 0.94

---

## License

Este projeto está licenciado sob a Licença MIT. Isso significa que você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do software, desde que mantenha o aviso de copyright original e a licença incluídos em todas as cópias ou partes substanciais do software.
