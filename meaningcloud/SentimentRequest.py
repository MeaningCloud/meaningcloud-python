import meaningcloud.Request


class SentimentRequest(meaningcloud.Request):
    endpoint = 'sentiment-2.1'
    otherparams = None
    extraheaders = None
    type_ = ""

    def __init__(self, key, lang=None, txt=None, txtf='plain', url=None, doc=None, otherparams=None, extraheaders=None, server='https://api.meaningcloud.com/'):
        """
        SentimentRequest constructor

        :param key:
            License key
        :param lang:
            Language used in the request
        :param txt:
            Text to use in the API calls
        :param txtf:
            Format of the text
        :param url:
            Url to use in the API calls
        :param doc:
            File to use in the API calls
        :param otherparams:
            Array where other params can be added to be used in the API call
        :param extraheaders:
            Array where other headers can be added to be used in the request
        :param server:
            String with the server the requests will be sent to
        """

        if server[len(server)-1] != '/':
            server += '/'

        self._params = {}
        meaningcloud.Request.__init__(self, (server + self.endpoint), key)

        self.otherarams = otherparams
        self.extraheaders = extraheaders
        self._url = server + self.endpoint

        self.addParam('key', key)
        self.addParam('lang', lang)
        self.addParam('txtf', txtf)

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
