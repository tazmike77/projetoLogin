# Use a imagem oficial do Python
FROM python:3.8-slim

# Copie os arquivos do projeto para o contêiner
COPY . /app
WORKDIR /app

# Instale as dependências
RUN pip install -r requirements.txt

# Comando para executar a aplicação quando o contêiner for iniciado
CMD ["python", "main.py"]

