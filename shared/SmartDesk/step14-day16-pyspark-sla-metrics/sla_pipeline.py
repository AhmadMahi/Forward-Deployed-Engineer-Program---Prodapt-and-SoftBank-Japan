"""SmartDesk step 14: PySpark SLA metrics pipeline (bronze -> silver -> gold)."""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

SLA_HOURS = {"high": 4, "medium": 24, "low": 72}


def spark_session():
    return (SparkSession.builder.master("local[1]").appName("smartdesk-sla")
            .config("spark.ui.enabled", "false").getOrCreate())


def sample_events(spark):
    rows = [(1, "network", "high", "2026-10-26 09:00:00", "2026-10-26 11:30:00"),
            (2, "billing", "high", "2026-10-26 10:00:00", "2026-10-26 18:00:00"),
            (3, "account", "medium", "2026-10-26 11:00:00", "2026-10-27 09:00:00"),
            (4, "network", "medium", "2026-10-26 18:00:00", "2026-10-28 08:00:00"),
            (5, "billing", "low", "2026-10-25 08:00:00", "2026-10-26 08:00:00"),
            (6, "account", "high", "2026-10-27 07:00:00", None),
            (6, "account", "high", "2026-10-27 07:00:00", None)]
    return spark.createDataFrame(rows, "ticket_id int, category string, priority string, opened string, resolved string")


def silver(bronze):
    sla = F.create_map(*[x for k, v in SLA_HOURS.items() for x in (F.lit(k), F.lit(v))])
    return (bronze.dropDuplicates()
            .withColumn("opened", F.to_timestamp("opened"))
            .withColumn("resolved", F.to_timestamp("resolved"))
            .withColumn("hours", (F.unix_timestamp("resolved") - F.unix_timestamp("opened")) / 3600)
            .withColumn("sla_hours", sla[F.col("priority")])
            .withColumn("breached", F.col("resolved").isNotNull() & (F.col("hours") > F.col("sla_hours"))))


def gold(silver_df):
    return (silver_df.filter(F.col("resolved").isNotNull())
            .groupBy("category")
            .agg(F.count("*").alias("resolved"), F.round(F.avg("hours"), 1).alias("avg_hours"),
                 F.sum(F.col("breached").cast("int")).alias("breaches"))
            .withColumn("breach_rate", F.round(F.col("breaches") / F.col("resolved"), 2))
            .orderBy("category"))


if __name__ == "__main__":
    spark = spark_session()
    s = silver(sample_events(spark))
    s.createOrReplaceTempView("tickets")
    gold(s).show()
    spark.sql("SELECT priority, COUNT(*) AS open FROM tickets WHERE resolved IS NULL GROUP BY priority").show()
