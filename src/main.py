# https://developers.cloudflare.com/cache/
import json, requests
from js import Response, Headers

async def game_id_list():
  pass


async def on_fetch(request, ctx, env) -> Response:
  pathname: str = request.url[29:] or "/"
  
  # 接続をウェブフックを使いディスコードで通知する
  await fetch(env.get("WEBHOOK_URL"), {"header":{"content-type": "application/json"}, "body": {"content": f'パスネーム {pathname}\nメソッド {request.get("method")}'}})

  # ゲットならステータス404を返す
  if request.method == "GET":
    return Response.new("Not Found.", status = 404)
  else:
    print(await request.text())
  
  return Response("{}", Headers.new({'content-type': 'application/json;charset=UTF-8'}))
  
