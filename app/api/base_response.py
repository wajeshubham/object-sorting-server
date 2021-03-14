class BaseResponse:
    def __init__(self):
        pass

    @staticmethod
    def success_response(data, status):
        return {
            "success": True,
            "status": status,
            "error": [],
            "data": data
        }

    @staticmethod
    def error_response(error, status):
        return {
            "success": False,
            "status": status,
            "error": error if type(error) == list else [error],
            "data": {}
        }
