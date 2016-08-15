import os
from setuptools import setup, find_packages
import glob

VERSION = "0.6.3"

src_dir = os.path.dirname(__file__)

install_requires = [
    "troposphere>=1.6.0",
    "boto3>=1.3.1",
    "botocore>=1.4.38",
    "PyYAML>=3.11",
    "awacs>=0.5.3",
    "colorama==0.3.7",
]

tests_require = [
    "nose>=1.0",
    "mock==1.0.1",
    "stacker_blueprints",
    "moto",
    "testfixtures",
]


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == "__main__":
    setup(
        name="stacker",
        version=VERSION,
        author="Michael Barrett",
        author_email="loki77@gmail.com",
        license="New BSD license",
        url="https://github.com/remind101/stacker",
        description="Opinionated AWS CloudFormation Stack manager",
        long_description=read("README.rst"),
        packages=find_packages(),
        scripts=glob.glob(os.path.join(src_dir, "scripts", "*")),
        install_requires=install_requires,
        tests_require=tests_require,
        test_suite="nose.collector",
    )
