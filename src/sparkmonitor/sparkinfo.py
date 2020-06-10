'''
Created on Jun 10, 2020

@author: stelios
'''

import pandas as pd
import json

class SparkInfo(object):
    """
    Holds information objects from Spark REST API responses
    
    """
    
    def __init__(self, data):
        """
        :param data:
        :type data:
        """
        self.data = data
        try:
            self.df = pd.read_json (json.dumps(data))
        except Exception as e:
            print (e)
            self.df = None


    def to_pandas(self):
        """
        Get info as a Pandas Dataframe
        """
        return self.df
        
        
    def to_json(self):
        """
        Get info in JSON format
        """
        return self.data
    
    
    def __str__(self, *args, **kwargs):
        if self.df is not None:
            return self.df.to_string()
        elif self.data:
            return json.dumps(self.data)
        return object.__str__(self, *args, **kwargs)