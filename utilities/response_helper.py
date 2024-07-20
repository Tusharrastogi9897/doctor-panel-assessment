
def response_helper(success: bool,  data: any = None, message: str = None, **kwargs):
    return {
        "success": success,
        "message": message,
        "data": data,
        **kwargs
    }