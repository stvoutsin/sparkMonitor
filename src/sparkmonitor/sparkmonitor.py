'''
Created on Jun 1, 2020

@author: stelios
'''

import requests

class SparkEndpoints(object):
    
    
    JOBS_SUBDIR = "jobs"
    STORAGE_SUBDIR = "storage/rdd/"
    STAGES_SUBDIR = "stages"
    EXECUTORS_SUBDIR = "executors"

    
    def __init__(self):
        pass
    
    
    

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
            return wrapper                # ...


    def __init__(self, host=None, port=None, appid=None, sparkcontext=None):
        '''
        Constructor
        
        :param host:
        :param port:
        :param appid:
        '''
        self.host = host
        self.port = port
        self.appid = self.sc_to_appid(appid) if sparkcontext else appid
        self.baseurl = self.generate_baseurl(self.host, self.port, self.appid)
        print(self.baseurl)

        
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
    
        
    def sc_to_appid(self, spark_context):
        return spark_context._jsc.sc().applicationId()
    
    
    def get_json(self, url):
        jsondata = requests.get(url).json()
        return jsondata
    
    
    def get_storage_info(self):
        url = self.baseurl + SparkEndpoints.STORAGE_SUBDIR
        [r.json() for r  in [
           requests.get("{0}{1}".format(url, rdd.get("id"))) for
           rdd  in requests.get(url).json()
        ] if r.status_code == 200]    


    def get_job_info(self):
        url = self.baseurl + SparkEndpoints.JOBS_SUBDIR
        return self.get_json(url)


    def get_stage_info(self):
        url = self.baseurl + SparkEndpoints.STAGES_SUBDIR
        return self.get_json(url)


    def get_executor_info(self):
        url = self.baseurl + SparkEndpoints.EXECUTORS_SUBDIR
        return self.get_json(url)

    
def main():
    sm = SparkMonitor("localhost", "8088", "application_1588261403747_0012")
    print(sm.get_job_info())
    #sm = SparkMonitor("localhost", "8088", sparkcontext=sc)

if __name__ == "__main__":
    main()
    