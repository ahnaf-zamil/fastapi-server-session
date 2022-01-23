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

from .manager import SessionManager
from .session import Session
from .interfaces.redis import RedisSessionInterface
from .interfaces.base import BaseSessionInterface

from datetime import datetime

__version__ = "0.0.1"
__author__ = "DevGuyAhnaf"
__copyright__ = f"Copyright (c) {datetime.now().strftime('%Y')} DevGuyAhnaf"
__email__ = "ahnaf@ahnafzamil.com"
__description__ = "A dependency-based extension for FastAPI that adds support for server-sided session management"
__license__ = "MIT"
__github__ = "https://github.com/ahnaf-zamil/fastapi-server-session"
