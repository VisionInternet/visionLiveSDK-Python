import apiErrorCode

class ApiException():

    def __init__(self, errorCode, errorMsg):
        if type(errorMsg) == unicode:
            errorMsg = errorMsg.encode('utf-8')
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        self.message = errorCode + ':' + errorMsg
    
    def __str__(self):
        return self.message