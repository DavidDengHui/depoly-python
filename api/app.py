from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import base64
import binascii
import json
import requests

app = Flask(__name__)
CORS(app)

status_data = {
    "status": "error",
    "code": "1001",
    "doit": "NO_KEY",
    "callback": "INVALID_KEY"
}


def to_list(cont):
    result = {}
    for key, value in cont.items():
        result[key] = value
    return result


@app.route("/doit", methods=["GET", "POST"])
def doit():
    token = request.args.get("token")
    if request.method == "POST":
        token = page_url = to_list(request.json)["password"]
    hook_name = request.args.get("hook_name")
    if request.method == "POST":
        hook_name = page_url = to_list(request.json)["hook_name"]
    if request.headers.get("HTTP_X_GITHUB_EVENT"):
        hook_name = request.headers.get("HTTP_X_GITHUB_EVENT")
    if token:
        if token == "get_info":
            if hook_name:
                if hook_name == "bilibili":
                    api = "api.bilibili.com"
                    path = "/x/web-interface/"
                    type = "popular"
                    web = "all"
                    if request.args.get("type"):
                        if request.args.get("type") == "rank":
                            web = "rank/all"
                            type = "ranking/v2?rid=0&type=all"
                        elif request.args.get("type") == "rank01":
                            web = "rank/bangumi"
                            path = "/pgc/web/rank/"
                            type = "list?day=3&season_type=1"
                        elif request.args.get("type") == "rank02":
                            web = "rank/guochan"
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=4"
                        elif request.args.get("type") == "rank03":
                            web = "rank/guochuang"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=168&type=all"
                        elif request.args.get("type") == "rank04":
                            web = "rank/documentary"
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=3"
                        elif request.args.get("type") == "rank05":
                            web = "rank/douga"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=1&type=all"
                        elif request.args.get("type") == "rank06":
                            web = "rank/music"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=3&type=all"
                        elif request.args.get("type") == "rank07":
                            web = "rank/dance"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=129&type=all"
                        elif request.args.get("type") == "rank08":
                            web = "rank/game"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=4&type=all"
                        elif request.args.get("type") == "rank09":
                            web = "rank/knowledge"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=36&type=all"
                        elif request.args.get("type") == "rank10":
                            web = "rank/tech"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=188&type=all"
                        elif request.args.get("type") == "rank11":
                            web = "rank/sports"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=234&type=all"
                        elif request.args.get("type") == "rank12":
                            web = "rank/car"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=223&type=all"
                        elif request.args.get("type") == "rank13":
                            web = "rank/life"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=160&type=all"
                        elif request.args.get("type") == "rank14":
                            web = "rank/food"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=211&type=all"
                        elif request.args.get("type") == "rank15":
                            web = "rank/animal"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=217&type=all"
                        elif request.args.get("type") == "rank16":
                            web = "rank/kichiku"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=119&type=all"
                        elif request.args.get("type") == "rank17":
                            web = "rank/fashion"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=155&type=all"
                        elif request.args.get("type") == "rank18":
                            web = "rank/ent"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=5&type=all"
                        elif request.args.get("type") == "rank19":
                            web = "rank/cinephile"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=181&type=all"
                        elif request.args.get("type") == "rank20":
                            web = "rank/movie"
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=2"
                        elif request.args.get("type") == "rank21":
                            web = "rank/tv"
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=5"
                        elif request.args.get("type") == "rank22":
                            web = "rank/variety"
                            path = "/pgc/season/rank/web/"
                            type = "list?day=3&season_type=7"
                        elif request.args.get("type") == "rank23":
                            web = "rank/origin"
                            path = "/x/web-interface/ranking/"
                            type = "v2?rid=0&type=origin"
                        elif request.args.get("type") == "rank24":
                            web = "rank/rookie"
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
                        "referer": "https://www.bilibili.com/v/popular/" + web,
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
        elif token == "get_api":
            if hook_name:
                status_data["doit"] = hook_name
                data = requests.get(hook_name)
                if data.ok:
                    get_data = data.content
                    data_json = json.loads(get_data)
                    status_data["status"] = "success"
                    status_data["code"] = "1103"
                    status_data["callback"] = data_json
                else:
                    status_data["code"] = "1006"
                    status_data["callback"] = f"INVALID_HOOK_{data.status_code}"
            else:
                status_data["code"] = "1005"
                status_data["doit"] = token
                status_data["callback"] = "NO_HOOK"
        else:
            try:
                token = base64.b64decode(token).decode()
                if hook_name:
                    if hook_name == "deployment_status":
                        status_data["code"] = "1009"
                        status_data["doit"] = token + " | " + hook_name
                        username = request.args.get("username")
                        repopath = request.args.get("repopath")
                        reponame = request.args.get("reponame")
                        state = request.args.get("state")
                        if request.method == "POST":
                            state = to_list(request.json)[
                                "deployment_status"]["state"]
                        if state == "success":
                            status_data["status"] = "success"
                            status_data["code"] = "1103"
                            page_url = request.args.get("url")
                            if request.method == "POST":
                                page_url = to_list(request.json)[
                                    "deployment_status"]["environment_url"]
                            url = f"https://api.github.com/repos/{repopath}/{reponame}/commits/master"
                            headers = {
                                "Authorization": f"token {token}",
                                "User-Agent": username,
                            }
                            response = requests.get(url, headers=headers)
                            data = response.json()
                            sha = data["sha"]
                            commit_msg = data["commit"]["message"]
                            url = f"https://api.github.com/repos/{repopath}/{reponame}/commits/{sha}/comments"
                            headers["Content-Type"] = "application/json"
                            body = f"# Successfully deployed with \n > {commit_msg}\n## Following the Pages URL:\n### [{page_url}]({page_url})"
                            response = requests.post(
                                url, data=json.dumps({"body": body}), headers=headers
                            )
                            status_data["callback"] = json.loads(
                                response.content)
                        else:
                            status_data["callback"] = f"[state]{state}"
                    elif hook_name == "push_hooks":
                        status_data["status"] = "success"
                        status_data["code"] = "1104"
                        status_data["doit"] = token + " | " + hook_name
                        username = request.args.get("username")
                        repopath = request.args.get("repopath")
                        reponame = request.args.get("reponame")
                        url = f"https://api.github.com/repos/{repopath}/{reponame}/dispatches"
                        data = {"event_type": request.args.get("event_type")}
                        data_json = json.dumps(data)
                        headers = {
                            "Accept": "application/json",
                            "Authorization": f"token {token}",
                            "User-Agent": username,
                            "Content-Type": "application/json",
                            "Content-Length": str(len(data_json)),
                        }
                        response = requests.post(
                            url, data=data_json, headers=headers
                        )
                        status_data["callback"] = {
                            "url": url,
                            "data": data,
                            "headers": headers,
                            "state": response.status_code,
                        }
                    else:
                        status_data["status"] = "error"
                        status_data["code"] = "1008"
                        status_data["doit"] = token + " | " + hook_name
                        status_data["callback"] = "INVALID_HOOK"
                else:
                    status_data["code"] = "1007"
                    status_data["doit"] = token
                    status_data["callback"] = "NO_HOOK"
            except binascii.Error:
                status_data["code"] = "1002"
                status_data["doit"] = token

    return jsonify(status_data)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
