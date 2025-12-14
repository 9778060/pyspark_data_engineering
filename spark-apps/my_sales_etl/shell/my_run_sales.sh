
#!/bin/bash

# Check for argument
# if [ -z "$1" ]; then
#   echo " Usage: ./my_run_sales.sh"
#   exit 1
# fi

RUN_DATE=$(date +%F)

echo "Triggering my_sales_etl.py for $RUN_DATE..."

# Run spark-submit inside spark-master container
docker exec spark-master spark-submit /opt/spark-apps/my_sales_etl/scripts/my_sales_etl_job.py "$RUN_DATE"

echo "Job completed for $RUN_DATE"
