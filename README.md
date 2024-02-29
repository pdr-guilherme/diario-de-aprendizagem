# Diário de Aprendizagem

Este é um aplicativo web feito com Python e Django que permite que os usuários criem tópicos e adicionem entradas sobre cada tópico, além de contar com criação e autenticação básica de usuários.

## Instalação / Uso

Para executar o Diário de Aprendizagem em seu ambiente local, siga estas instruções:

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/pedrogs07/diario-de-aprendizagem.git
   ```

2. **Navegue até o Diretório:**

   ```bash
   cd diario-de-aprendizagem
   ```

3. **Instale as Dependências:**
   É recomendável criar um ambiente virtual Python para este projeto. Após ativá-lo, instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar as Migrações:**
   Execute as migrações do Django para configurar o banco de dados SQLite:

   ```bash
   python manage.py migrate
   ```

5. **Inicie o Servidor de Desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

6. **Acesse o Aplicativo:**
   Abra um navegador da web e acesse um dos seguintes endereços:
   ```
   http://127.0.0.1:8000/
   http://localhost:8000/
   ```

Agora você pode começar a usar o Diário de Aprendizagem para registrar suas experiências de aprendizado, definir metas e acompanhar seu progresso!
