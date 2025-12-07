from pyspark.sql import SparkSession
from pyspark.sql.functions import when


def main():
    spark = SparkSession.builder.appName("CustomerOrdersJob").getOrCreate()

    customers_path = "/opt/spark-apps/input/customers.csv"
    orders_path = "/opt/spark-apps/input/orders.json"
    output_path_csv = "/opt/spark-apps/output/orders_enriched_csv"
    output_path_parquet = "/opt/spark-apps/output/orders_enriched_parquet"

    # ✅ Prod Mode (HDFS)
    # customers_path = "hdfs://hdfs-namenode:9000/input/customers.csv"
    # orders_path = "hdfs://hdfs-namenode:9000/input/orders.json"
    # output_path_csv = "hdfs://hdfs-namenode:9000/output/orders_enriched_csv"
    # output_path_parquet = "hdfs://hdfs-namenode:9000/output/orders_enriched_parquet"

    # 1 - Read customer and order data
    df_customers = spark.read.option("header", True).csv(customers_path)
    df_orders = spark.read.json(orders_path)

    #2 - Join datasets and enrich with order type
    df_joined = df_orders.join(df_customers, on="customer_id", how="inner")

    #3 - Enrich with order type based on amount
    df_enriched = df_joined.withColumn(
        "order_type",
        when(df_joined.amount >= 200, "High Value")
        .when(df_joined.amount >= 100, "Medium Value")
        .otherwise("Low Value")
    )

    #4 - Write enriched data to CSV and Parquet
    df_enriched_op = df_enriched.select("order_id", "name", "amount", "order_type")
    df_enriched_op.write.mode("overwrite").csv(output_path_csv)
    df_enriched_op.write.mode("overwrite").parquet(output_path_parquet)

    spark.stop()


if __name__ == "__main__":
    main()
