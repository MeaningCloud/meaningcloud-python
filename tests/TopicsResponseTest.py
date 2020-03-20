import unittest
import meaningcloud
import json


class TopicsResponseTest(unittest.TestCase):

    outputOK = '{"status":{"code":"0","msg":"OK","credits":"1"},"entity_list":[{"form":"London","id":"01d0d69c7d","sementity":{"class":"instance","fiction":"nonfiction","id":"ODENTITY_CITY","type":"Top>Location>GeoPoliticalEntity>City"},"semgeo_list":[{"adm1":{"form":"England","id":"98db781864"},"adm2":{"form":"Greater London","id":"ed00f6dec4"},"continent":{"form":"Europe","id":"0404ea4d6c"},"country":{"form":"United Kingdom","id":"d29f412b4b","standard_list":[{"id":"ISO3166-1-a2","value":"GB"},{"id":"ISO3166-1-a3","value":"GBR"}]}}],"semld_list":["http://en.wikipedia.org/wiki/London","http://ar.wikipedia.org/wiki/لندن","http://ca.wikipedia.org/wiki/Londres","http://cs.wikipedia.org/wiki/Londýn","http://da.wikipedia.org/wiki/London","http://de.wikipedia.org/wiki/London","http://es.wikipedia.org/wiki/Londres","http://fi.wikipedia.org/wiki/Lontoo","http://fr.wikipedia.org/wiki/Londres","http://he.wikipedia.org/wiki/לונדון","http://hi.wikipedia.org/wiki/लंदन","http://id.wikipedia.org/wiki/London","http://it.wikipedia.org/wiki/Londra","http://ja.wikipedia.org/wiki/ロンドン","http://ko.wikipedia.org/wiki/런던","http://nl.wikipedia.org/wiki/Londen","http://no.wikipedia.org/wiki/London","http://pl.wikipedia.org/wiki/Londyn","http://pt.wikipedia.org/wiki/Londres","http://ro.wikipedia.org/wiki/Londra","http://ru.wikipedia.org/wiki/Лондон","http://sv.wikipedia.org/wiki/London","http://th.wikipedia.org/wiki/ลอนดอน","http://tr.wikipedia.org/wiki/Londra","http://zh.wikipedia.org/wiki/伦敦","http://d-nb.info/gnd/4074335-4","http://linkedgeodata.org/triplify/node107775","http://linked-web-apis.fit.cvut.cz/resource/london_city","http://linked-web-apis.fit.cvut.cz/resource/london_uk_city","http://data.nytimes.com/14085781296239331901","http://sw.cyc.com/concept/Mx4rvVjWPJwpEbGdrcN5Y29ycA","http://umbel.org/umbel/rc/Location_Underspecified","http://umbel.org/umbel/rc/PopulatedPlace","http://umbel.org/umbel/rc/Village","http://sws.geonames.org/2643743/","@BBCLondres2012","@LDN","@OlimpicoCaracol","@TelevisaLondres","@TimeOutLondon","@visitlondon","sumo:City"],"variant_list":[{"form":"London","inip":"0","endp":"5"}],"relevance":"100"},{"form":"London","id":"76075d4877","sementity":{"class":"instance","fiction":"nonfiction","id":"ODENTITY_LAST_NAME","type":"Top>Person>LastName"},"semld_list":["sumo:LastName"],"variant_list":[{"form":"London","inip":"0","endp":"5"}],"relevance":"100"}],"concept_list":[{"form":"city","id":"817857ee40","sementity":{"class":"class","fiction":"nonfiction","id":"ODENTITY_CITY","type":"Top>Location>GeoPoliticalEntity>City"},"semld_list":["http://en.wikipedia.org/wiki/City","http://ar.wikipedia.org/wiki/مدينة","http://ca.wikipedia.org/wiki/Ciutat","http://cs.wikipedia.org/wiki/Město","http://de.wikipedia.org/wiki/Stadt","http://es.wikipedia.org/wiki/Ciudad","http://fi.wikipedia.org/wiki/Kaupunki","http://fr.wikipedia.org/wiki/Ville","http://he.wikipedia.org/wiki/עיר","http://hi.wikipedia.org/wiki/शहर","http://id.wikipedia.org/wiki/Kota","http://it.wikipedia.org/wiki/Città","http://ja.wikipedia.org/wiki/都市","http://ko.wikipedia.org/wiki/도시","http://nl.wikipedia.org/wiki/Stad","http://no.wikipedia.org/wiki/By","http://pl.wikipedia.org/wiki/Miasto","http://pt.wikipedia.org/wiki/Cidade","http://ro.wikipedia.org/wiki/Oraș","http://ru.wikipedia.org/wiki/Город","http://sv.wikipedia.org/wiki/Stad","http://th.wikipedia.org/wiki/นคร","http://tr.wikipedia.org/wiki/Şehir","http://zh.wikipedia.org/wiki/城市","http://d-nb.info/gnd/4056723-0","sumo:City"],"variant_list":[{"form":"city","inip":"17","endp":"20"}],"relevance":"100"},{"form":"$","id":"__9145003407816029121","sementity":{"class":"class","type":"Top>Unit>Currency"},"variant_list":[{"form":"$","inip":"30","endp":"30"}],"relevance":"100"},{"form":"tortoise","id":"1019079343","sementity":{"class":"class","fiction":"nonfiction","id":"ODENTITY_REPTILE","type":"Top>LivingThing>Animal>Vertebrate>Reptile"},"semld_list":["http://en.wikipedia.org/wiki/Tortoise","http://ar.wikipedia.org/wiki/سلاحف_برية","http://ca.wikipedia.org/wiki/Testudínid","http://cs.wikipedia.org/wiki/Testudovití","http://de.wikipedia.org/wiki/Landschildkröten","http://es.wikipedia.org/wiki/Testudinidae","http://fi.wikipedia.org/wiki/Testudinidae","http://fr.wikipedia.org/wiki/Tortues_terrestres","http://he.wikipedia.org/wiki/צבים_יבשתיים","http://hi.wikipedia.org/wiki/स्थलीय_कछुआ","http://id.wikipedia.org/wiki/Kura-kura","http://it.wikipedia.org/wiki/Testudinidae","http://ja.wikipedia.org/wiki/リクガメ科","http://ko.wikipedia.org/wiki/땅거북과","http://nl.wikipedia.org/wiki/Landschildpadden","http://no.wikipedia.org/wiki/Landskilpadder","http://pl.wikipedia.org/wiki/Żółwie_lądowe","http://pt.wikipedia.org/wiki/Testudinidae","http://ro.wikipedia.org/wiki/Testudinidae","http://ru.wikipedia.org/wiki/Сухопутные_черепахи","http://sv.wikipedia.org/wiki/Landsköldpaddor","http://tr.wikipedia.org/wiki/Kara_kaplumbağası","http://zh.wikipedia.org/wiki/陸龜","sumo:Reptile"],"semtheme_list":[{"id":"ODTHEME_ZOOLOGY","type":"Top>NaturalSciences>Zoology"}],"variant_list":[{"form":"turtles","inip":"41","endp":"47"}],"relevance":"100"}],"time_expression_list":[{"form":"the 5th of November","normalized_form":"|||||11|5||||","actual_time":"2017-11-05","precision":"day","inip":"53","endp":"71"},{"form":"5th of November","normalized_form":"|||||11|5||||","actual_time":"2017-11-05","precision":"day","inip":"57","endp":"71"}],"money_expression_list":[{"form":"$5","amount_form":"5","numeric_value":"5","currency":"USD","inip":"30","endp":"31"}],"quantity_expression_list":[{"form":"two turtles","amount_form":"two","numeric_value":"2","unit":"turtle","inip":"37","endp":"47"}],"other_expression_list":[{"form":"1245FG","type":"unknown","inip":"104","endp":"109"}],"quotation_list":[{"form":"he was tired in flight 1245FG.","verb":{"form":"said","lemma":"say"},"inip":"81","endp":"110"}],"relation_list":[{"form":"On the 5th of November he said he was tired in flight 1245FG.","inip":"73","endp":"109","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"said","lemma_list":["say"],"sense_id_list":["ODENTITY_COMMUNICATION_PROCESS","ODENTITY_LINGUISTIC_COMMUNICATION","ODENTITY_PROCESS"]},"complement_list":[{"form":"he was tired in flight 1245FG","type":"isDirectObject"}],"degree":"1"},{"form":"London is a nice city.","inip":"0","endp":"20","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a nice city","type":"isAttribute"}],"degree":"1"},{"form":"I have $5 and two turtles.","inip":"23","endp":"47","subject":{"form":"I","lemma_list":["I"],"sense_id_list":["PRONHUMAN"]},"verb":{"form":"have","lemma_list":["have"]},"complement_list":[{"form":"$5 and two turtles","type":"isDirectObject"}],"degree":"1"},{"form":"On the 5th of November he said he was tired in flight 1245FG.","inip":"81","endp":"109","subject":{"form":"he","lemma_list":["he"],"sense_id_list":["PRONHUMAN"]},"verb":{"form":"was tired","lemma_list":["tire"]},"complement_list":[{"form":"in flight","type":"isComplement"}],"degree":"1"}]}'
    response = meaningcloud.TopicsResponse(outputOK)

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.TopicsResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.TopicsResponse('')

    def testGetEntities(self):
        self.assertIsNotNone(self.response.getEntities())
        self.assertTrue(isinstance(self.response.getEntities(), list))

    def testGetNonexistentEntities(self):
        responseWithNoEntities = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"money_expression_list":[],"quantity_expression_list":[],"other_expression_list":[],"quotation_list":[],"relation_list":[{"form":"London is a very nice city.","inip":"0","endp":"25","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a very nice city","type":"isAttribute"}],"degree":"1"}]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoEntities)
        self.assertTrue(isinstance(local_response.getEntities(), dict))
        self.assertEqual(local_response.getEntities(), {})

    def testGetConcepts(self):
        self.assertIsNotNone(self.response.getConcepts())
        self.assertTrue(isinstance(self.response.getConcepts(), list))

    def testGetNonexistentConcepts(self):
        responseWithNoConcepts = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"money_expression_list":[],"quantity_expression_list":[],"other_expression_list":[],"quotation_list":[],"relation_list":[{"form":"London is a very nice city.","inip":"0","endp":"25","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a very nice city","type":"isAttribute"}],"degree":"1"}]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoConcepts)
        self.assertTrue(isinstance(local_response.getConcepts(), dict))
        self.assertIsNotNone(local_response.getConcepts())

    def testGetMoneyExpressions(self):
        self.assertIsNotNone(self.response.getMoneyExpressions())
        self.assertTrue(isinstance(self.response.getMoneyExpressions(), list))

    def testGetNonexistentMoneyExpressions(self):
        responseWithNoMoneyExpressions = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"quantity_expression_list":[],"other_expression_list":[],"quotation_list":[],"relation_list":[{"form":"London is a very nice city.","inip":"0","endp":"25","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a very nice city","type":"isAttribute"}],"degree":"1"}]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoMoneyExpressions)
        self.assertTrue(isinstance(local_response.getMoneyExpressions(), dict))
        self.assertIsNotNone(local_response.getMoneyExpressions())

    def testGetQuantityExpressions(self):
        self.assertIsNotNone(self.response.getQuantityExpressions())
        self.assertTrue(isinstance(self.response.getQuantityExpressions(), list))

    def testGetNonexistentQuantityExpressions(self):
        responseWithNoQuantityExpressions = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"money_expression_list":[],"other_expression_list":[],"quotation_list":[],"relation_list":[{"form":"London is a very nice city.","inip":"0","endp":"25","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a very nice city","type":"isAttribute"}],"degree":"1"}]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoQuantityExpressions)
        self.assertTrue(isinstance(local_response.getQuantityExpressions(), dict))

    def testGetTimeExpressions(self):
        self.assertIsNotNone(self.response.getTimeExpressions())
        self.assertTrue(isinstance(self.response.getTimeExpressions(), list))

    def testGetNonexistentTimeExpressions(self):
        responseWithNoTimeExpressions = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"money_expression_list":[],"quantity_expression_list":[],"other_expression_list":[],"quotation_list":[],"relation_list":[{"form":"London is a very nice city.","inip":"0","endp":"25","subject":{"form":"London","lemma_list":["London"],"sense_id_list":["01d0d69c7d","76075d4877"]},"verb":{"form":"is","lemma_list":["be"]},"complement_list":[{"form":"a very nice city","type":"isAttribute"}],"degree":"1"}]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoTimeExpressions)
        self.assertTrue(isinstance(local_response.getTimeExpressions(), dict))
        self.assertIsNotNone(self.response.getTimeExpressions())

    def testGetQuotations(self):
        self.assertIsNotNone(self.response.getQuotations())
        self.assertTrue(isinstance(self.response.getQuotations(), list))

    def testGetNonexistentQuotations(self):
        responseWithNoQuotations = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"money_expression_list":[],"quantity_expression_list":[],"other_expression_list":[]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoQuotations)
        self.assertTrue(isinstance(local_response.getQuotations(), dict))
        self.assertIsNotNone(local_response.getQuotations())

    def testGetRelations(self):
        self.assertIsNotNone(self.response.getRelations())
        self.assertTrue(isinstance(self.response.getRelations(), list))

    def testGetNonexistentRelations(self):
        responseWithNoRelations = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"time_expression_list":[],"money_expression_list":[],"quantity_expression_list":[],"other_expression_list":[],"quotation_list":[]}'
        local_response = meaningcloud.TopicsResponse(responseWithNoRelations)
        self.assertTrue(isinstance(local_response.getRelations(), dict))
        self.assertIsNotNone(local_response.getRelations())

    def testGetForm(self):
        self.assertIsNotNone(self.response.getTopicForm(self.response.getEntities()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getConcepts()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getTimeExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getMoneyExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getQuantityExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getQuotations()[0]))
        self.assertIsNotNone(self.response.getTopicForm(self.response.getRelations()[0]))

    def testGetRelevance(self):
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getEntities()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getConcepts()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getTimeExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getMoneyExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getQuantityExpressions()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getQuotations()[0]))
        self.assertIsNotNone(self.response.getTopicRelevance(self.response.getRelations()[0]))

    def testGetOntoType(self):
        # correct_values
        firstEntityOntoType = self.response.getOntoType(self.response.getEntities()[0])
        self.assertIsNotNone(firstEntityOntoType)
        self.assertEqual(firstEntityOntoType, 'Top>Location>GeoPoliticalEntity>City')

        firstConceptOntoType = self.response.getOntoType(self.response.getConcepts()[0])
        self.assertIsNotNone(firstConceptOntoType)
        self.assertEqual(firstConceptOntoType, 'Top>Location>GeoPoliticalEntity>City')

        # wrong_values
        with self.assertRaises(AttributeError):
            wrongFormatOntoType = self.response.getOntoType('dummy_value')

        wrongFormatArrayOntoType = self.response.getOntoType({'dummy_key': 'dummy_value'})
        self.assertEqual(wrongFormatArrayOntoType, "")

    def testGetTypeLastNode(self):
        # correct_values
        firstEntityLastNode = self.response.getTypeLastNode(self.response.getOntoType(self.response.getEntities()[0]))
        self.assertIsNotNone(firstEntityLastNode)
        self.assertEqual(firstEntityLastNode, 'City')

        firstConceptLastNode = self.response.getTypeLastNode(self.response.getOntoType(self.response.getConcepts()[0]))
        self.assertIsNotNone(firstConceptLastNode)
        self.assertEqual(firstConceptLastNode, 'City')

        # wrong_values
        wrongFormat = self.response.getTypeLastNode('dummy_value')
        self.assertEqual(wrongFormat, 'dummy_value')

        wrongFormatArray = self.response.getTypeLastNode({'dummy_key': 'dummy_value'})
        self.assertEqual(wrongFormatArray, "")

    def testGetTypeFirstNode(self):
        # correct_values
        firstEntityFirstNode = self.response.getTypeFirstNode(self.response.getOntoType(self.response.getEntities()[0]))
        self.assertIsNotNone(firstEntityFirstNode)
        self.assertEqual(firstEntityFirstNode, 'Location')

        firstConceptFirstNode = self.response.getTypeFirstNode(self.response.getOntoType(self.response.getConcepts()[0]))
        self.assertIsNotNone(firstConceptFirstNode)
        self.assertEqual(firstConceptFirstNode, 'Location')

        responseNoFirstNode = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"5000"},"entity_list":[{"form":"DummyTopValue","id":"__madeUpID","sementity":{"class":"instance","id":"__madeupValue","type":"Top"},"variant_list":[{"form":"DummyTopValue","inip":"0","endp":"12"}],"relevance":"100"}]}'
        localResponse = meaningcloud.TopicsResponse(responseNoFirstNode)
        localFirstEntityFirstNode = localResponse.getTypeFirstNode(localResponse.getOntoType(localResponse.getEntities()[0]))
        self.assertIsNotNone(localFirstEntityFirstNode)
        self.assertEqual(localFirstEntityFirstNode, 'Top')

        # wrong_values
        wrongFormat = self.response.getTypeLastNode('dummy_value')
        self.assertEqual(wrongFormat, 'dummy_value')

        wrongFormatArray = self.response.getTypeLastNode({'dummy_key': 'dummy_value'})
        self.assertEqual(wrongFormatArray, "")


    def testIsUserDefined(self):
        self.assertEqual(self.response.isUserDefined(self.response.getEntities()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getConcepts()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getTimeExpressions()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getMoneyExpressions()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getQuantityExpressions()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getOtherExpressions()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getQuotations()[0]), False)
        self.assertEqual(self.response.isUserDefined(self.response.getRelations()[0]), False)

        responseWithUserDefinedEntities = '{"status":{"code":"0","msg":"OK","credits":"1"},"entity_list":[{"form":"Lincoln Trikru","official_form":"Lincoln","dictionary":"test1","id":"ent_sin_tag","sementity":{"class":"instance","type":"Top&gt;People&gt;Grounders"},"variant_list":[{"form":"Lincoln","inip":"0","endp":"6"}],"relevance":"100"}],"concept_list":[{"form":"dropship","id":"concepto_sin_tag","dictionary":"test1","sementity":{"class":"class"},"variant_list":[{"form":"dropship","inip":"19","endp":"26"}],"relevance":"100"}]}'
        responseWithUD = meaningcloud.TopicsResponse(responseWithUserDefinedEntities)
        self.assertEqual(responseWithUD.isUserDefined(responseWithUD.getEntities()[0]), True)
        self.assertEqual(responseWithUD.isUserDefined(responseWithUD.getConcepts()[0]), True)

    def testGetNumberOfAppearances(self):
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getEntities()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getConcepts()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getTimeExpressions()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getMoneyExpressions()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getQuantityExpressions()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getOtherExpressions()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getQuotations()[0]), 1)
        self.assertEqual(self.response.getNumberOfAppearances(self.response.getRelations()[0]), 1)

        # wrong value
        self.assertEqual(self.response.getNumberOfAppearances(None), 0)


if __name__ == '__main__':
    unittest.main()
