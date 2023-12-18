from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='envfetch',
    version='2.0',
    packages=['envfetch'],  # Указываем папку с вашими модулями
    python_requires='>=3.6',
    install_requires=[
        'python-dotenv',
    ],
    author='hBroccoli',
    author_email='vovo.r@yandex.ru',
    description='EnvFetch - это библиотека на Python для управления переменными окружения в приложениях...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/HermitBroccoli/EnvUtil',
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
