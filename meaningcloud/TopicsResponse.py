# Created by MeaningCloud Support Team
# Date: 26/02/18

import meaningcloud.Response

class TopicsResponse(meaningcloud.Response):

    #TopicsResponse constructor
    #@param string response string returned by the request
    #@throws \Exception  if the parameters passed are incorrect

    def __init__(self, response):
        if not response:
            raise Exception("The request sent did not return a response")

        meaningcloud.Response.__init__(self, response)


    # Getters for the different types of topics returned

    #@return array with the entities detected

    def getEntities(self):
        return (self._response['entity_list']
                if(('entity_list' in self._response.keys()) and  (self._response['entity_list'] is not None))
                else {})



    #@return array with the concepts detected

    def getConcepts(self):
        return (self._response['concept_list']
                if (('concept_list' in self._response.keys()) and (self._response['concept_list'] is not None))
                else {})



    #@return array with the time expressions detected

    def getTimeExpressions(self):
        return (self._response['time_expression_list']
                if (('time_expression_list' in self._response.keys()) and (self._response['time_expression_list'] is not None))
                else {})



    #@return array with the money expressions detected

    def getMoneyExpressions(self):
        return (self._response['money_expression_list']
                if (('money_expression_list' in self._response.keys()) and (self._response['money_expression_list'] is not None))
                else {})



    #@return array with the other expressions detected

    def getQuantityExpressions(self):
        return (self._response['quantity_expression_list']
                if (('quantity_expression_list' in self._response.keys()) and (self._response['quantity_expression_list'] is not None))
                else {})



    #@return array with the other expressions detected

    def getOtherExpressions(self):
        return (self._response['other_expression_list']
                if (('other_expression_list' in self._response.keys()) and (self._response['other_expression_list'] is not None))
                else {})



    #@return array with the quotations detected

    def getQuotations(self):
        return (self._response['quotation_list']
                if (('quotation_list' in self._response.keys()) and (self._response['quotation_list'] is not None))
                else {})




    #@return array with the relations detected

    def getRelations(self):
        return (self._response['relation_list']
                if (('relation_list' in self._response.keys()) and (self._response['relation_list'] is not None))
                else {})



    #Generic auxiliary functions


    # @param array topic
    # @return string

    def getTopicForm(self, topic):
        return (topic['form']
                if (('form' in topic.keys()) and (topic['form'] is not None))
                else "")



    # @param array topic
    # @return string

    def getTopicRelevance(self, topic):
        return (topic['relevance']
                if (('relevance' in topic.keys()) and (topic['relevance'] is not None))
                else "")




    #Obtains the ontology type of a topic (if it applies)
    # @param array topic
    # @returns string


    def getOntoType(self, topic):
        return (topic['sementity']['type']
                if (('sementity' in topic.keys()) and ('type' in topic['sementity'].keys()) and (topic['sementity']['type'] is not None))
                else "")





    # Obtain the last node or leaf of the type specified
    # @param string $type type we want to analyze (sementity, semtheme)
    # @return string

    def getTypeLastNode(self, type_):
        lastNode = ""
        if ((type_) and (type(type_) is not list) and (type(type_) is not dict)):
            aType = type_.split('>')
            lastNode = aType[len(aType) - 1]
        return lastNode





    # Gets the number of appearances of a topic
    # @param array $topic
    # @return int number of appearances


    def getNumberOfAppearances(self, topic):
        if topic is not None:
            if('variant_list' in topic.keys()) and (topic['variant_list'] is not None):
                return len(topic['variant_list'])
            else:
                return 1;
        else:
            return 0





    # Checks the field "dictionary" to check if a entity/concept comes from a user dictionary
    # @param $topic
    # @return bool true if the field dictionary is in the topic

    def isUserDefined(self, topic):
        if (('dictionary' in topic.keys()) and (topic['dictionary'])):
            return True
        else:
            return False