def urlparse(url: str):
    """Parse GET parameters from URL

    Args:
        url (str): full url (including http://)

    Returns:
        parameters: dict with all the parameters and values found
    """
    try:
        querystringSplit = url.split("/?")
        querystring = querystringSplit[-1]
        parameters = {}
        ampersandSplit = querystring.split("&")
        for element in ampersandSplit:
          equalSplit = element.split("=")
          parameters[equalSplit[0]] = equalSplit[1]
        return parameters
    except:
        return parameters

def urlextract(request:str):
    """extract URL from full Request

    Args:
        request (str): full request as extracted by socket connection

    Returns:
        splitbyspace[1]: string with the url endpoint (example: /?speed=low&direction=left)
    """
    splitbyspace = request.split(" ")
    return splitbyspace[1]