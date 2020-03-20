import meaningcloud.Response


class LanguageResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        LanguageResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

    # Getters for the different objects returned
    def getLanguages(self):
        """
        Get languages from the analyzed text

        :return:
            Array with the languages detected
        """

        return (self._response['language_list']
                if (('language_list' in self._response.keys()) and (self._response['language_list'] is not None))
                else {})

    def getFirstLanguage(self):
        """
        Get first language returned for the analyzed text

        :return:
            Array with the field of the language detected
        """

        languages = (self._response['language_list']
                if (('language_list' in self._response.keys()) and (self._response['language_list'] is not None))
                else {})
        return languages[0] if((len(languages) > 0) and (languages[0] is not None)) else []

    def getLanguageCode(self, language):
        """
        Get the code of a language

        :param language:
            Language you want the code from
        :return:
            Language code
        """

        return (language['language']
                if ((len(language) > 0) and ('language' in language.keys()) and (language['language'] is not None))
                else "")

    def getLanguageName(self, language):
        """
        Get the name of a language

        :param language:
            Language you want the name from
        :return:
            Language name
        """

        return (language['name']
                if ((len(language) > 0) and ('name' in language.keys()) and (language['name'] is not None))
                else "")
