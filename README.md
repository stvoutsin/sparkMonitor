# sparkMonitor
Spark Monitor for getting information and metadata from the Spark UI REST API

## Example Usage:
The following assumes that the Spark Monitor is run using Zeppelin, which has access to a Spark cluster
If run without Zeppelin, ignore the steps that print the output (z.show(df))

### Import SparkMonitor

```
from sparkmonitor import SparkMonitor
```

### Initialize SparkMonitor 

```
sm = SparkMonitor("stv-dev-master", "8088", sparkcontext=sc)
```

### Get and display Job Info

```
job_info = sm.get_job_info()
job_info_df = job_info.to_pandas()
job_info_json = job_info.to_json()
if len(job_info_df)>0:
    df = spark.createDataFrame(job_info_df.astype(str)) 
    z.show(df)
```

### Use JSON version to access the first job status

```
print("Status of first job: {}".format(job_info_json[0]["status"]))
```

### Get and display Executor Info

```
executor_info = sm.get_executor_info()
exec_info_df = executor_info.to_pandas()
if len(exec_info_df)>0:
    df = spark.createDataFrame(exec_info_df.astype(str)) 
    z.show(df)
```

### Get and display Storage Info

```
storage_info = sm.get_storage_info()
storage_info_df = storage_info.to_pandas()
if len(storage_info)>0:
    df = spark.createDataFrame(storage_info_df.astype(str)) 
    z.show(df)
```
    
### Get and display Stage info

```
stage_info = sm.get_stage_info()
stage_info = stage_info.to_pandas()
if len(stage_info)>0:
    df = spark.createDataFrame(stage_info.astype(str)) 
    z.show(df)    
```
    
