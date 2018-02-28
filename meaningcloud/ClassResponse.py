# Created by MeaningCloud Support Team
# Date: 26/02/18


import meaningcloud.Response



class ClassResponse(meaningcloud.Response):

    # ClassResponse constructor
    # @param string response string returned by the request
    # @throws \Exception  if the parameters passed are incorrect

    def __init__(self,response):
        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)


    # @return array with the categories detected

    def getCategories(self):
        return (self._response['category_list']
                if (('category_list' in self._response.keys()) and (self._response['category_list'] is not None))
                else {})

    # Generic auxiliary functions

    # @param array category
    # @return string

    def getCategoryCode(self, category):
        return (category['code']
                if ((len(category)>0) and ('code' in category.keys()) and (category['code'] is not None))
                else "")

    # @param array category
    # @return string

    def getCategoryLabel(self, category):
        return (category['label']
                if ((len(category)>0) and ('label' in category.keys()) and (category['label'] is not None))
                else "")

    # @param array category
    # @return string

    def getCategoryAbsRelevance(self, category):
        return (category['abs_relevance']
                if ((len(category)>0) and ('abs_relevance' in category.keys()) and (category['abs_relevance'] is not None))
                else "")

    # @param array category
    # @return string

    def getCategoryRelevance(self, category):
        return (category['relevance']
                if ((len(category)>0) and ('relevance' in category.keys()) and (category['relevance'] is not None))
                else "")
