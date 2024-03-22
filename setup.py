from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Ife Stephen',
    author_email = 'damoflove2022@gmail.com',
    install_requires = ["openai", "langchain", "streamlit", "python-dotenv", "PDF2"],
    packages = find_packages()
)