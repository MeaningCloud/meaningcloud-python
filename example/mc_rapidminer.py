# Created by MeaningCloud Support Team
# Copyright 2020 MeaningCloud LLC
# Date: 23/02/2020

import sys
import os
import meaningcloud
import pandas as pd

# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = '<<<your license key>>>'

# @param text_column - Name of the column where the texts will be
text_column = 'Review'


# auxiliary variables to follow progress of the process
index_count = 1


# Analyzes the text passed as a parameter
def analyzeText(text):
    global index_count
    print("Analyzing text " + str(index_count))


    # this is where we are going to store our results
    polarity = ''
    entities = ''
    concepts = ''
    iab2 = ''

    try:
        # We are going to make a request to the Sentiment Analysis API
        print("\tGetting sentiment analysis...")
        sentiment_response = meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(license_key, lang='en', txt=text, txtf='markup').sendReq())
        if sentiment_response.isSuccessful():
            polarity = sentiment_response.getGlobalScoreTag()
        else:
            print('Request to sentiment was not succesful: ' + sentiment_response.getStatusMsg())


        # We are going to make a request to the Topics Extraction API
        print("\tGetting entities and concepts...") 
        topics_req = meaningcloud.TopicsRequest(license_key, txt=text, lang='en', topicType='ec', otherparams={'txtf':'markup'})
        topics_response = meaningcloud.TopicsResponse(topics_req.sendReq())

        # If there are no errors in the request, we extract the entities and concepts
        if topics_response.isSuccessful():
            entities_list = topics_response.getEntities()
            formatted_entities = []
            if entities_list:
                for entity in entities_list:
                    if int(topics_response.getTopicRelevance(entity)) >= 100: #we limit the entities to those with relevance higher than 100
                        formatted_entities.append(topics_response.getTopicForm(entity) + ' (' + topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + ')')
                entities = ', '.join(formatted_entities)

            concepts_list = topics_response.getConcepts()
            formatted_concepts = []
            if concepts_list:
                for concept in concepts_list:
                    if int(topics_response.getTopicRelevance(concept)) >= 100: #we limit the entities to those with relevance higher than 100
                        formatted_concepts.append(topics_response.getTopicForm(concept))

                concepts = ', '.join(list(dict.fromkeys(formatted_concepts)))
        else:
            print('Request to topics was not succesful: ' + topics_response.getStatusMsg())


        # We are going to make a request to the Deep Categorization API
        print("\tGetting IAB 2.0 classification...")
        deepcat_response = meaningcloud.DeepCategorizationResponse(meaningcloud.DeepCategorizationRequest(license_key, model='IAB_2.0_en', txt=text, otherparams={'txtf':'markup'}).sendReq())    
        if deepcat_response.isSuccessful():
            categories = deepcat_response.getCategories()
            iab2 = (', '.join(deepcat_response.getCategoryCode(cat) for cat in categories[:1])) if categories else ''
        else:
            print('Request to Deep Categorization was not succesful: ' + deepcat_response.getStatusMsg())

    except ValueError:
        e = sys.exc_info()[0]
        print("\nException: " + str(e))

    index_count += 1

    return pd.Series([polarity, entities, concepts, iab2])



############# Main flow ######################


# Flow when it's run from RapidMiner
def rm_main(data):
    print('Number ot texts to analyze: ' + str(len(data)))
    index = 0
    results = data    

    #create pandas data frame from the given dictionary
    df = pd.DataFrame(data)

    # check if data frame creation worked
    if not isinstance(df, pd.DataFrame):
        print("ERROR: Conversion to data frame failed.")
        return;

    if not text_column in df:
        print('ERROR: The column configured does not exist in the data input!')
        return;

    # main analysis
    label_list = ['Polarity', 'Entities', 'Concepts', 'IAB2']
    df[label_list] = df[text_column].apply(analyzeText)
  

    # connect output ports to see the results
    return df