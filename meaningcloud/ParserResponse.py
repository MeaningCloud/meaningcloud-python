import meaningcloud.Response


class ParserResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        ParserResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")

        meaningcloud.Response.__init__(self, response)

    # This function obtains the lemmas and PoS for the text sent
    # @param boolean fullPOSTag set to true to obtain the complete PoS tag
    # @return array of tokens from the syntactic tree with their lemmas and PoS
    def getLemmatization(self, fullPOSTag=False):
        """
        This function obtains the lemmas and PoS for the text sent

        :param fullPOSTag:
            Set to true to obtain the complete PoS tag
        :return:
            Dictionary of tokens from the syntactic tree with their lemmas and PoS
        """

        leaves = self._getTreeLeaves()
        lemmas = {}
        for leaf in leaves:
            analyses = []
            if 'analysis_list' in leaf.keys():
                for analysis in leaf['analysis_list']:
                    analyses.append({
                        'lemma': analysis['lemma'],
                        'pos': analysis['tag'] if fullPOSTag else analysis['tag'][:2]
                    })
            lemmas[leaf['form']] = analyses

        return lemmas

    def _getTreeLeaves(self):
        if 'token_list' in self._response.keys():
            leaves = []
            for sentence in self._response['token_list']:
                self._traverseTree(sentence, leaves)

            return leaves

    def _traverseTree(self, token, leaves):
        if 'token_list' in token.keys():
            for t in token['token_list']:
                if 'token_list' in t.keys():
                    self._traverseTree(t, leaves)
                else:
                    leaves.append(t)
