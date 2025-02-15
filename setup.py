from setuptools import find_packages, setup

setup(
    name='fwx-python-sdk',
    packages=find_packages(include=['FWX']),
    version='0.1.0',
    description='An unofficial Python SDK for interacting with the FWX DeFi protocol',
    author='Krittipat Krittakom',
    author_email='Krittipat.k@ku.th',  # Add your email here
    url='https://github.com/Krittipat-K/FWX-Python-SDK',  # Add the URL to your repository
    install_requires=[
        'web3==7.7.0',
        'python-dotenv==1.0.1'
    ],
    python_requires='>=3.9',
)