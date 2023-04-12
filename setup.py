import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='shinycomponents',
    version='0.0.1',
    author='Bart Verweire',
    author_email='bart.verweire@smals.be',
    description='Connection Manager for Smals databases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bartverweire/py-shinycomponents',
    project_urls = {
        "Bug Tracker": "https://github.com/bartverweire/py-shinycomponents/issues"
    },
    license='None',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pandas','shiny','shinywidgets','ipywidgets'],
)