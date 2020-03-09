from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

# with open('HISTORY.md') as history_file:
#     HISTORY = history_file.read()

setup_args = dict(
    name='pycovid',
    version='0.1.0',
    description='Useful tool to access Rami Krispin Novel Corona Dataset',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Sudharshan Ashok',
    author_email='sudharshan93@gmail.com',
    keywords=['Coronavirus', 'COVID'],
    url='https://sudharshan-ashok.github.io',
    download_url='https://sudharshan-ashok.github.io'
)

install_requires = [
    'pandas', 'numpy', 'plotly'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

