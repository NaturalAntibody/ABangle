from setuptools import find_packages, setup

setup(
    name="abangle",
    version="0.1.0",
    # data/ has no .py files and isn't a real package, but setuptools treats any
    # directory as an "implicit namespace package" once its contents are bundled via
    # package_data; declaring it explicitly here (as setuptools' own warning suggests)
    # resolves the ambiguity instead of leaving it to that implicit discovery.
    packages=find_packages() + ["abangle.data"],
    package_data={"abangle": ["data/*"]},
    include_package_data=True,
    install_requires=[
        "anarci",
        "biopython",
        "numpy",
        "fastcore",
    ],
    entry_points={
        "console_scripts": [
            "ABangle=abangle.cli:main",
        ],
    },
)
