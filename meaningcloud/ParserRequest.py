import meaningcloud.Request


class ParserRequest(meaningcloud.Request):
    URL = 'https://api.meaningcloud.com/parser-2.0'
    otherparams = None
    extraheaders = None
    type_ = ""

    def __init__(self, key, txt=None, doc=None, url=None, lang=None, otherparams=None, extraheaders=None):
        """
        ParserRequest constructor

        :param key:
            License key
        :param txt:
            Text to use in the API calls
        :param doc:
            File to use in the API calls
        :param url:
            Url to use in the API calls
        :param lang:
            Language used in the request
        :param otherparams:
            Array where other params can be added to be used in the API call
        :param extraheaders:
            Array where other headers can be added to be used in the request
        """

        self._params = {}
        meaningcloud.Request.__init__(self, self.URL, key)
        self.otherparams = otherparams
        self.extraheaders = extraheaders
        self._url = self.URL

        self.addParam('key', key)
        self.addParam('lang', lang)

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
