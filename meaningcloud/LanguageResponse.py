import meaningcloud.Response


class LanguageResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        LanguageResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)
