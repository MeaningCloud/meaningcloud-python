# Created by MeaningCloud Support Team
# Date: 26/02/18

import requests
import sys
if(sys.version_info.major < 3):
    from urllib import urlencode
elif (sys.version_info.major == 3):
    from urllib.parse import urlencode

class Request:
    # @var int
    _timeout = 60
    # @var string
    _url = ""
    # @var string
    _key = ""
    # @ var array
    _params = {}

    CONTENT_TYPE_TXT = 'txt'
    CONTENT_TYPE_URL = 'url'
    CONTENT_TYPE_FILE = 'doc'


    # Request constructor
    # @param string url URL of the API against which the request will be made
    # @param string key license key
    # @throws \Exception if the parameters passed are incorrect

    def __init__(self, url, key):
        if not url or not key:
            raise ValueError ("URL and key cannot be empty")
        self._url = url
        self._key = key
        self.addParam('key',key)




    # Add a parameter to the request.
    # @param string $paramName name of the parameter
    # @param string $paramValue value of the parameter
    # @throws \Exception if the parameters passed are incorrect


    def addParam(self,paramName, paramValue):
        if not paramName:
            raise ValueError('paramName cannot be empty')
        self._params[paramName]=paramValue



    # Sets the content that's going to be sent to analyze according to its type.

    # @param string $type with the type of content (text, file or url)
    # @param string $value value of the content

    def setContent(self, type_, value):
        if type_ in [self.CONTENT_TYPE_TXT, self.CONTENT_TYPE_URL,
                     self.CONTENT_TYPE_FILE]:
            if type_ == self.CONTENT_TYPE_FILE:
                self.addParam('doc',open(value,'rb'))
            else:
                self.addParam(type_, value)


    # Sets a text content to send to the API.
    # @param string txt

    def setContentTxt(self, txt):
        self.setContent(self.CONTENT_TYPE_TXT, txt)




    # Sets a URL content to send to the API.
    # @param url

    def setContentUrl(self, url):
        self.setContent(self.CONTENT_TYPE_URL, url)





    # Sets a File content to send to the API.
    # @param file

    def setContentFile(self, file):
        self.setContent(self.CONTENT_TYPE_FILE, file)



    # Sends a request to the URL specified and returns a response only if the HTTP code returned is OK
    # @param array extraHeaders allows to configure additional headers in the request
    # @return Response object set to None if there is an error


    def sendRequest(self, extraHeaders=""):
        params = urlencode(self._params)
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        url = self._url
        if ((extraHeaders is not None) and(extraHeaders is dict)):
            headers = headers.update(extraHeaders)

        result = requests.request("POST", url=url, data=params, headers=headers)
        return result


    # Getters and Setters

    # Get the url of the request
    # @return string with the url

    def getUrl(self):
        return self._url



    # Set a new URL
    # @param string $url

    def setUrl(self, url):
        self._url = url



    # Get the params attribute
    # @return array

    def getParams(self):
        return self._params




    # Get the timeout value
    # @return integer

    def getTimeout(self):
        return self._timeout



    # Set a new timeout value
    # @param integer $timeout

    def setTimeout(self, timeout):
        self._timeout = timeout