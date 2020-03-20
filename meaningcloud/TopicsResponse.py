import meaningcloud.Response


class TopicsResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        TopicsResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")

        meaningcloud.Response.__init__(self, response)

    # Getters for the different types of topics returned

    def getEntities(self):
        """
        Obtains the entities detected in the text

        :return:
            Entities
        """

        return (self._response['entity_list']
                if(('entity_list' in self._response.keys()) and (self._response['entity_list'] is not None))
                else {})

    def getConcepts(self):
        """
        Obtains the concepts detected in the text

        :return:
            Concepts
        """

        return (self._response['concept_list']
                if (('concept_list' in self._response.keys()) and (self._response['concept_list'] is not None))
                else {})

    def getTimeExpressions(self):
        """
        Obtains the time expressions detected in the text

        :return:
            Time expressions
        """

        return (self._response['time_expression_list']
                if (('time_expression_list' in self._response.keys()) and
                    (self._response['time_expression_list'] is not None)) else {})

    def getMoneyExpressions(self):
        """
        Obtains the money expressions detected in the text

        :return:
            Money expressions
        """

        return (self._response['money_expression_list']
                if (('money_expression_list' in self._response.keys()) and
                    (self._response['money_expression_list'] is not None)) else {})

    def getQuantityExpressions(self):
        """
        Obtains the quantity expressions detected in the text

        :return:
            Quantity expressions
        """

        return (self._response['quantity_expression_list']
                if (('quantity_expression_list' in self._response.keys()) and
                    (self._response['quantity_expression_list'] is not None)) else {})

    def getOtherExpressions(self):
        """
        Obtains other expressions detected in the text

        :return:
            Other expressions
        """

        return (self._response['other_expression_list']
                if (('other_expression_list' in self._response.keys()) and
                    (self._response['other_expression_list'] is not None)) else {})

    def getQuotations(self):
        """
        Obtains quotations detected in the text

        :return:
            Quotations
        """

        return (self._response['quotation_list']
                if (('quotation_list' in self._response.keys()) and (self._response['quotation_list'] is not None))
                else {})

    def getRelations(self):
        """
        Obtains relations detected in the text

        :return:
            Relations
        """

        return (self._response['relation_list']
                if (('relation_list' in self._response.keys()) and (self._response['relation_list'] is not None))
                else {})

    # Generic auxiliary functions

    def getTopicForm(self, topic):
        """
        Obtains the form of a topic

        :param topic:
            Topic to obtain the form from
        :return:
            Topic form
        """

        return (topic['form']
                if (('form' in topic.keys()) and (topic['form'] is not None))
                else "")

    def getTopicRelevance(self, topic):
        """
        Obtains the relevance of a topic

        :param topic:
            Topic to obtain the relevance from
        :return:
            Topic relevance
        """

        return (topic['relevance']
                if (('relevance' in topic.keys()) and (topic['relevance'] is not None))
                else "")

    def getOntoType(self, topic):
        """
        Obtains the ontology type of a topic (if it applies)

        :param topic:
            Topic to obtain the ontology type from
        :return:
            Topic ontology type
        """

        return (topic['sementity']['type']
                if (('sementity' in topic.keys()) and ('type' in topic['sementity'].keys()) and
                    (topic['sementity']['type'] is not None)) else "")

    def getTypeLastNode(self, type_):
        """
        Obtains the last node or leaf of the type specified

        :param type_:
            Type we want to analize (sementity, semtheme)
        :return:
            Last node of the type
        """

        lastNode = ""
        if type_ and (type(type_) is not list) and (type(type_) is not dict):
            aType = type_.split('>')
            lastNode = aType[len(aType) - 1]
        return lastNode

    def getTypeFirstNode(self, type_):
        """
        Obtains the firstlevel node of the type specified
        :param type_:
            Type we want to analize (sementity, semtheme)
        :return:
            First node of the type (or Top if there's no first type)
        """

        firstNode = ""
        if type_ and (type(type_) is not list) and (type(type_) is not dict):
            aType = type_.split('>')
            firstNode = aType[1] if len(aType)>1 else aType[0]
        return firstNode

    def getNumberOfAppearances(self, topic):
        """
        Gets the number of appearances of a topic

        :param topic:
            Topic to analyze
        :return:
            Number of appearances
        """

        if topic is not None:
            if('variant_list' in topic.keys()) and (topic['variant_list'] is not None):
                return len(topic['variant_list'])
            else:
                return 1
        else:
            return 0

    def isUserDefined(self, topic):
        """
        Checks the field 'dictionary' to check if an entity/concept comes from a user dictionary

        :param topic:
            Topic to analyze
        :return:
            Boolean indicating if the topic comes from a user dictionary
        """

        if ('dictionary' in topic.keys()) and (topic['dictionary']):
            return True
        else:
            return False
