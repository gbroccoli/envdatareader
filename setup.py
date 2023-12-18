from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='EnvUtil',  # Замените на имя вашего пакета
    version='1.0',  # Замените на вашу версию
    packages=[''],  # Укажите пустой список, так как у вас только один файл
    py_modules=['EnvUtil'],  # Замените на имя вашего файла с классом
    python_requires='>=3.6',  # Укажите версию Python
    install_requires=[
        'python-dotenv',
    ],
    author='hBroccoli',
    author_email='vovo.r@yandex.ru',
    description='EnvUtil - это библиотека на Python для управления переменными окружения в приложениях. Она предоставляет удобный интерфейс для загрузки переменных окружения из файлов .env с использованием библиотеки python-dotenv. С помощью EnvManager вы можете легко и безопасно управлять конфигурацией вашего приложения, храня чувствительные данные, такие как ключи API или настройки, в файле .env и использовать их в вашем коде.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HermitBroccoli/EnvManager',
    license='MIT', 
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
