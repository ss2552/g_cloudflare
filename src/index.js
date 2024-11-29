// https://developers.cloudflare.com/cache/

export default{
    async fetch(request, env, ctx){
	const pn = new URL(request.url).pathname || "/"

        if(request.method == "GET"){
        	return new Response("Not Found.", {status: 404})
        }else{
        	console.log(await request.text())
		//接続をウェブフックを使いディスコードで通知する
		try{
			await fetch(env.WH_URL, {headers: {"content-type": "application/json"}, body: JSON.stringify({content: `パスネーム ${pn}\nメソッド ${request.method}`}), method: "POST"})
		}catch(e){
			console.log(e)
		}
		//ゲットならステータス404を返す
	}
	return new Response("{}", {headers: {'content-type': 'application/json;charset=UTF-8'}})
    }
}
