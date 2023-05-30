from flask import Flask, jsonify, request, render_template
import base64
import binascii
import json
import requests

app = Flask(__name__)


status_data = {
    "status": "error",
    "code": "1001",
    "doit": "NO_KEY",
    "callback": "INVALID_KEY"
}


@app.route("/doit")
def doit():
    token = request.args.get("token")
    hook_name = request.args.get("hook_name")
    if token:
        if token == "get_info":
            if hook_name:
                if hook_name == "bilibili":
                    api = "api.bilibili.com"
                    path = "/x/web-interface/"
                    type = "popular"
                    if request.args.get("type"):
                        if request.args.get("type") == "rank":
                            type = "ranking/v2?rid=0&type=all"
                        elif request.args.get("type") == "rank01":
                            path = "/pgc/web/rank/"
                            type = "list?day=3&season_type=1"
                        elif request.args.get("type") == "rank02":
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=4"
                        elif request.args.get("type") == "rank03":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=168&type=all"
                        elif request.args.get("type") == "rank04":
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=3"
                        elif request.args.get("type") == "rank05":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=1&type=all"
                        elif request.args.get("type") == "rank06":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=3&type=all"
                        elif request.args.get("type") == "rank07":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=129&type=all"
                        elif request.args.get("type") == "rank08":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=4&type=all"
                        elif request.args.get("type") == "rank09":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=36&type=all"
                        elif request.args.get("type") == "rank10":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=188&type=all"
                        elif request.args.get("type") == "rank11":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=234&type=all"
                        elif request.args.get("type") == "rank12":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=223&type=all"
                        elif request.args.get("type") == "rank13":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=160&type=all"
                        elif request.args.get("type") == "rank14":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=211&type=all"
                        elif request.args.get("type") == "rank15":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=217&type=all"
                        elif request.args.get("type") == "rank16":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=155&type=all"
                        elif request.args.get("type") == "rank17":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=5&type=all"
                        elif request.args.get("type") == "rank18":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=181&type=all"
                        elif request.args.get("type") == "rank19":
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=2"
                        elif request.args.get("type") == "rank20":
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=5"
                        elif request.args.get("type") == "rank21":
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=7"
                        elif request.args.get("type") == "rank22":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=0&type=origin"
                        elif request.args.get("type") == "rank23":
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=0&type=rookie"
                    else:
                        if request.args.get("ps"):
                            type = type + "?ps=" + request.args.get("ps")
                            if request.args.get("pn"):
                                type = type + "&pn=" + request.args.get("pn")
                            else:
                                type = type + "&pn=1"

                    header = {
                        "authority": api,
                        "method": "GET",
                        "path": path + type,
                        "scheme": "https",
                        "accept": "application/json, text/plain, /",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                        "cache-control": "no-cache",
                        "cookie": "",
                        "origin": "https://www.bilibili.com",
                        "pragma": "no-cache",
                        # "referer": "https://www.bilibili.com/v/popular/rank/all",
                        "sec-ch-ua": '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": '"Windows"',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-site",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
                    }
                    url = "https://" + api + path + type
                    data = requests.get(url)
                    get_data = data.content
                    data_json = json.loads(get_data)
                    status_data["status"] = "success"
                    status_data["code"] = "1101"
                    status_data["doit"] = url
                    status_data["callback"] = data_json
                else:
                    status_data["code"] = "1004"
                    status_data["doit"] = token + " | " + hook_name
                    status_data["callback"] = "INVALID_HOOK"
            else:
                status_data["code"] = "1003"
                status_data["doit"] = token
                status_data["callback"] = "INVALID_HOOK"
        else:
            try:
                token = base64.b64decode(token).decode()
                status_data["status"] = "success"
                status_data["code"] = "1102"
                status_data["doit"] = token
                status_data["callback"] = token
            except binascii.Error:
                status_data["code"] = "1002"
                status_data["doit"] = token

    return jsonify(status_data)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
