import unittest
import meaningcloud
import json

class MyTestCase(unittest.TestCase):
    outputOK = '{"status": {"code": "0","msg": "OK","credits": "1","remaining_credits":"5000"},"category_list": [{"code": "01021001","label": "arts, culture and entertainment - entertainment (general) - entertainment award","abs_relevance": "0.48236102","relevance": "100"},{"code": "08006000","label": "human interest - award and prize","abs_relevance": "0.28744578","relevance": "60"}]}'
    response = meaningcloud.ClassResponse(outputOK)

    outputEmpty = '{"status": {"code": "0","msg": "OK","credits": "1","remaining_credits":"5000"}}'
    empty_response = meaningcloud.ClassResponse(outputEmpty)

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
         meaningcloud.ClassResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.ClassResponse('')


    def testConstructEmptyResult(self):
        self.assertIsNotNone(self.empty_response.getResponse())


    def testGetCategories(self):
        self.assertIsNotNone(self.response.getCategories())
        self.assertTrue(isinstance(self.response.getCategories(),list))


    def testGetNonexistentCategories(self):
        self.assertEqual(len(self.empty_response.getCategories()),0)


    def testGetCategoryCode(self):
        categories = self.response.getCategories()
        category = categories[0] if((len(categories)>0) and (categories[0] is not None)) else []
        self.assertIsNotNone(self.response.getCategoryCode(category))


    def testGetCategoryCodeWithEmptyInput(self):
        self.assertEqual(self.response.getCategoryCode([]),"")


    def testGetCategoryLabel(self):
        categories = self.response.getCategories()
        category = categories[0] if ((len(categories) > 0) and (categories[0] is not None)) else []
        self.assertIsNotNone(self.response.getCategoryLabel(category))

    def testGetCategoryLabelWithEmptyInput(self):
        self.assertEqual(self.response.getCategoryLabel([]),"")


    def testGetCategoryAbsRelevance(self):
        categories = self.response.getCategories()
        category = categories[0] if ((len(categories) > 0) and (categories[0] is not None)) else []
        self.assertIsNotNone(self.response.getCategoryAbsRelevance(category))

    def testGetCategoryAbsRelevanceWithEmptyInput(self):
        self.assertEqual(self.response.getCategoryAbsRelevance([]), "")


    def testGetCategoryRelevance(self):
        categories = self.response.getCategories()
        category = categories[0] if ((len(categories) > 0) and (categories[0] is not None)) else []
        self.assertIsNotNone(self.response.getCategoryRelevance(category))

    def testGetCategoryRelevanceWithEmptyInput(self):
        self.assertEqual(self.response.getCategoryRelevance([]), "")




if __name__ == '__main__':
    unittest.main()
