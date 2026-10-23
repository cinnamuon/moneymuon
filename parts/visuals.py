def SetStyle(bold: bool, color: str, message: str):
    # choices are green, bold green, red, bold red, default

    if not bold and color == "green":
        return "\x1b[%sm%s\x1b[0m" % ("0;32", message)
    if bold and color == "green":
        return "\x1b[%sm%s\x1b[0m" % ("1;32", message)
    if not bold and color == "red":
        return "\x1b[%sm%s\x1b[0m" % ("0;31", message)
    if bold and color == "red":
        return "\x1b[%sm%s\x1b[0m" % ("1;31", message)
    if not bold and color == "yellow":
        return "\x1b[%sm%s\x1b[0m" % ("0;33", message)
    if bold and color == "yellow":
        return "\x1b[%sm%s\x1b[0m" % ("1;33", message)
    if not bold and color == "blue":
        return "\x1b[%sm%s\x1b[0m" % ("0;34", message)
    if bold and color == "blue":
        return "\x1b[%sm%s\x1b[0m" % ("1;34", message)    

    # default case
    return message

    pass

def DisplayHeader():


    pass

def DisplayMessage(type: str, allow_input: bool, message: str):
    """
    Returns a message with coloring and emboldening.
    """

    bold, color, identifier = False, "", ""

    match type:
        case "alert":
            bold, color, identifier = True, "yellow", "! "
        case "query":
            bold, color, identifier = True, "blue", "? "
        case "positive":
            color = "green"
        case "negative":
            color = "red"
        case "info":
            color = "blue"
        case _:
            pass

    message = f"{identifier}{message}"

    if allow_input:
        return f"{SetStyle(bold, color, message)} : "
    return f"{SetStyle(bold, color, message)}"

    pass