

class OcrResult:
    success: bool = False
    error_message: str = ""
    text: str = ""
    matches: [str] = []

    def __init__(self,json_obj):
        for key in json_obj:
            setattr(self, key, json_obj[key])


