import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="token_manager",
    version="0.1.0",
    author="Stavros Theocharis",
    author_email="stavrostheocharis@yahoo.gr",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["Python", "Streamlit", "React", "JavaScript"],
    python_requires=">=3.9",
    install_requires=[
        "streamlit >= 1.29.0",
    ],
)