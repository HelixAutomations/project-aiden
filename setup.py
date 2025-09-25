from setuptools import setup, find_packages

setup(
    name="aiden-spider",
    version="1.0.0",
    description="Microsoft Graph API Spider Agent - Crawls into projects and delivers Graph superpowers",
    author="Aiden",
    py_modules=["aiden"],
    install_requires=[
        "azure-keyvault-secrets>=4.10.0",
        "azure-identity>=1.25.0",
        "requests>=2.32.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)