import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# URL para servir arquivos estáticos
STATIC_URL = '/static/'

# Diretórios onde o Django irá procurar por arquivos estáticos
STATICFILES_DIRS = [BASE_DIR / "static"]

# Configuração para arquivos de mídia, se aplicável
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Chave secreta
SECRET_KEY = '89e5i$7_=tyal_d4e%c+-*hl(op89*l_*mfmuqx!di*qv-t%0r'

# Debug
DEBUG = False

# Hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Adicionando ROOT_URLCONF
ROOT_URLCONF = 'myproject.urls'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'womakers',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'womakers' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do WSGI
WSGI_APPLICATION = 'myproject.wsgi.application'