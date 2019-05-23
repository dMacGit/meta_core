from setuptools import setup, find_packages

with open("README.md","r") as fr:
    full_description = fr.read()

setup(

    name="meta_core",
    version="1.0",
    author="dMacGit",
    author_email="d.g.mcindoe@gmail.com",
    description="Core logic for Media Scraper application",
    long_description=full_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dMacGit/meta_core",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "lxml>=4.3.3",
        "requests>=2.22.0"
    ],
)
