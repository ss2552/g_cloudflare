// https://developers.cloudflare.com/cache/

export default{
    async fetch(request, env, ctx){
		const pn = new URL(request.url).pathname || "/"

		//接続をウェブフックを使いディスコードで通知する
		try{
			await fetch(env.WH_URL, {headers: {"content-type": "application/json"}, body: JSON.stringify({content: `パスネーム ${pn}\nメソッド ${request.method}`}), method: "POST"})
		}catch(e){
			console.log(e)
		}
		//ゲットならステータス404を返す
        if(request.method == "GET"){
        	return new Response("Not Found.", {status: 404})
        }else{
        	console.log(await request.text())
		}
		return new Response("{}", {headers: {'content-type': 'application/json;charset=UTF-8'}})
    },
}

/*
fetch(`https://dash.cloudflare.com/api/v4/accounts/${account_id}/workers/observability/telemetry/query`, {
  "headers": {
    "content-type": "application/json"
  },
  "body": "{\"timeframe\":{\"to\":1732354780864,\"from\":1732095580864},\"view\":\"events\",\"limit\":100,\"dry\":true,\"queryId\":\"workers-logs\",\"parameters\":{\"datasets\":[\"cloudflare-workers\"],\"filters\":[{\"key\":\"$baselime.service\",\"type\":\"string\",\"value\":\"g\",\"operation\":\"=\"}]}}",
  "method": "POST"
});
*/
