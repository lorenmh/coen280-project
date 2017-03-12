#!/DCNFS/applications/cdh/5.6/app/spark-1.5.0-cdh5.6.0/bin/spark-submit

from pyspark import SparkContext, SparkConf
from pyspark.mllib.fpm import FPGrowth

conf = SparkConf()
conf.setAppName("Simple App")
sc = SparkContext(conf=conf)
# Suppress log warnings to errors only, 
# doesn't apply right away but does the trick
sc.setLogLevel("ERROR")

#data = sc.textFile("data/mllib/sample_fpgrowth.txt")
data = [["a", "b", "c"], ["a", "b", "d", "e"], ["a", "c", "e"], ["a", "c", "f"]]

#transactions = data.map(lambda line: line.strip().split(' '))
transactions = sc.parallelize(data)

transactions.getNumPartitions()

model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)

result = model.freqItemsets().collect()
for fi in result:
    print(fi)

sc.stop()
