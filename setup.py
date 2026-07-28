# ============================================================
# FILE: setup.py
# PURPOSE: Makes my ML project installable as a Python package
# ============================================================

import setuptools

# ---------------------------------------------------------------
# Read long description from README.md
# ---------------------------------------------------------------
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# ---------------------------------------------------------------
# Project Metadata
# ---------------------------------------------------------------
__version__ = "0.0.1"

REPO_NAME    = "wine-quality-end-to-end-ml"
AUTHOR_USER_NAME = "KzRaihan"
SRC_REPO     = "mlProject"
AUTHOR_EMAIL = "kamruzzamanraihan00@gmail.com"


# ---------------------------------------------------------------
# Setup Configuration
# ---------------------------------------------------------------
setuptools.setup(
    name                          = SRC_REPO,
    
    version                       = __version__,
    
    author                        = AUTHOR_USER_NAME,
    
    author_email                  = AUTHOR_EMAIL,
    
    description                   = "An end-to-end machine learning pipeline for wine quality prediction.",
    
    long_description              = long_description,
    
    long_description_content_type = "text/markdown",   
    
    url                           = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    
    package_dir  = {"": "src"},                        
    
    packages     = setuptools.find_packages(where="src"),  
    
    python_requires = ">=3.8",                         
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)