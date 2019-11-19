import meaningcloud.Response


class ClusteringResponse(meaningcloud.Response):

    def __init__(self, response):
        """
        ClusteringResponse constructor

        :param response:
            String returned by the request
        """

        if not response:
            raise Exception("The request sent did not return a response")
        meaningcloud.Response.__init__(self, response)

    def getClusters(self):
        """
        Get clusters found for the texts sent

        :return:
            Array with the categories detected
        """

        return (self._response['cluster_list']
                if (('cluster_list' in self._response.keys()) and (self._response['cluster_list'] is not None))
                else {})

    # Generic auxiliary functions

    def getClusterTitle(self, cluster):
        """
        Get the title of a cluster

        :param cluster:
            Cluster you want the title from
        :return:
            Cluster title
        """

        return (cluster['title']
                if ((len(cluster) > 0) and ('title' in cluster.keys()) and (cluster['title'] is not None))
                else "")

    def getClusterSize(self, cluster):
        """
        Get the size of a cluster

        :param cluster:
            Cluster you want the size from
        :return:
            Cluster size
        """

        return (cluster['size']
                if ((len(cluster) > 0) and ('size' in cluster.keys()) and (cluster['size'] is not None))
                else "")

    def getClusterScore(self, cluster):
        """
        Get the score of a cluster

        :param cluster:
            Cluster you want the score from
        :return:
            Cluster score
        """

        return (cluster['score']
                if ((len(cluster) > 0) and ('score' in cluster.keys()) and (cluster['score'] is not None))
                else "")

    def getClusterDocuments(self, cluster):
        """
        Get the list of documents in a cluster

        :param cluster:
            Cluster you want the relevance from
        :return:
            Cluster relevance
        """

        return (self._response['document_list']
                if (('document_list' in self._response.keys()) and (self._response['document_list'] is not None))
                else {})