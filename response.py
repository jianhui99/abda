from flask import jsonify


ok = 1
notok = 0

def __result(code, data, msg=None):
    """
    Helper function to create a JSON response.
    """
    response = {
        "code": code,
        "data": data,
        "message": msg
    }

    return jsonify(response)


def success_response(data, msg='success'):
    """
    Function to create a success JSON response.
    """
    return __result(ok, data, msg)


def error_response(msg):
    """
    Function to create an error JSON response.
    """
    return __result(notok, None, msg)

