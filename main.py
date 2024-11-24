# https://developers.cloudflare.com/cache/
import parse from urllib
import json
import request
from js import Response, Headers

async def game_id_list():
  pass


async def on_fetch(request, ctx, env) -> Response:
  pathname: str = parse.urlparse(request.url).path or "/"
  
  # 接続をウェブフックを使いディスコードで通知する
  res = requests.post(env.get("WEBHOOK_URL"), headers={"content-type": "application/json"}, json={"content": f'パスネーム {pathname}\nメソッド {request.get("method")}'})
  print(res.status)

  //ゲットならステータス404を返す
  if request.method == "GET":
    return Response.new("Not Found.", status = 404)
  else:
    print(await request.text())
  
  return Response("{}", Headers.new({'content-type': 'application/json;charset=UTF-8'}))

"""
fetch(`https://dash.cloudflare.com/api/v4/accounts/${account_id}/workers/observability/telemetry/query`, {
  "headers": {
    "content-type": "application/json"
  },
  "body": "{\"timeframe\":{\"to\":1732354780864,\"from\":1732095580864},\"view\":\"events\",\"limit\":100,\"dry\":true,\"queryId\":\"workers-logs\",\"parameters\":{\"datasets\":[\"cloudflare-workers\"],\"filters\":[{\"key\":\"$baselime.service\",\"type\":\"string\",\"value\":\"g\",\"operation\":\"=\"}]}}",
  "method": "POST"
});
"""
