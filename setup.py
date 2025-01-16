# setup.py
from setuptools import setup, find_packages

setup(
    name="cropsflow-automobile-tn",
    version="0.1.0",
    description="automobile.tn Cropsflow project",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Med Mahdi Maarouf",
    author_email="info@cropsflow.com",
    url="https://github.com/medmahdimaarouf/cropsflow-automobile.tn",  # Your project URL
    packages=find_packages(include=["automobile_tn", "automobile_tn.*"]),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
