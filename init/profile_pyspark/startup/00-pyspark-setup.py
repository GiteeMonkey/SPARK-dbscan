# Configure the necessary Spark environment
import os
import sys


# Note: Some Spark installations do not need the extra libexec path
spark_home = os.environ.get('SPARK_HOME', None)
sys.path.inse