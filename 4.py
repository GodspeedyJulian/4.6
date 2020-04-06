import websockets
import asyncio
cs=set()
async def talk(websocket,path):
    while True:
        if (not websocket in cs):
            cs.add(websocket)
            msg='欢迎：'+str(websocket.remote_address)
        else:
            msg=str(websocket.remote_addrss)+'说：'+str(await websocket.recv())
        await asyncio.wait([ws.send(msg) for ws in cs])
    
start_server=websockets.serve(talk,'192.168.3.28',8764)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
