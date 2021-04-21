from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="drumbot-utils",
    packages=["drumbot-utils"],
    version="0.1.0",
    description="Funciones, metodos y clases que se usan de forma recurrente en los "
                "proyectos de drumbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luis Manuel Torres Trevino",
    author_email="lmtorres123@icloud.com",
    url="https://github.com/trevino-676/drumbot-utils",
    download_url="https://github.com/trevino-676/drumbot-utils/tarball/0.1",
    keywords=[],
    classifiers=[],
    install_requires=[
        "pymongo"
    ]
)
