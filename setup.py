import io
import re

from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("kapwrapper/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="kap-wrapper",
    version=version,
    description="Kap wrapper to fetch funds data from http://kap.org.tr/",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Serhat Durmaz",
    author_email="serhat.md@gmail.com",
    url="https://github.com/semudu/kap-wrapper",
    download_url="https://github.com/semudu/kap-wrapper/archive/v" + version + ".tar.gz",
    keywords=["KAP", "WRAPPER", "FUND", "FON"],
    install_requires=["requests","lxml"],
    packages=["kapwrapper"],
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
