def get_response_code_message(response):
    switcher = {
        200: "Transaction Successful",
        400: "Bad Request",
        401: "Authentication Failed",
        403: "Forbidden",
        404: "URL Not Found",
        201: "Transaction Successful",
        500: "Internal Server Error",
        502:  "Bad Gateway",
        503: "SERVICE UNAVAILABLE",
        504: "Gateway Timeout"

    }
    return switcher.get(response, "Un-Identified")
