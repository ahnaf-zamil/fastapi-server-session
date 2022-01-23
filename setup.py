# Copyright (c) 2022 DevGuyAhnaf

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

import fastapi_server_session

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fastapi-server-session",
    author=fastapi_server_session.__author__,
    author_email=fastapi_server_session.__email__,
    version=fastapi_server_session.__version__,
    description=fastapi_server_session.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=fastapi_server_session.__license__,
    url=fastapi_server_session.__github__,
    packages=["fastapi_server_session", "fastapi_server_session.interfaces"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    exclude=("__pycache__",),
    install_requires=["fastapi", "redis"],
)
