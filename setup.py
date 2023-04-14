from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dicom-processor",
    version="1.0.0",
    author="Mohammed Sinad",
    author_email="sinadsiraj@gmail.com",
    description="A package for processing DICOM images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/dicom-processor",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "pydicom",
        "Pillow",
    ],
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
)