from setuptools import setup, find_packages

def read_readme() -> str:
    with open("README.md", "r", encoding="utf-8") as file:
        return file.read()

setup(
    name="PasswordGenerator",
    version="1.0",
    author="Jin-Mach",
    author_email="Ji82Ma@seznam.cz",
    description="A simple and customizable password generator built with PyQt6 and the secrets library.",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jin-Mach/PasswordGenerator",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.7.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "passwordgenerator=password_generator:create_app",
            ],
        },
    keywords="passwordgenerator, pyqt6, secrets",
)