import meaningcloud.Request


class DeepCategorizationRequest(meaningcloud.Request):

    endpoint = 'deepcategorization-1.0'
    otherparams = None
    extraheaders = None
    type_ = ""

    def __init__(self, key, model, txt=None, url=None, doc=None, polarity='n', otherparams=None, extraheaders=None, server='https://api.meaningcloud.com/'):
        """
        DeepCategorizationRequest constructor

        :param key:
            license key
        :param txt:
            Text to use in the API calls
        :param url:
            Url to use in the API calls
        :param doc:
            File to use in the API calls
        :param model:
            Name of the model to use in the classification
        :param polarity:
            Determines if categories will contain an associated polarity value.
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
        self.addParam('model', model)
        self.addParam('polarity', polarity)

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
        if (otherparams):
            for key in otherparams:
                self.addParam(key, otherparams[key])

    def sendReq(self):
        return self.sendRequest(self.extraheaders)
