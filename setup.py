import setuptools
with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()    
__version__="0.0.0"
REPO_NAME="End-to-end-Text-Summarization"
AUTHOR_USER_NAME="yashvk2430"
SRC_REPO="textsummarization"
AUTHOR_EMAIL="yashvk2418@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" A small python package for NLP app",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)