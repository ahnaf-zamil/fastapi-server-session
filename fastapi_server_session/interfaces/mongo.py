# Copyright (c) 2022 iudeen

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

from datetime import datetime, timedelta, timezone

from .base import BaseSessionInterface

try:
    import pymongo
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "MongoSessionInterface requires 'pymongo' to be installed. Install it using 'pip install pymongo'"
    )


class MongoSessionInterface(BaseSessionInterface):
    def __init__(
        self,
        client: pymongo.MongoClient,
        *,
        db: str,
        collection: str,
        session_id_key: str = "key",
        created_at_key: str = "_lib_created_at_",
        expire: timedelta = timedelta(days=15)
    ):
        self.client = client
        self.db = db
        self.collection = collection
        self.session_id_key = session_id_key
        self.created_at_key = created_at_key
        self.expire = expire

        self.create_collection()

    def create_collection(self):
        _db = self.client[self.db]
        if self.collection not in _db.list_collection_names():
            _db.create_collection(self.collection)

        _collection = _db[self.collection]
        _collection.create_index(self.session_id_key, name="user_session_id")
        _collection.create_index(
            self.created_at_key, expireAfterSeconds=self.expire.total_seconds()
        )

    def _set_session_data(self, session_id: str, data: dict):
        _db = self.client[self.db]
        _collection = _db[self.collection]
        query = {self.session_id_key: session_id}
        data.update(
            {
                self.created_at_key: datetime.now(tz=timezone.utc),
                self.session_id_key: session_id,
            }
        )
        _collection.update_one(query, {"$set": {**data}}, upsert=True)

    def _get_session_data(self, session_id: str) -> dict:
        try:
            _db = self.client[self.db]
            _collection = _db[self.collection]
            query = {self.session_id_key: session_id}
            return _collection.find_one(query, {"_id": 0})
        except Exception:
            raise

    def _delete_session(self, session_id: str):
        _db = self.client[self.db]
        _collection = _db[self.collection]
        query = {self.session_id_key: session_id}
        _collection.delete_one(query)
