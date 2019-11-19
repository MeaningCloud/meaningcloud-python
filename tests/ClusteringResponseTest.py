import unittest
import meaningcloud
import json


class MyTestCase(unittest.TestCase):
    outputOK = '{"status":{"code":"0","msg":"OK","credits":"1","remaining_credits":"31634"},"cluster_list":[{"title":"Girl","size":"2","score":"0.16","document_list":{"2":"the girl","3":"the girl and the giraffes."}},{"title":"Giraffe","size":"2","score":"0.13","document_list":{"1":"the giraffe","3":"the girl and the giraffes."}}]}'
    response = meaningcloud.ClusteringResponse(outputOK)

    outputEmpty = '{"status": {"code": "0","msg": "OK","credits": "1","remaining_credits":"5000"}}'
    empty_response = meaningcloud.ClusteringResponse(outputEmpty)

    def testConstruct(self):
        self.assertIsNotNone(self.response.getResponse())

    def testConstructWithWrongJson(self):
        outputWrong = 'malformed json'
        with self.assertRaises(json.JSONDecodeError):
            meaningcloud.ClusteringResponse(outputWrong)

    def testConstructWithEmptyParam(self):
        with self.assertRaises(Exception):
            meaningcloud.ClusteringResponse('')

    def testConstructEmptyResult(self):
        self.assertIsNotNone(self.empty_response.getResponse())

    def testGetClusters(self):
        self.assertIsNotNone(self.response.getClusters())
        self.assertTrue(isinstance(self.response.getClusters(), list))

    def testGetNonexistentClusters(self):
        self.assertEqual(len(self.empty_response.getClusters()), 0)

    def testGetClusterTitle(self):
        clusters = self.response.getClusters()
        cluster = clusters[0] if((len(clusters) > 0) and (clusters[0] is not None)) else []
        self.assertIsNotNone(self.response.getClusterTitle(cluster))

    def testGetClusterTitleWithEmptyInput(self):
        self.assertEqual(self.response.getClusterTitle([]), "")

    def testGetClusterSize(self):
        clusters = self.response.getClusters()
        cluster = clusters[0] if ((len(clusters) > 0) and (clusters[0] is not None)) else []
        self.assertIsNotNone(self.response.getClusterSize(cluster))

    def testGetClusterSizeWithEmptyInput(self):
        self.assertEqual(self.response.getClusterSize([]), "")

    def testGetClusterScore(self):
        clusters = self.response.getClusters()
        cluster = clusters[0] if ((len(clusters) > 0) and (clusters[0] is not None)) else []
        self.assertIsNotNone(self.response.getClusterScore(cluster))

    def testGetClusterScoreWithEmptyInput(self):
        self.assertEqual(self.response.getClusterScore([]), "")

    def testGetClusterDocuments(self):
        clusters = self.response.getClusters()
        cluster = clusters[0] if ((len(clusters) > 0) and (clusters[0] is not None)) else []
        self.assertIsNotNone(self.response.getClusterDocuments(cluster))

    def testGetClusterDocumentsWithEmptyInput(self):
        self.assertEqual(self.response.getClusterDocuments([]), {})


if __name__ == '__main__':
    unittest.main()
