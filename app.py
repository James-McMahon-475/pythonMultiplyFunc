from mul import multiply
from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)

@app.route('/')
def mulNum():
    ru = request.args.get('u')
    rv = request.args.get('v')

    if not ru:
        r = "You must include a u value"
        response = Response(response=r, status=400)
        return response

    if not rv or rv == 0:
        r = "You must include a v value"
        response = Response(response=r, status=400)
        return response

    try:
        u = int(ru)
        v = int(rv)
    except ValueError:
        r = "You must provide valid integer for u and v"
        response = Response(response=r, status=400)
        return response


    x, z = multiply(u, v)
    r = {"error": z, "string": ru+" * "+rv+" = "+str(x), "u": u, "v": v, "answer": x}
    reply = jsonify(r)
    reply.headers["Content-Type"]="application/json"
    reply.headers["Access-Control-Allow-Origin"]="*"
    return reply

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)
