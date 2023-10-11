from bottle import route, run, post, request, response, auth_basic, parse_auth, Bottle, error
from json import dumps
import subprocess


app = Bottle()


def authentication(user, password):
    try:
        host = request.get_header("Host")
        conn = request.get_header("Connection")
        x_f5 = request.get_header("X-F5-Auth-Token")

        assert user == "admin", "Wrong user"
        assert password == "horizon3", "Wrong password"
        assert host in ("localhost", "127.0.0.1"), "Wrong Host"
        assert "X-F5-Auth-Token" in conn, "Connection header missing X-F5-Auth-Token"
        assert x_f5 is not None, "Missing X-F5-Auth-Token"
    except AssertionError as e:
        print(e)
        return False

    return True


@app.post('/mgmt/tm/util/bash')
@auth_basic(authentication)
def mgmtutil():
    postdata = request.json
    utilCmdArgs = postdata["utilCmdArgs"]
    rce = subprocess.Popen("bash " + utilCmdArgs, stdout=subprocess.PIPE, shell=True)
    (output, err) = rce.communicate()
    rce.wait()
    resultjson = {
        "commandResult" : output.decode('utf-8')
    }
    response.content_type = 'application/json'
    return dumps(resultjson)


@app.route('/')
def main():
    return "Under construction"


@app.route('/mgmt/admin')
@auth_basic(authentication)
def admin():
    response.status_code = 200


@app.error(401)
def error401(error):
    return "401 Unauthorized"


@app.error(404)
def error404(error):
    return "404 Error page not Found"


if __name__ == "__main__":
    run(app, host='0.0.0.0', port=80)
