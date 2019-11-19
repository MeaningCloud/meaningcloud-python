# Created by MeaningCloud Support Team
# Copyright 2019 MeaningCloud LLC
# Date: 12/11/2019

import sys
import meaningcloud
import os
import pandas as pd


# This script illustrates how the different functionalities provided by MeaningCloud can be used and combined to extract
# information from a collection of files. The script receives as input a folder that contains files with plain text (UTF-8)
# and results in two CSV files, one with analyses for each one of the texts and another one with the result of clustering
# the files in the folder. Progress of the process will be shown through the console (stout)


############ CONFIGURATION ############
# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = '<<<<< your license key >>>>>'
# @param get_fibo - Determines if the analysis will get FIBO concepts. Access to the pack is needed: https://www.meaningcloud.com/developer/documentation/vertical-packs#financial_industry
get_fibo = True
# @param number_categories - Number of categories to show in the results in Deep Categorization and Text Classification analysis
number_categories = 3
# @param topics_relevance - Relevance used for filtering entities and concepts
topics_relevance = 80

# auxiliary variables to follow progress of the process
index_count = 1
total_files = None


############## FUNCTIONS ##############

# Calls Sentiment Analysis and returns the global polarity for the text
def getSentimentAnalysis(text):
    polarity = ''
    # We are going to make a request to the Sentiment Analysis API
    print("\tGetting sentiment analysis...")
    sentiment_response = meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(license_key, lang='en', txt=text, txtf='markup').sendReq())
    if sentiment_response.isSuccessful():
        polarity = sentiment_response.getGlobalScoreTag()
    else:
        print("\tOops! Request to sentiment was not succesful: (" + sentiment_response.getStatusCode() + ') ' + sentiment_response.getStatusMsg())
    return polarity


# Calls Language Detection and returns the code or name for the text
def detectLanguage(text, get_name=False):
    language = ''
    # We are going to make a request to the Language Identification API
    print("\tDetecting language...")
    lang_response = meaningcloud.LanguageResponse(meaningcloud.LanguageRequest(license_key, txt=text).sendReq())
    if lang_response.isSuccessful():
        langs = lang_response.getLanguages()
        if langs:
            language = lang_response.getLanguageCode(langs[0]) if not get_name else lang_response.getLanguageName(langs[0])
    else:
        print("\tOops! Request to detect language was not succesful: (" + lang_response.getStatusCode() + ') ' + lang_response.getStatusMsg())
    return language


# Calls Topics Extraction and returns the entities, concepts and fibo concepts if cofigured
def extractTopics(text, fibo, relevance):
    
    entities = ''
    concepts = ''
    if fibo:
        fibo_concepts = ''

    print("\tGetting entities and concepts...") 
    topics_req = meaningcloud.TopicsRequest(license_key, txt=text, lang='en', topicType='ec', otherparams={'txtf':'markup'})
    if fibo:
        topics_req.addParam('ud', 'FIBO_en')
        
    topics_response = meaningcloud.TopicsResponse(topics_req.sendReq())

    # If there are no errors in the request, we extract the entities and concepts
    if topics_response.isSuccessful():
        entities_list = topics_response.getEntities()
        formatted_entities = []
        if entities_list:
            for entity in entities_list:
                if int(topics_response.getTopicRelevance(entity)) >= relevance: #we limit the entities to those with relevance higher than 80
                    formatted_entities.append(topics_response.getTopicForm(entity) + ' (' + topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + ')')
            entities = ', '.join(formatted_entities)
        else:
            entities = '(none)'

        concepts_list = topics_response.getConcepts()
        formatted_concepts = []
        formatted_fibo_concepts = []
        if concepts_list:
            for concept in concepts_list:
                if fibo and 'dictionary' in concept.keys() and concept['dictionary'] == 'FIBO_en':
                    formatted_fibo_concepts.append(topics_response.getTopicForm(concept) + ' (' + topics_response.getTypeLastNode(topics_response.getOntoType(concept)) + ')')
                #we limit the concepts to those with relevance higher than 80 or multiwords, or user defined concepts
                elif int(topics_response.getTopicRelevance(concept)) >= relevance  or (' ' in topics_response.getTopicForm(concept) and int(topics_response.getTopicRelevance(concept)) >= (relevance/2)) or topics_response.isUserDefined(concept):
                    formatted_concepts.append(topics_response.getTopicForm(concept) + ' (' + topics_response.getTypeLastNode(topics_response.getOntoType(concept)) + ')')

            concepts = ', '.join(formatted_concepts) if formatted_concepts else '(none)'
            fibo_concepts = ', '.join(formatted_fibo_concepts) if formatted_fibo_concepts else '(none)'
        else:
            concepts = "(none)"
            fibo_concepts = "(none)"
    else:            
        print("\tOops! Request to topics was not succesful: (" + topics_response.getStatusCode() + ') ' + topics_response.getStatusMsg())


    return entities, concepts, fibo_concepts if fibo else entities, concepts

            
# Calls Deep Categorization for a given model and returns the label and relevance of the categories
def getDeepCategorization(text, model, num_cats):
    # We are going to make a request to the Deep Categorization API
    formatted_categories = ''
    print("\tGetting " + model[0:len(model) - 3].replace('_', ' ') + " analysis...")
    deepcat_response = meaningcloud.DeepCategorizationResponse(meaningcloud.DeepCategorizationRequest(license_key, model=model, txt=text).sendReq())
    if deepcat_response.isSuccessful():
        categories = deepcat_response.getCategories()
        formatted_categories = (', '.join(deepcat_response.getCategoryLabel(cat) + ' (' + deepcat_response.getCategoryRelevance(cat) +')' for cat in categories[:num_cats])) if categories else '(none)'
    else:
        print("\tOops! Request to Deep Categorization was not succesful: (" + deepcat_response.getStatusCode() + ') ' + deepcat_response.getStatusMsg())

    return formatted_categories


# Calls Text Classification for a specific model and returns the label and relevance of the categories
def getTextClassification(text, model, num_cats):
    formatted_categories = ''
    print("\tGetting " + model[0:len(model) - 3].replace('_', ' ')+ " analysis...")
    class_response = meaningcloud.ClassResponse(meaningcloud.ClassRequest(license_key, txt=text, model=model, otherparams={'txtf': 'markup'}).sendReq())
    if class_response.isSuccessful():
        categories = class_response.getCategories()
        formatted_categories = (', '.join(class_response.getCategoryLabel(cat) + ' (' + class_response.getCategoryRelevance(cat) +')' for cat in categories[:num_cats])) if categories else '(none)'
    else:
        print("\tOops! The request to Text Classification was not succesful: (" + class_response.getStatusCode() + ') ' + class_response.getStatusMsg())

    return formatted_categories


# Calls Summarization and obtains an extractive summary with the number of sentences especified
def getSummarization(text, sentences):
    # We are going to make a request to the Summarization API
    summary = ''
    print("\tGetting automatic summarization...")
    summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest(license_key, sentences=sentences, txt=text).sendReq())
    if summarization_response.isSuccessful():
        summary = summarization_response.getSummary()
    else:
        print("\tOops! Request to Summarization was not succesful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())

    return summary


# This function obtains the text clustering of the text collection passed as a parameter
def getClustering(text_collection):

    # We are going to make a request to the Clustering API
    print("Getting clustering analysis...")
    clustering_response = meaningcloud.ClusteringResponse(meaningcloud.ClusteringRequest(license_key, lang='en', texts=text_collection).sendReq())
    if clustering_response.isSuccessful():
        clusters = clustering_response.getClusters()
        titles = [clustering_response.getClusterTitle(cl) for cl in clusters]
        sizes = [clustering_response.getClusterSize(cl) for cl in clusters]
        scores = [clustering_response.getClusterScore(cl) for cl in clusters]
        docs = [', '.join(cl['document_list'].keys()) for cl in clusters]
        return titles, sizes, scores, docs
    else:
        print('Request to clustering was not succesful: (' + clustering_response.getStatusCode() + ') ' + clustering_response.getStatusMsg())
        return [], [], [], []
    

# Analyzes the text passed as a parameter
def analyzeText(text, fibo=False):
    # this is where we are going to store our results
    global index_count    

    print("Analyzing file " + str(index_count) + " of "+ str(total_files))
    index_count += 1

    try:
        # We are going to make a request to the Language Identification API
        language = detectLanguage(text, get_name=True)

        # We are going to make a request to the Sentiment Analysis API
        polarity = getSentimentAnalysis(text)

        # We are going to make a request to the Topics Extraction API
        topics = extractTopics(text, fibo, topics_relevance)
        entities = topics[0]
        concepts = topics[1]
        if fibo:
            fibo_concepts = topics[2]

        # We are going to make a request to the Deep Categorization API
        iab2 = getDeepCategorization(text, 'IAB_2.0_en', number_categories)

        # We are going to make a request to the Text Classification API
        iptc = getTextClassification(text, 'IPTC_en', number_categories)

        # We are going to make a request to the Summarization API
        summary = getSummarization(text, 3)

    except ValueError:
        e = sys.exc_info()[0]
        print("\nException: " + str(e))

    if fibo:
        return pd.Series([polarity, language, entities, concepts, fibo_concepts, iab2, iptc, summary])
    else:
        return pd.Series([polarity, language, entities, concepts, iab2, iptc, summary])



###################### Main flow ######################
# Flow when the script is run from the command line
if __name__ == "__main__":

    # checks the args needed
    if len(sys.argv)<=2:
        print("\nusage: mc_showcase.py <input_files_folder> <output_files_name>\n")
        exit()

    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    
    # read files
    input_files = {}
    for file_name in os.listdir('./' + input_folder):
        f = open(input_folder + '/' + file_name, 'r', encoding='utf-8', errors='ignore')
        if f.mode == 'r':
            input_files[file_name] = f.read()
    
    total_files = len(input_files)


    print(str(total_files) + " files read from '" + input_folder + "'")

    # Process texts
    df = pd.DataFrame({'Text': input_files})
    label_list = ['Polarity', 'Language', 'Entities', 'Concepts', 'FIBO_concepts', 'IAB2', 'IPTC', 'Summary'] if get_fibo else ['Polarity', 'Language', 'Entities', 'Concepts', 'IAB2', 'IPTC', 'Summary']
    df[label_list] = df['Text'].apply(analyzeText, fibo=get_fibo)
    df.to_csv('./' + output_file + '.csv', index_label='File_name')
    print("Results printed to '"+ output_file + ".csv'!")
    # print(df)


    # Cluster all files
    resulting_clusters = getClustering(input_files)
    df_clusters = pd.DataFrame( {'Cluster_Name': resulting_clusters[0], 'Size': resulting_clusters[1], 'Score': resulting_clusters[2], 'Documents': resulting_clusters[3]})
    df_clusters.to_csv('./' + output_file + '_clusters.csv', index_label='Cluster_ID')
    print("Clustering results printed to '"+ output_file + "_clusters.csv'!")
    # print(df_clusters)
