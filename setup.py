import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='busybutton',
    version='0.2',
    author='Som Shekar',
    author_email='shek2994@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shek2994/busybutton',
    project_urls = {
        "Bug Tracker": "https://github.com/shek2994/busybutton/issues"
    },
    license='MIT',
    packages=['busybutton'],
    install_requires=['PyQt5'],
)