import json


class Response:
    _response = {}
    __strResponse = {}
    __aux = {}

    def __init__(self, response):
        """
        Response constructor

        :param response:
            Array returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        self.__strResponse = response
        if response.__class__ == 'str'.__class__:
            self._response = json.loads(response)
        else:
            self._response = json.loads(response.text)

    def isSuccessful(self):
        """
        Checks if the response has been successful at application level (code returned by the API)

        :return:
            Boolean indicating if the request has finished successfully (application level)
        """

        return(self.getStatusCode() == '0')

    # Getters and Setters

    def getStatusCode(self):
        """
        Returns the code of the status or None if it does not exist

        :return:
            Status code of the response
        """

        if 'status' in self._response.keys():
            if (self._response['status'] is not None) and ('code' in self._response['status'].keys()) and (self._response['status']['code'] is not None):
                return self._response['status']['code']

            else:
                return None
        else:
            return None

    def getStatusMsg(self):
        """
        Returns the message of the status or an empty string if it does not exist

        :return:
            Status message of the response
        """

        if 'status' in self._response.keys():
            if (self._response['status'] is not None) and ('msg' in self._response['status'].keys()) and (self._response['status']['msg'] is not None):
                return self._response['status']['msg']
            else:
                return ''

    def getConsumedCredits(self):
        """
        Returns the credit consumed by the request made

        :return:
            String with the number of credits consumed
        """

        if 'status' in self._response.keys():
            if (self._response['status'] is not None) and ('credits' in self._response['status'].keys()):
                if self._response['status']['credits'] is not None:
                    return self._response['status']['credits']
                else:
                    return '0'
            else:
                print("Not credits field\n")
        else:
            return None

    def getRemainingCredits(self):
        """
        Returns the remaining credits for the license key used after the request was made

        :return:
            String with remaining credits
        """

        if 'status' in self._response.keys():
            if (self._response['status'] is not None) and ('remaining_credits' in self._response['status'].keys()):
                if self._response['status']['remaining_credits'] is not None:
                    return self._response['status']['remaining_credits']
                else:
                    return ''
            else:
                print("Not remaining credits field\n")
        else:
            return None

    def getResults(self):
        """
        Returns the results from the API without the status of the request

        :return:
            Dictionary with the results
        """

        results = self._response.copy()
        if 'status' in self._response.keys():
            if results['status'] is not None:
                del results['status']
            return results
        else:
            return None

    def getResponse(self):
        """
        Returns the complete response from the API

        :return:
            Dictionary with the response
        """

        return self._response

    def getStrResponse(self):
        """
        Returns the response from the API as a string

        :return:
            String with the response
        """

        return self.__strResponse
