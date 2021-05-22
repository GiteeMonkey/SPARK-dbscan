# Configure the necessary Spark environment
import os
import sys


# Note: Some Spark installations do not need the extra libexec path
spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "/libexec/python")

# Add the py4j to the path.
# You may need to change the version number to match your insta