from setuptools import find_packages, setup


setup(
    name='tilesizer',
    version='0.0.2',
    author="Paul Norman",
    author_email="osm@paulnorman.ca",
    url="https://github.com/pnorman/tilesizer",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'Click',
        'fs'
    ],
    entry_points={
        'console_scripts': ['tilesizer=tilesizer:cli']
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    python_requires="~=3.6"
)
