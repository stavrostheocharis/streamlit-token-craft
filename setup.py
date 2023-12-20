import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="token_craft",
    version="0.1.0",
    author="Stavros Theocharis",
    author_email="stavrostheocharis@yahoo.gr",
    description="streamlit custom token craft and management component",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stavrostheocharis/streamlit-token-craft",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "Python",
        "Streamlit",
        "React",
        "JavaScript",
        "token craft",
        "token manager",
    ],
    python_requires=">=3.9",
    install_requires=[
        "streamlit >= 1.29.0",
    ],
)
