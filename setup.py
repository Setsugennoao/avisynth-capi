#!/usr/bin/env python3

import setuptools

with open("README.md") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    install_requires = fh.read()

setuptools.setup(
    name="avipynth",
    version="0.0.1",
    author="Setsugen no ao",
    author_email="setsugen@setsugen.dev",
    description="AviSynth script bindings in Python, with VapourSynth integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["avipynth", "avipynth.structures"],
    url="https://github.com/Setsugennoao/avisynth-py",
    package_data={
        'avipynth': ['py.typed'],
    },
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9'
)
