from pathlib import Path

import setuptools


def parse_requirements(filename: str) -> list[str]:
    with open(Path(__name__).parent / filename) as f:
        return [line for line in f.readlines() if line[0] not in ["-", "#"]]


setuptools.setup(
    name="mixoni",
    version="0.0.1",
    author="figchutney",
    author_email="fig.chutney8@gmail.com",
    description="A little tool to help you make cocktails",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/figchutney/mixoni",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=parse_requirements("requirements.in"),
    extras_require={"dev": parse_requirements("requirements-dev.in")},
)
