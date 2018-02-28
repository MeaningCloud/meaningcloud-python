import meaningcloud.Response

class LanguageResponse(meaningcloud.Response):

    def __init__(self,response):
        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

