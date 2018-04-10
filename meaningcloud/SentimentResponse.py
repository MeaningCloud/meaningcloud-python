import meaningcloud.Response


class SentimentResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        SentimentResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

    # Getters for the different objects returned

    def getModel(self):
        """
        Obtains the sentiment model used to obtain the response

        :return:
            Identifier of the model
        """

        return (self._response['model']
                if (('model' in self._response.keys()) and (self._response['model'] is not None))
                else "")

    def getGlobalScoreTag(self):
        """
        Obtains the global score tag of the response

        :return:
            Global score tag
        """

        return self.getScoreTag(self._response)

    def getScoreTag(self, node):
        """
        Obtains the score tag field of a node (if it applies)

        :param node:
            Node you want to obtain the score tag from
        :return:
            Score tag of the node
        """

        return (node['score_tag']
                if (('score_tag' in node.keys()) and (node['score_tag'] is not None))
                else "")

    def getGlobalAgreement(self):
        """
        Obtains the global agreement of the response

        :return:
            Global agreement
        """

        return (self.getAgreement(self._response))

    def getAgreement(self, node):
        """
        Obtains the agreement field of a node (if it applies)

        :param node:
            Node you want to obtain the agreement from
        :return:
            Agreement of the node
        """

        return (node['agreement']
                if (('agreement' in node.keys()) and (node['agreement'] is not None))
                else "")

    def getSubjectivity(self):
        """
        Obtains the global subjectivity of the response

        :return:
            Global subjectivity
        """

        return (self._response['subjectivity']
                if (('subjectivity' in self._response.keys()) and (self._response['subjectivity'] is not None))
                else "")

    def getGlobalConfidence(self):
        """
        Obtains the global confidence of the response

        :return:
            Global confidence
        """

        return (self.getConfidence(self._response))

    def getConfidence(self, node):
        """
        Obtains the confidence field of a node (if it applies)

        :param node:
            Node you want to obtain the confidence from
        :return:
            Confidence of the node
        """
        return (node['confidence']
                if (('confidence' in node.keys()) and (node['confidence'] is not None))
                else "")

    def getIrony(self):
        """
        Obtains the global irony of the response

        :return:
            Global irony
        """

        return (self._response['irony']
                if (('irony' in self._response.keys()) and (self._response['irony'] is not None))
                else "")

    def getGlobalSentimentedEntities(self):
        """
        Obtains the entities identified in the text with the global polarity associated to them

        :return:
            Sentimented entities
        """

        return self.getSentimentedEntities(self._response)

    def getSentimentedEntities(self, node):
        """
        Obtains the entities identified in the text with the polarity associated to them in the node

        :param node:
            Node you want to obtain entities from
        :return:
            Entities of the node
        """

        return (node['sentimented_entity_list']
                if ((len(node) > 0) and ('sentimented_entity_list' in node.keys()) and
                    (node['sentimented_entity_list'] is not None)) else "")

    def getGlobalSentimentedConcepts(self):
        """
        Obtains the concepts identified in the text with the global polarity associated to them

        :return:
            Sentimented concepts
        """

        return self.getSentimentedConcepts(self._response)

    def getSentimentedConcepts(self, node):
        """
        Obtains the concepts identified in the text with the polarity associated to them in the node

        :param node:
            Node you want to obtain concepts from
        :return:
            Concepts of the node
        """

        return (node['sentimented_concept_list']
                if ((len(node) > 0) and ('sentimented_concept_list' in node.keys()) and
                    (node['sentimented_concept_list'] is not None)) else "")

    # Generic auxiliary functions

    def scoreTagToString(self, scoreTag):
        """
        :param scoreTag:
        :return:
        """

        scoreTagToString = ""
        if scoreTag == "P+":
            scoreTagToString = 'strong positive'
        elif scoreTag == "P":
            scoreTagToString = 'positive'
        elif scoreTag == "NEU":
            scoreTagToString = 'neutral'
        elif scoreTag == "N":
            scoreTagToString = 'negative'
        elif scoreTag == "N+":
            scoreTagToString = 'strong negative'
        elif scoreTag == "NONE":
            scoreTagToString = 'no sentiment'

        return scoreTagToString
