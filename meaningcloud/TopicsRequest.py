import meaningcloud.Request


class TopicsRequest(meaningcloud.Request):

    URL = 'https://api.meaningcloud.com/topics-2.0'
    otherparams = None
    extraheaders = None
    type_ = ""

    # TopicsRequest constructor
    # @param string url URL of the API against which the request will be made
    # @param string key license key
    # @param string lang . Language used in the request
    # @param string txt . Text to use in the API calls
    # @param string url . Text to use in the API calls
    # @param string doc . Text to use in the API calls
    # @param string txtf . Format of the text
    # @params array otherparams . Array where can be added other params to use in the API call
    # @params array extraheaders . Array where can be added other headers used in the request

    def __init__(self, key, txt=None, doc=None, url =None, lang=None, topicType="a", otherparams=None, extraheaders=None):
        self._params = {}
        meaningcloud.Request.__init__(self, self.URL, key)
        self.otherarams = otherparams
        self.extraheaders = extraheaders
        self._url = self.URL

        self.addParam('key', key)
        self.addParam('lang', lang)
        self.addParam('tt',topicType)

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
        if(otherparams):
            for key in otherparams:
                self.addParam(key, otherparams[key])



    def sendReq(self):

        return self.sendRequest(self.extraheaders)
