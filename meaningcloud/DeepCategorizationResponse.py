import meaningcloud.Response


class DeepCategorizationResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        DeepCategorizationResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

    def getCategories(self):
        """
        Get categories from the analyzed text

        :return:
            Array with the categories detected
        """

        return (self._response['category_list']
                if (('category_list' in self._response.keys()) and (self._response['category_list'] is not None))
                else {})

    # Generic auxiliary functions

    def getCategoryCode(self, category):
        """
        Get the code of a category

        :param category:
            Category you want the code from
        :return:
            Category code
        """

        return (category['code']
                if ((len(category) > 0) and ('code' in category.keys()) and (category['code'] is not None))
                else "")

    def getCategoryLabel(self, category):
        """
        Get the label of a category

        :param category:
            Category you want the label from
        :return:
            Category label
        """

        return (category['label']
                if ((len(category) > 0) and ('label' in category.keys()) and (category['label'] is not None))
                else "")

    def getCategoryAbsRelevance(self, category):
        """
        Get the absolute relevance of a category

        :param category:
            Category you want the abs_relevance from
        :return:
            Category abs_relevance
        """

        return (category['abs_relevance']
                if ((len(category) > 0) and ('abs_relevance' in category.keys()) and
                    (category['abs_relevance'] is not None))
                else "")

    def getCategoryRelevance(self, category):
        """
        Get the relevance of a category

        :param category:
            Category you want the relevance from
        :return:
            Category relevance
        """

        return (category['relevance']
                if ((len(category) > 0) and ('relevance' in category.keys()) and (category['relevance'] is not None))
                else "")

    def getCategoryPolarity(self, category):
        """
        Get the polarity of a category

        :param category:
            Category you want the polarity from
        :return:
            Category relevance
        """

        return (category['polarity']
                if ((len(category) > 0) and ('polarity' in category.keys()) and (category['polarity'] is not None))
                else "")