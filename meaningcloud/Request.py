import requests
import sys
if sys.version_info.major < 3:
    from urllib import urlencode
elif sys.version_info.major == 3:
    from urllib.parse import urlencode


class Request:
    _timeout = 60
    _url = ""
    _key = ""
    _params = {}

    _file = {}

    CONTENT_TYPE_TXT = 'txt'
    CONTENT_TYPE_URL = 'url'
    CONTENT_TYPE_FILE = 'doc'

    def __init__(self, url, key):
        """
        Request constructor

        :param url:
            URL of the API against which the request will be made
        :param key:
            License key
        """

        if not url or not key:
            raise ValueError("URL and key cannot be empty")
        self._url = url
        self._key = key
        self.addParam('key', key)

    def addParam(self, paramName, paramValue):
        """
        Add a parameter to the request

        :param paramName:
            Name of the parameter
        :param paramValue:
            Value of the parameter
        """

        if not paramName:
            raise ValueError('paramName cannot be empty')
        self._params[paramName] = paramValue

    def setContent(self, type_, value):
        """
        Sets the content that's going to be sent to analyze according to its type

        :param type_:
            Type of the content (text, file or url)
        :param value:
            Value of the content
        """

        if type_ in [self.CONTENT_TYPE_TXT, self.CONTENT_TYPE_URL,
                     self.CONTENT_TYPE_FILE]:
            if type_ == self.CONTENT_TYPE_FILE:
                self._file = {}
                self._file = {'doc': open(value, 'rb')}
            else:
                self.addParam(type_, value)

    def setContentTxt(self, txt):
        """
        Sets a text content to send to the API

        :param txt:
            Text to be sent to the API
        """

        self.setContent(self.CONTENT_TYPE_TXT, txt)

    def setContentUrl(self, url):
        """
        Sets a URL content to send to the API

        :param url:
            URL to be analyzed by the API
        """

        self.setContent(self.CONTENT_TYPE_URL, url)

    def setContentFile(self, file):
        """
        Sets a File content to send to the API.

        :param file:
            File to be sent to the API
        """

        self.setContent(self.CONTENT_TYPE_FILE, file)

    def sendRequest(self, extraHeaders=""):
        """
        Sends a request to the URL specified and returns a response only if the HTTP code returned is OK

        :param extraHeaders:
             Allows to configure additional headers in the request
        :return:
            Response object set to None if there is an error
        """
        if not 'src' in self._params.keys():
            self.addParam('src', 'mc-python')

        params = urlencode(self._params)

        url = self._url

        if 'doc' in self._file.keys():
            headers = {}

            if (extraHeaders is not None) and (extraHeaders is dict):
                headers = headers.update(extraHeaders)

            result = requests.post(url=url, data=self._params, files=self._file, headers=headers)
            result.encoding = 'utf-8'
            return result
        else:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            if (extraHeaders is not None) and (extraHeaders is dict):
                headers = headers.update(extraHeaders)
            result = requests.request("POST", url=url, data=params, headers=headers, timeout=self._timeout)
            result.encoding = 'utf-8'
            return result

    # Getters and Setters

    def getUrl(self):
        """
        Get the url of the request

        :return:
            String with the url
        """

        return self._url

    def setUrl(self, url):
        """
        Set a new URL

        :param url:
            New URL
        """

        self._url = url

    def getParams(self):
        """
        Get the params attribute

        :return:
            params attribute
        """

        return self._params

    def getTimeout(self):
        """
        Get the timeout value

        :return:
            timeout value
        """

        return self._timeout

    def setTimeout(self, timeout):
        """
        Set a new timeout value

        :param timeout:
            New timeout
        """

        self._timeout = timeout

    def getFile(self):
        """
        Get the file attribute

        :return:
            file attribute
        """

        return self._file
