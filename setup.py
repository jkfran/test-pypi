import setuptools

setuptools.setup(
    name="hello-jkfran",
    version="0.3",
    scripts=["hello-jkfran"],
    author="Francisco Jimenez Cabrera",
    author_email="jkfran@gmail.com",
    description="Hello jkfran",
    long_description="Hello jkfran",
    long_description_content_type="text/plain",
    url="https://github.com/jkfran/test-pypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
