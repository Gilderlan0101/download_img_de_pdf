# download_img_de_pdf

# Baixar Imagens de PDF

## Sobre
Este projeto é uma aplicação web desenvolvida em Flask que permite aos usuários converter arquivos PDF com imagens para um formato ZIP contendo todas as imagens extraídas de cada página do PDF. Utilizando a biblioteca PyPDF2 e PIL para manipulação de imagens, a aplicação oferece uma solução prática para quem precisa extrair imagens de documentos PDF.

## Funcionalidades
- **Upload de arquivos PDF**: O usuário pode enviar um arquivo PDF.
- **Extração de imagens**: As imagens de cada página do PDF são extraídas e convertidas para PNG.
- **Download do ZIP**: O resultado é um arquivo ZIP contendo todas as imagens convertidas.

## Como Usar
1. **Pré-requisitos**:
   - Certifique-se de ter Python 3 instalado.
   - Crie e ative um ambiente virtual:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
     ```

2. **Instalar dependências**:
   - Após ativar o ambiente virtual, instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuração**:
   - Certifique-se de que o arquivo `.env` está configurado corretamente:
     ```bash
     FLASK_APP=run.py
     ```

4. **Iniciar a aplicação**:
   - Com o ambiente virtual ativado, inicie o servidor Flask:
     ```bash
     flask run
     ```

5. **Acessar a aplicação**:
   - Abra seu navegador e vá para `http://127.0.0.1:5000/`.

## Como Contribuir
Se você deseja contribuir para este projeto, sinta-se à vontade para abrir uma pull request. Sinta-se livre para sugerir melhorias, relatar problemas ou enviar modificações.

## Licença
Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
- Gilderlan: [GitHub](https://github.com/Gilderlan0101)
- Email: [dacruzgg01gmail.com](mailto:dacruzgg01@gmail.com)
