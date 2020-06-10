# sparkMonitor

This package is a wrapper around the Spark REST API and allows users to access information and Spark applications

# Example Usage

sm = SparkMonitor("localhost", "8088", "application_1588261403747_0012")
print(sm.get_job_info())
print(sm.get_executor_info())
print(sm.get_storage_info())
print(sm.get_stage_info())
