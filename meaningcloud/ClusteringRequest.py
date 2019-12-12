import meaningcloud.Request


class ClusteringRequest(meaningcloud.Request):

    endpoint = 'clustering-1.1'
    otherparams = None
    extraheaders = None
    type_ = ""

    def __init__(self, key, lang, texts, mode='tm', otherparams=None, extraheaders=None, server='https://api.meaningcloud.com/'):
        """
        ClusteringRequest constructor

        :param key:
            license key
        :param lang:
            language of the text
        :param txt:
            Collection of texts to cluster. Dictionary expected where the keys are the IDs of the text/doc
        :param mode:
            Clustering algorithm
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
        self.addParam('mode', mode)
        self.addParam('txt', "\r\n".join(val.replace("\r", ' ').replace("\n", " ").replace("\f", " ").replace("\x00", " ").replace("\x01", " ").replace("\x02", " ") for val in texts.values()))
        self.addParam('id', "\r\n".join(texts.keys()))

        if (otherparams):
            for key in otherparams:
                self.addParam(key, otherparams[key])

    def sendReq(self):
        return self.sendRequest(self.extraheaders)
