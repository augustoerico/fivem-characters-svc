import simplejson as json


def handle(event: dict, _):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "data": {
                ""
            }
        })
    }
    pass
