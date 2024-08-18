#  @Project: NDN Storage
#  @Authors: Please check AUTHORS.rst
#  @Source-Code: https://github.com/tntech-ngin/ndn-python-database
#  @Pip-Library: https://pypi.org/project/ndn-python-database

import io
import re
from setuptools import setup, find_packages
from typing import List

with io.open("./docs/version.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with io.open("README.rst", "rt", encoding="utf8") as f:
    long_description = f.read()


def _parse_requirements(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return [s for s in [line.split('#', 1)[0].strip(' \t\n') for line in f] if s != '']


setup(
    name='ndn-python-database',
    version=version,
    description='An NDN Storage Library for Applications in Python 3',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/tntech-ngin/ndn-python-database',
    author='See GitHub',
    author_email='sshannigrahi@tntech.edu',
    maintainer='see GitHub',
    maintainer_email='sshannigrahi@tntech.edu',
    download_url='https://pypi.python.org/pypi/ndn-python-database',
    project_urls={
        "Bug Tracker": "https://github.com/tntech-ngin/ndn-python-database/issues",
        "Source Code": "https://github.com/tntech-ngin/ndn-python-database",
    },
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='NDN STORAGE DISK MEMORY CACHE',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={'ndn-python-database': ['config.yaml', 'docs/version.py', 'docs/requirements.txt']},
    install_requires=_parse_requirements('docs/requirements.txt'),
    python_requires=">=3.8",
    zip_safe=False)
