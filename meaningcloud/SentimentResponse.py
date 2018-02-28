# Created by MeaningCloud Support Team
# Date: 26/02/18

import meaningcloud.Response

class SentimentResponse(meaningcloud.Response):

    # TSentimentResponse constructor
    # @param string response string returned by the request
    # @throws \Exception  if the parameters passed are incorrect

    def __init__(self,response):
        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)


    # Getters for the different objects returned

    # Obtains the sentiment model used to obtain the response
    # @return string

    def getModel(self):
        return (self._response['model']
                if (('model' in self._response.keys()) and (self._response['model'] is not None))
                else "")



    # Obtains the global score tag of the response
    # @return string

    def getGlobalScoreTag(self):
        return (self.getScoreTag(self._response))



    # Obtains the score tag field of a node (if it applies)
    # @param array node
    # @return string

    def getScoreTag(self, node):
        return (node['score_tag']
                if (('score_tag' in node.keys()) and (node['score_tag']  is not None))
                else "")





    # Obtains the global agreement of the response
    # @return string

    def getGlobalAgreement(self):
        return (self.getAgreement(self._response))





    # Obtains the agreement field of a node (if it applies)
    # @param array node
    # @return string

    def getAgreement(self, node):
        return (node['agreement']
                if (('agreement' in node.keys()) and (node['agreement'] is not None))
                else "")




    # Obtains the global subjectivity of the response
    # @return string

    def getSubjectivity(self):
        return (self._response['subjectivity']
                if (('subjectivity' in self._response.keys()) and (self._response['subjectivity'] is not None))
                else "")




    # Obtains the global confidence of the response
    # @return string

    def getGlobalConfidence(self):
        return (self.getConfidence(self._response))





    # Obtains the confidence field of a node (if it applies)
    # @param array node
    # @return string

    def getConfidence(self, node):
        return (node['confidence']
                if (('confidence' in node.keys()) and (node['confidence'] is not None))
                else "")




    # Obtains the global irony of the response

    # @return string

    def getIrony(self):
        return (self._response['irony']
                if (('irony' in self._response.keys()) and (self._response['irony'] is not None))
                else "")




    # Obtains the entities identified in the text with the global polarity associated to them

    # @return array

    def getGlobalSentimentedEntities(self):
        return (self.getSentimentedEntities(self._response))





    # Obtains the entities identified in the text with the polarity associated to them in the node
    # @param array node
    # @return array

    def getSentimentedEntities(self, node):
        return (node['sentimented_entity_list']
                if ((len(node)>0) and ('sentimented_entity_list' in node.keys()) and (node['sentimented_entity_list'] is not None))
                else "")




    # Obtains the concepts identified in the text with the global polarity associated to them
    # @param array node
    # @return array

    def getGlobalSentimentedConcepts(self):
                return(self.getSentimentedConcepts(self._response))






    # Obtains the concepts identified in the text with the polarity associated to them in the node
    # @param array node
    # @return array

    def getSentimentedConcepts(self, node):
                return (node['sentimented_concept_list']
                if ((len(node)>0) and ('sentimented_concept_list' in node.keys()) and (node['sentimented_concept_list'] is not None))
                else "")




    # Generic auxiliary functions


    # @param scoreTag
    # return string

    def scoreTagToString(self, scoreTag):
        scoreTagToString = "";
        if(scoreTag == "P+"):
            scoreTagToString = 'strong positive'
        elif(scoreTag == "P"):
            scoreTagToString = 'positive'
        elif(scoreTag == "NEU"):
            scoreTagToString = 'neutral'
        elif(scoreTag == "N"):
            scoreTagToString = 'negative'
        elif(scoreTag == "N+"):
            scoreTagToString = 'strong negative'
        elif(scoreTag == "NONE"):
            scoreTagToString = 'no sentiment'

        return scoreTagToString
