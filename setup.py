import setuptools
from setuptools import setup
from pathlib import Path
from src.vocably import __version__

core_requirements = [
    "click~=8.0.1",
    "jsonpickle~=2.1.0",
    "pyyaml~=6.0",
    "torch~=1.13.0",
    "regex",
    "scikit-learn~=1.1.2",
    'rich~=12.6.0',
    "transformers~=4.22.0",
    'gensim~=4.2.0',
    'nltk~=3.7',
    'spacy~=3.4.1',
    'smart-open~=5.2.1',
    'sentencepiece~=0.1.98',
    'protobuf~=3.20.0',
    'happytransformer~=2.4.1',
    'aiohttp~=3.7.4'
]

# not to install as egg file
setup(
    name='vocably',
    version=__version__,
    py_modules=['command', 'core'],
    install_requires=core_requirements,
    description='Vocably is a Natural Language Framework written in Python for Language based Tasks.',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    python_requires='>=3.7,<4',
    author="Nandhini, Sarika",
    author_email="nandhinisiva2561@gmail.com",
    url="https://github.com/Nandhini25S/Vocably",
    include_package_data=True,
    os_type=["linux", "Windows", "MacOS", "Unix"],
    license='MIT',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'vocably = vocably.cli.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
