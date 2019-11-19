import meaningcloud.Response


class SummarizationResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        SummarizationResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

    # Getters for the different objects returned

    def getSummary(self):
        """
        Obtains the summary returned

        :return:
            Text extracted as the summary
        """

        return (self._response['summary']
                if (('summary' in self._response.keys()) and (self._response['summary'] is not None))
                else "")