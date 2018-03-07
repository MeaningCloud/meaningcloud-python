import meaningcloud.Request


class ClassRequest(meaningcloud.Request):

    URL = 'https://api.meaningcloud.com/class-1.1'
    otherparams = None
    extraheaders = None
    type_ = ""

    # ClassRequest constructor
    # @param string url URL of the API against which the request will be made
    # @param string key license key
    # @param string txt . Text to use in the API calls
    # @param string url . Url to use in the API calls
    # @param string doc . File to use in the API calls
    # @param string model . Name of the model to use in the classification
    # @params array otherparams . Array where can be added other params to use in the API call
    # @params array extraheaders . Array where can be added other headers used in the request

    def __init__(self, key, txt=None,url=None, doc=None, model='IPTC_en', otherparams=None, extraheaders=None):
        self._params = {}
        meaningcloud.Request.__init__(self, self.URL, key)
        self.otherarams = otherparams
        self.extraheaders = extraheaders
        self._url = self.URL


        self.addParam('key', key)
        self.addParam('model', model)

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