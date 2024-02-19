class Error:


    @staticmethod
    def error_503():
        print('Service Unavailable')
    @staticmethod
    def error_404():
        print('Not Found')
    

Error.error_404()
Error.error_503()