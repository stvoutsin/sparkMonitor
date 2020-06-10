'''
Created on Jun 10, 2020

@author: stelios
'''
import requests
import pandas as pd


class Helpers(object):
    """
    Helper methods
    """

    def __init__(self):
        pass


    @staticmethod
    def get_json(url):
        """
        Get the JSON data from a URL
        :param url:
        :type url:
        """
        jsondata = requests.get(url).json()
        return jsondata


    @staticmethod
    def sc2appid(spark_context):
        """
        Create a Spark context from a given Application ID
        :param spark_context:
        :type spark_context:
        """
        return spark_context._jsc.sc().applicationId()


    @staticmethod
    def json2panda(jsonstring=""):
        """
        Convert a json string to a pandas Dataframe
        :param jsonstring:
        :type jsonstring:
        """
        df = pd.read_json (jsonstring)
        return df
    
    
    