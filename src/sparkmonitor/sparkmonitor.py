'''
Created on Jun 1, 2020

@author: stelios
'''

import requests
from params import SparkParams
from helpers import Helpers
from sparkinfo import SparkInfo


class SparkMonitor(object):
    '''
    SparkMonitor class
    Used to fetch and display metadata for Spark applications
    '''
    
    class Decorators(object):
        
        @classmethod
        def sanitize(self,method):
            '''
            :param method:
            :type method:
            '''
            def wrapper(self, host, port, appid):
                if host and port and appid:
                    return method(self, host, port, appid)
                else:
                    return None
            return wrapper


    def __init__(self, host=None, port=None, appid=None, sparkcontext=None):
        '''
        Constructor
        
        :param host:
        :type host: str
        :param port:
        :type port: str
        :param appid:
        :type appid: str
        :param sparkcontext:
        :type sparkcontext: str

        '''
        self.host = host
        self.port = port
        self.appid = Helpers.sc2appid(sparkcontext) if sparkcontext is not None else appid
        self.baseurl = self.generate_baseurl(self.host, self.port, self.appid)

        
    @property
    def host(self):
        return self.__host
    
    @host.setter
    def host(self, host):
        self.__host = host
        
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, port):
        self.__port = port
        
    @property
    def appid(self):
        return self.__appid
    
    @appid.setter
    def appid(self, appid):
        self.__appid = appid     
    
    @Decorators.sanitize
    def generate_baseurl(self, host, port, appid):
        return "http://{0}:{1}/proxy/{2}/api/v1/applications/{2}/".format(host, port, appid)
  
        
    def get_storage_info(self):
        """
        Get the Spark Storage info
        """
        url = self.baseurl + SparkParams.STORAGE_SUBDIR
        return SparkInfo(Helpers.get_json(url)) 
                                     
    def get_job_info(self):
        """
        Get the Spark Job info
        """
        url = self.baseurl + SparkParams.JOBS_SUBDIR
        return SparkInfo(Helpers.get_json(url))


    def get_stage_info(self):
        """
        Get the Spark Stage info
        """
        url = self.baseurl + SparkParams.STAGES_SUBDIR
        return SparkInfo(Helpers.get_json(url))


    def get_executor_info(self):
        """
        Get the Spark Executor info
        """
        url = self.baseurl + SparkParams.EXECUTORS_SUBDIR
        return SparkInfo(Helpers.get_json(url))

    
    def get_job_logs(self):
        """
        Get the Spark Storage logs
        """
        url = self.baseurl + SparkParams.LOGS_SUBDIR
        return requests.get(url).text
    
    
    
    
def main():
    sm = SparkMonitor("localhost", "8088", "application_1588261403747_0013")
    #sm = SparkMonitor("localhost", "8088", sparkcontext=sc)
    print(sm.get_job_info())
    print(sm.get_executor_info())
    print(sm.get_storage_info())
    print(sm.get_stage_info())
    
    #print(sm.get_job_logs())

if __name__ == "__main__":
    main()
    
