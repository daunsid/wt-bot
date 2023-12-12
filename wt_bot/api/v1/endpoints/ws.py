import json
from datetime import datetime

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from wt_bot.api.v1.endpoints import utils

from wt_bot.wt_bot import ChatApgar

router = APIRouter()
chat = ChatApgar()

@router.websocket("/chat/{user_id}")
async def chat_api(
    user_id:str,
    websocket:WebSocket
):
    await utils.manager.connect(websocket)


    now = datetime.now()
    current_time = now.strftime("%H:%M")

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            response = chat.generate_response(data)
            print(response)
            response = json.dumps(response["output"])

            await utils.manager.send_personal_message(response, websocket)

    except WebSocketDisconnect:
        utils.manager.disconnect(websocket)
        
