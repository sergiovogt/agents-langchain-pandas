# Desarrollo e Implementación de Agentes de LangChain con Streamlit, para análisis de datos Excel o CSV
Basado en el tutorial de Agentes Pandas de [LangChain](https://python.langchain.com/docs/integrations/toolkits/pandas)


## Requerimientos
- [OpenAI API key](https://platform.openai.com/)

## Installation

#### 1. Clonar el repositorio

```bash
git clone https://github.com/sergiovogt/agents-langchain-pandas.git
```

#### 2. Crear el entorno

``` bash
cd agents-langchain-pandas
python -m venv env
source env/bin/activate
```

#### 3. Instalar las dependencias requeridas
``` bash
pip install -r requirements.txt
```

Primero, crear el archvio `.env` en el directorio raiz del proyecto. Dentro del archvio, agreagar la API Key de OpenAI:

```makefile
OPENAI_API_KEY="agregar_aquí_la_apikey"
```

Guardar el archivo y cerrarlo. En el script de Python, cargar el archivo `.env` usando el siguiente código (ya está cargado en [frontend.py]:
```python
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```

Ahora tu entorno de Python está listo! ya puedes continuar...

## Tutoriales
Para ver más tutoriales, podés visitar mi canal de YouTube:  [youtube.com/@sergiovogtds1998](https://youtube.com/@sergiovogtds1998)
