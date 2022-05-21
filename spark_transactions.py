from pyspark.sql import SparkSession


class SparkApp:
    def __init__(self, name):
        self.spark = SparkSession.builder.appName(name).getOrCreate()

    def process_file(self, file_name):
        df = self.spark.read.csv(file_name)
        print("Number of lines in file:", df.count())


def main():
    spark_name = 'SparkTransactionsProject'
    file_name = 'PS_20174392719_1491204439457_log.csv'
    spark_app = SparkApp(spark_name)
    spark_app.process_file(file_name)


if __name__ == "__main__":
    main()
