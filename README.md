# FastAPI Server-sided Session

[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-black?style=flat-square)](https://github.com/psf/black)
[![pyvers](https://img.shields.io/badge/python-3.6+-blue?style=flat-square)]()

FastAPI Server Session is a dependency-based extension for FastAPI that adds support for server-sided session management.

At the moment, it supports using Redis and MongoDB as the session datastore. But in the future, it will support even more datastores including but not limited to SQL, etc.

## Quickstart

#### For Redis Backend
```py
from fastapi_server_session import SessionManager, RedisSessionInterface, Session
import redis


session_manager = SessionManager(
    interface=RedisSessionInterface(redis.from_url("redis://localhost"), expiration=timedelta(days=7))
)
```

#### For Mongo Backend
```py
from fastapi_server_session import SessionManager, MongoSessionInterface, Session
import pymongo

session_manager = SessionManager(
    interface=MongoSessionInterface(
        pymongo.MongoClient(
            "mongodb://localhost:27017"
        ),
        db="users",
        collection="session",
    )
)

```

```py
from fastapi import Depends, FastAPI

api = FastAPI()


@api.get("/set")
async def set_session(session: Session = Depends(session_manager.use_session)):
    session["key"] = "value"
    return {"status": "ok"}

@api.get("/get")
async def get_session(session: Session = Depends(session_manager.use_session)):
    return {"value": session["key"]} # or session.get("key")
```

## Contributing

If you are considering to contribute, thanks a lot! We welcome all contributors here and, you can help out as well.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/) License

Copyright (c) 2022 DevGuyAhnaf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
