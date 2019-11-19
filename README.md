# MeaningCloud for Python

This is MeaningCloud's official Python client, designed to enable you to use MeaningCloud's services easily from your own applications.

## MeaningCloud

MeaningCloud is a cloud-based text analytics service that through APIs allows you extract meaning from all kind of unstructured content: social conversation, articles, documents... You can check our demos here: https://www.meaningcloud.com/demos

The different APIs provide easy access to many NLP tasks such as automatic classification, sentiment analysis, topic extraction, etc. To be able to use the service you just have to log into MeaningCloud (by registering or using other services to log in: https://www.meaningcloud.com/developer/login), and you will receive a license key associated to a basic Free plan.

You can read more about the plans and the features available here: https://www.meaningcloud.com/products/pricing


## Getting started

### Installation

You can load meaningcloud-python into your project by using:
```
pip install MeaningCloud-python
```

You can also clone the code and type the following on your shell:

``` 
python setup.py install
```

### Configuration

The only thing you need to start using MeaningCloud's APIs is to log into MeaningCloud (by registering or using other services to log in). Once you've done that, you will be given a license key (https://www.meaningcloud.com/developer/account/subscription). Copy it and paste it in the corresponding place in the code, select the API you want to use and the parameters you want to use, and that's it.

You can find all the technical documentation about the APIs in the API section of the website: https://www.meaningcloud.com/developer/apis

And we are always available at support@meaningcloud.com

### Functionality

This SDK currently contains the following:

- **Request**: manages requests to any of MeaningCloud's APIS. It can also be used to directly generate requests without using specific classes .
    - **ClassRequest**: models a request to MeaningCloud Text Classification API.
    - **ClusteringRequest**: models a request to MeaningCloud Text Clustering API.
    - **DeepCategorizationRequest**: models a request to MeaningCloud Deep Categorization API.
    - **LanguageRequest**: models a request to MeaningCloud Language Identification API.
    - **ParserRequest**: models a request to Meaningcloud Lemmatization, PoS and Parsing API.
    - **SentimentRequest**: models a request to MeaningCloud Sentiment Analysis API.
    - **SummarizationRequest**: models a request to Meaningcloud Summarization API.
    - **TopicsRequest**: models a request to MeaningCloud TopicsExtraction API.
- **Response**: models a generic response from the MeaningCloud API.
    - **ClassResponse**: models a response from the Text Classification API, providing auxiliary functions to work with the response and extract the different fields in each category.
    - **ClusteringResponse**: models a response from the Text Clustering API, providing auxiliary functions to work with the response and extract the different fields in each cluster.
    - **DeepCategorizationResponse**: models a response from the Deep Categorization API, providing auxiliary functions to work with the response and extract the different fields in each category.
    - **LanguageResponse**: models a response from the Language Identification API, providing auxiliary functions to work with the response and extract the sentiment detected at different levels and for different elements.
    - **ParserResponse**: models a response from the Lemmatization, PoS and Parsing API, providing auxiliary functions to work with the response and extract the lemmatization and PoS tagging of the text provided.
    - **SentimentResponse**: models a response from the Sentiment Analysis API, providing auxiliary functions to work with the response and extract the sentiment detected at different levels and for different elements.
    - **SummarizationResponse**: models a response from the Summarization API, providing auxiliary functions to work with the response and obtain the summary extracted.
    - **TopicsResponse**: models a response from the Topic Extraction API, providing auxiliary functions to work with the response, extracting the different types of topics and some of the most used fields in them.
   
### Usage

In the _example_ folder, there are two examples:
- **Client.py**, which contains a simple example on how to use the SDK
- **mc_showcase**, which implements a pipeline where plain text files are read from a folder, and two CSV files result as output: one with several types of analyses done over each text, and the results from running [Text Clustering](https://www.meaningcloud.com/developer/text-clustering) over the complete collection.
    The analyses done are:

  * [Language Identification](https://www.meaningcloud.com/developer/language-identification): detects the language and returns code or name
  * [Sentiment Analysis](https://www.meaningcloud.com/developer/sentiment-analysis): detects the global polarity detected in the text
  * [Topics Extraction](https://www.meaningcloud.com/developer/topics-extraction): detects the most relevant entities and concepts in the text. If the _get_fibo_ variable is enabled, FIBO concepts will be output (requires access to the [Financial Industry pack](https://www.meaningcloud.com/developer/documentation/vertical-packs#financial_industry))
  * [Deep Categorization](https://www.meaningcloud.com/developer/deep-categorization): categorizes the text according to the *IAB 2.0* taxonomy
  * [Text Classification](https://www.meaningcloud.com/developer/text-classification): classifies the text according the *IPTC* taxonomy
  * [Summarization](https://www.meaningcloud.com/developer/summarization): extracts a summary from the text


This is what **Client.py** looks like:

```python
#! /usr/bin/env python

# Created by MeaningCloud Support Team
# Date: 26/02/18

import sys
import meaningcloud

# @param model str - Name of the model to use. Example: "IAB_en" by default = "IPTC_en"
model = 'IAB_en'

# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = '<your_license_key>'

# @param text - Text to use for different API calls
text = 'London is a very nice city but I also love Madrid.'


try:
    # We are going to make a request to the Topics Extraction API
    topics_response =  meaningcloud.TopicsResponse(meaningcloud.TopicsRequest(license_key, txt=text, lang='en', topicType='e').sendReq())

    # If there are no errors in the request, we print the output
    if (topics_response.isSuccessful()):
        print("\nThe request to 'Topics Extraction' finished successfully!\n")

        entities =  topics_response.getEntities()
        if (entities):
            print("\tEntities detected (" + str(len(entities)) + "):\n")
            for entity in entities:
                print("\t\t" + topics_response.getTopicForm(entity) + ' --> ' + topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + "\n")

        else:
            print("\nOh no! There was the following error: " + topics_response.getStatusMsg() + "\n")
    else:
        if(topics_response.getResponse() is None):
            print("\nOh no! The request sent did not return a Json\n")
        else:
            print("\nOh no! There was the following error: " + topics_response.getStatusMsg() + "\n")


    #CLASS API CALL	
    #class_response = meaningcloud.ClassResponse(meaningcloud.ClassRequest(license_key, txt=text, model=model).sendReq())


    #SENTIMENT API CALL
    #sentiment_response = meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(license_key, lang='en', txt=text, txtf='plain').sendReq())


    #GENERIC API CALL
    #generic = meaningcloud.Request(url="url_of_specific_API",key=key)
    #generic.addParam('parameter','value')
    #generic_result = generic.sendRequest()
    #generic_response = meaningcloud.Response(generic_result)


    #We are going to make a request to the Language Identification API
    lang_response = meaningcloud.LanguageResponse(meaningcloud.LanguageRequest(license_key, txt=text).sendReq())

    #If there are no errors in the request, we will use the language detected to make a request to Sentiment and Topics
    if(lang_response.isSuccessful()):
        print("\nThe request to 'Language Identification' finished successfully!\n")

        results = lang_response.getResults()
        if('language_list' in results.keys() and results['language_list']):
            language = results['language_list'][0]['language']
            print("\tLanguage detected: " + results['language_list'][0]['name'] + ' (' + language + ")\n")

    # We are going to make a request to the Lemmatization, PoS and Parsing API
    parser_response = meaningcloud.ParserResponse(
        meaningcloud.ParserRequest(license_key, txt=text, lang='en').sendReq())

    # If there are no errors in the request, print tokenization and lemmatization
    if parser_response.isSuccessful():
        print("\nThe request to 'Lemmatization, PoS and Parsing' finished successfully!\n")
        lemmatization = parser_response.getLemmatization(True)
        print("\tLemmatization and PoS Tagging:\n")
        for token, analyses in lemmatization.items():
            print("\t\tToken -->", token)
            for analysis in analyses:
                print("\t\t\tLemma -->", analysis['lemma'])
                print("\t\t\tPoS Tag -->", analysis['pos'], "\n")


except ValueError:
    e = sys.exc_info()[0]
    print("\nException: " + str(e))
```
