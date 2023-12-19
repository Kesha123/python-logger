import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python_logger',
    version='{{VERSION_PLACEHOLDER}}',
    author='Innokentii Kozlov',
    author_email='innokentiikozlov@gmail.com',
    description='Python Logger',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Kesha123/python-logger',
    license='MIT',
    packages=['python_logger', 'python_logger.utils'],
    install_requires=[
        'pymongo==4.6.1'
    ]
)