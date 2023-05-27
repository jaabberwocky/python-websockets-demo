# Simple websockets implementation in Python

Playing around with the `websockets` library in Python and using some `asyncio` capabilities.

## Instructions
1. Install dependencies using `poetry` by running `poetry install`
2. Run the server `poetry run python server.py`
3. Initiate the client connection by using another terminal with:

```
python -m websockets ws://localhost:8765/
```
4. Send messages using the client:

``` 
$ python -m websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> Hello world!
< Hello world!
```
