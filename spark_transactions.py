from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName('SparkTransactionsProject').getOrCreate()
    df = spark.read.csv("PS_20174392719_1491204439457_log.csv")
    print(df.count())


if __name__ == "__main__":
    main()
