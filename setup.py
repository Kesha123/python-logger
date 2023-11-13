import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python_logger',
    version='3.0.0',
    author='Innokentii Kozlov',
    author_email='innokentiikozlov@gmail.com',
    description='Python Logger',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hiava-Oy/python-logger',
    license='MIT',
    packages=['python_logger'],
)