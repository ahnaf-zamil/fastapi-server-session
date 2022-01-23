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

from .base import BaseSessionInterface
from datetime import timedelta

try:
    import redis
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "RedisSessionInterface requires 'redis' to be installed. Install it using 'pip install redis'"
    )

import json


class RedisSessionInterface(BaseSessionInterface):
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    def _set_session_data(self, session_id: str, data: dict):
        self.redis.set(
            session_id, json.dumps(data), ex=timedelta(days=15)
        )  # Session expires after 15 days

    def _get_session_data(self, session_id: str) -> dict:
        try:
            return json.loads(self.redis.get(session_id))
        except:
            return {}

    def _delete_session(self, session_id: str):
        self.redis.delete(str(session_id))
