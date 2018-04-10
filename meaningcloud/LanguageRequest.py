import meaningcloud.Request


class LanguageRequest(meaningcloud.Request):
    URL = 'https://api.meaningcloud.com/lang-2.0'
    otherparams = None
    extraheaders = None
    type_ = ""

    def __init__(self, key, txt=None, url=None, doc=None, otherparams=None, extraheaders=None):
        """
        LanguageRequest constructor

        :param key:
            License key
        :param txt:
            Text to use in the API calls
        :param url:
            Url to use in the API calls
        :param doc:
            File to use in the API calls
        :param otherparams:
            Array where other params can be added to be used in the API call
        :param extraheaders:
            Array where other headers can be added to be used in the request
        """

        self._params = {}
        meaningcloud.Request.__init__(self, self.URL, key)
        self.otherarams = otherparams
        self.extraheaders = extraheaders
        self._url = self.URL

        self.addParam('key', key)

        if txt:
            type_ = 'txt'

        elif doc:
            type_ = 'doc'

        elif url:
            type_ = 'url'

        else:
            type_ = 'default'

        options = {'doc': lambda: self.setContentFile(doc),
                   'url': lambda: self.setContentUrl(url),
                   'txt': lambda: self.setContentTxt(txt),
                   'default': lambda: self.setContentTxt(txt)
                   }
        options[type_]()
        if otherparams:
            for key in otherparams:
                self.addParam(key, otherparams[key])

    def sendReq(self):
        return self.sendRequest(self.extraheaders)
