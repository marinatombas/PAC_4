from setuptools import setup, find_packages

setup(
    name="pac4_laliga",
    version="1.0.0",
    author="Marina Tombas Suñé",
    author_desc="mtombass@uoc.edu",
    description="Projecte modular per a l'anàlisi de dades històriques de LaLiga (1995-2025)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url= "https://github.com/marinatombas/PAC_4",

    # Codi font del projecte
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    # Instalar requirements
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "networkx",
    ]
)