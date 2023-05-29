# Simple websockets implementation in Python

Playing around with the `websockets` library in Python and using some `asyncio` capabilities. This project comes with a client written in vanilla HTML/JS and using Skeleton CSS.

The current implementation supports broadcasting all messages to all connected clients.

## Instructions
1. Install dependencies using `poetry` by running `poetry install`
2. Run the server `poetry run python server.py`

### Options for clients

a. Start the client by serving the `index.html`:

```
cd client
http-server .
```

Navigate to the URL (`http://localhost:8080` for `http-server`) and interact with the client!

b. Initiate the client connection by using another terminal with:

```
python -m websockets ws://localhost:8765/
```
Send messages using the client:

``` 
$ python -m websockets ws://localhost:8765/
Connected to ws://localhost:8765/.
> {"type":"ping"}
```

