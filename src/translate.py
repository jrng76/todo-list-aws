import todoList


def translate(event, context):
    # create a response
    print("Id: " + event['pathParameters']['id'])
    print("Lenguaje: " + event['pathParameters']['language'])
    re = todoList.gettranslate_todo_text(event['pathParameters']['id'],
                                         event['pathParameters']['language'])
    if re != "":
        response = {
            "statusCode": 200, "body": re
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
