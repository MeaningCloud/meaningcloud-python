#
# Created by MeaningCloud Support Team
# Date: 26/02/18
#


import json
import copy

class Response:
    # @param response. Array with the response
    _response = {}
    # @param strResponse. String response
    __strResponse = {}

    __aux = {}

    #Response constructor
    # @param response. Array returned by the request
    # @throws \Exception if the parameters passed are incorrect

    def __init__(self, response):
        if not response:
            raise Exception("The request sent did not return a response")
        self.__strResponse = response
        if(response.__class__ == 'str'.__class__):
            self._response = json.loads(response)
        else:
            self._response = json.loads(response.text)

    #Checks if the response has been successful at application level (code returned by the API)
    #@return booleas if the request has finished successfully (application level)


    def isSuccessful(self):
        return(self.getStatusCode() == '0')

    # Getters and Setters

    #Returns the code of the status or None if it does not exist
    #@return string|None

    def getStatusCode(self):
        if('status' in self._response.keys()):
            if ((self._response['status'] is not None) and ('code' in self._response['status'].keys()) and (self._response['status']['code'] is not None)):
                return self._response['status']['code']

            else:
                return None
        else:
            return None


    #Returns the message of the status or an empty string if it doesn't exist
    # @return string

    def getStatusMsg(self):
        if ('status' in self._response.keys()):
            if ((self._response['status'] is not None) and ('msg' in self._response['status'].keys()) and (self._response['status']['msg'] is not None)):
                return self._response['status']['msg']
            else:
                return ''


    #Returns the credits consumed by the request made
    # @return string



    def getConsumedCredits(self):
        if ('status' in self._response.keys()):
            if ((self._response['status'] is not None) and ('credits' in self._response['status'].keys())):
                if (self._response['status']['credits'] is not None):
                    return self._response['status']['credits']
                else:
                    return '0'
            else:
                print("Not credits field\n")
        else:
            return None


    #Returns the remaining credits for the license key used after the request was made
    # @return string

    def getRemainingCredits(self):
        if ('status' in self._response.keys()):
            if ((self._response['status'] is not None) and ('remaining_credits' in self._response['status'].keys())):
                if (self._response['status']['remaining_credits'] is not None):
                    return self._response['status']['remaining_credits']
                else:
                    return ''
            else:
                print("Not remaining credits field\n")
        else:
            return None


    # Returns the results from the API without the status of the request
    # @return string

    def getResults(self):
        results = self._response.copy()
        if ('status' in self._response.keys()):
            if results['status'] is not None:
                del results['status']
            return results
        else:
            return None

    # Returns the response frome the API
    # @return string


    def getResponse(self):
        return self._response

    # Returns the response from de API as a string
    # @return string

    def getStrResponse(self):
        return self.__strResponse
