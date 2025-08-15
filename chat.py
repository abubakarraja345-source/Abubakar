def handler(request):
    import json
    body = json.loads(request.body)
    message = body.get("message", "")
    personality = body.get("personality", "friendly")

    reply = f"You said: '{message}' with personality '{personality}'"
    return {
        "statusCode": 200,
        "body": json.dumps({ "reply": reply })
    }