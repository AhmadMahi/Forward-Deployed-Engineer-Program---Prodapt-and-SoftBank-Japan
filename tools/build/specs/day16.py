"""Day 16 spec. Basics: Data Pipelines, Spark and PySpark.
Source: archive/v1-40-day/Day14 (pipelines and Spark intro) + Day16 (PySpark batch pipelines and SQL), merged.
NEW (v4) topics are marked.
"""
DAY = 16
FOLDER = "Day16-Data-Pipelines-Spark-and-PySpark"
SLUG = "Data_Pipelines_Spark_and_PySpark"
TITLE = "Data Pipelines, Spark and PySpark"
SUBTITLE = "Pipeline stages, Spark DataFrames and joins, an end-to-end batch pipeline, Spark SQL and AI-assisted " \
           "data engineering"
DATE = "Tue 17 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 17: DevOps and cloud fundamentals, plus Basics assessment 3."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 15"),
        ("Pipelines", "Stages, medallion layers, why Spark"),
        ("Spark DataFrames", "Transformations, actions, joins"),
        ("End-to-end pipeline", "Run date, checks, run log"),
        ("Spark SQL", "SQL refresher on DataFrames"),
        ("AI-assisted DE", "Codex drafts, you verify. NEW (v4)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Design a batch job", "Describe stages, schedules and bronze, silver and gold layers."),
        ("Use PySpark", "Clean, aggregate and join DataFrames; explain laziness."),
        ("Ship a pipeline", "Parameterised, idempotent, validated and logged, with SQL gold tables."),
        ("Verify AI code", "Check a Codex-generated transformation against a known answer."),
    ]),
    dict(type="table", title="How today is organised", header=["Session", "Duration", "Focus"], rows=[
        ["Session 1", "1 hr", "Pipelines and stages; why Spark"],
        ["Session 2", "2 hrs", "SparkSession, DataFrames, transformations vs actions, joins"],
        ["Session 3", "2.5 hrs", "End-to-end batch pipeline; Spark SQL refresher"],
        ["Session 4", "1 hr", "AI-assisted data engineering: generate a transformation with Codex and verify it (NEW v4)"],
    ]),

    dict(type="section", title="Pipelines and stages", sub="Session 1 (1 hr): data jobs that run on a schedule"),
    dict(type="cards", title="Layers of a modern pipeline", items=[
        ("Bronze (raw)", "Data exactly as received."),
        ("Silver (clean)", "Fixed types, no duplicates, valid rows."),
        ("Gold (business)", "Aggregated tables for reports."),
    ], note="Called the medallion architecture. Each layer can be rebuilt from the one before."),
    dict(type="cards", title="What makes a batch job production ready", items=[
        ("Scheduled", "Runs nightly or hourly with a scheduler."),
        ("Idempotent", "A re-run gives the same result, no duplicates."),
        ("Partitioned", "Process one day at a time, not all history."),
        ("Observable", "Logs row counts, rejects and run time."),
    ]),
    dict(type="compare", title="pandas and Spark", left=dict(title="pandas", bullets=[
        "Runs on one machine", "Data must fit in memory", "Executes each line immediately", "Perfect up to a few GB",
    ]), right=dict(title="Spark", bullets=[
        "Runs on a cluster of machines", "Handles terabytes", "Lazy: builds a plan, then runs it",
        "Same code on a laptop or a cluster",
    ])),
    dict(type="flow", title="How Spark runs your code", items=[
        ("Driver", "Your program builds the plan"),
        ("Plan", "Optimiser rewrites it"),
        ("Tasks", "Split by partition"),
        ("Executors", "Workers run tasks in parallel"),
    ], note="A partition is one chunk of the data. More partitions, more parallel work."),

    dict(type="section", title="Spark DataFrames", sub="Session 2 (2 hrs): describe the result you want"),
    dict(type="bullets_code", title="Starting Spark", bullets=[
        "SparkSession is your entry point",
        "local[1] in class; local[*] uses all cores",
        "Read CSV, JSON or Parquet",
        "printSchema shows column types",
    ], code='''from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .master("local[1]")
         .appName("day16")
         .getOrCreate())

df = spark.read.csv("orders.csv",
                    header=True, inferSchema=True)
df.printSchema()
df.show(5)'''),
    dict(type="table", title="Transformations and actions", header=["Kind", "Examples", "What happens"], rows=[
        ["Transformation", "select, filter, withColumn, groupBy, join", "Adds a step to the plan. Nothing runs yet."],
        ["Action", "show, count, collect, write", "Runs the whole plan and returns or saves data."],
    ], note="Lazy evaluation lets Spark optimise the whole job before touching any data."),
    dict(type="bullets_code", title="Clean and enrich", greet="Seiri (整理): Sorting things out", bullets=[
        "F holds Spark's built-in functions",
        "filter keeps matching rows",
        "withColumn adds or replaces a column",
        "when / otherwise is Spark's if / else",
    ], code='''from pyspark.sql import functions as F

clean = (df
  .dropDuplicates(["order_id"])
  .filter(F.col("amount") > 0)
  .withColumn("city", F.trim("city"))
  .withColumn("size", F.when(
      F.col("amount") >= 1000, "large")
      .otherwise("small")))'''),
    dict(type="bullets_code", title="Group and aggregate", bullets=[
        "groupBy then agg with named results",
        "Many aggregates in one pass",
        "orderBy for sorting",
        "Same idea as SQL GROUP BY",
    ], code='''daily = (clean
  .groupBy("order_date", "city")
  .agg(F.count("*").alias("orders"),
       F.sum("amount").alias("revenue"),
       F.round(F.avg("amount"), 2)
         .alias("avg_order"))
  .orderBy(F.desc("revenue")))

daily.show()'''),
    dict(type="table", title="Choosing a join", header=["Join", "Keeps", "Question it answers"], rows=[
        ["inner", "Rows with a match on both sides", "Orders with known customers"],
        ["left", "All left rows, nulls if no match", "All orders, with customer if known"],
        ["left_anti", "Left rows with no match", "Orders from unknown customers"],
        ["left_semi", "Left rows that have a match", "Customers who ordered"],
    ], note="Always check row counts before and after a join. Duplicated keys multiply rows."),
    dict(type="bullets_code", title="Joins and writing the result", bullets=[
        "how= picks the join type",
        "Anti joins find data quality gaps",
        "Parquet: columnar, compressed, typed",
        "mode overwrite makes re-runs idempotent",
    ], code='''enriched = orders.join(customers,
                       on="customer_id", how="left")
unknown = orders.join(customers,
                      on="customer_id", how="left_anti")
print("Unknown customers:", unknown.count())

(daily.write
   .mode("overwrite")
   .partitionBy("order_date")
   .parquet("gold/daily_city_revenue"))'''),

    dict(type="section", title="An end-to-end batch pipeline", sub="Session 3 (2.5 hrs): from prototype to a daily job"),
    dict(type="table", title="SQL refresher: the order clauses run in", greet="Narabi (並び): Order and arrangement",
         header=["Written order", "Runs as step", "Purpose"], rows=[
        ["SELECT", "5", "Pick and compute columns"],
        ["FROM / JOIN", "1", "Choose and combine tables"],
        ["WHERE", "2", "Filter rows"],
        ["GROUP BY", "3", "Make groups"],
        ["HAVING", "4", "Filter groups"],
        ["ORDER BY / LIMIT", "6", "Sort and cut"],
    ]),
    dict(type="bullets_code", title="CTEs and window functions", bullets=[
        "WITH names an intermediate result",
        "Window functions keep every row",
        "PARTITION BY = per group",
        "Great for ranks and running totals",
    ], code='''WITH daily AS (
  SELECT order_date, city,
         SUM(amount) AS revenue
  FROM orders
  GROUP BY order_date, city
)
SELECT order_date, city, revenue,
  RANK() OVER (
    PARTITION BY order_date
    ORDER BY revenue DESC) AS rnk
FROM daily;'''),
    dict(type="bullets_code", title="Spark SQL: query DataFrames with SQL", bullets=[
        "createOrReplaceTempView names a DataFrame",
        "spark.sql returns a new DataFrame",
        "Same optimiser as the DataFrame API",
        "Mix both freely in one pipeline",
    ], code='''orders.createOrReplaceTempView("orders")

top = spark.sql("""
  SELECT city, SUM(amount) AS revenue
  FROM orders
  GROUP BY city
  ORDER BY revenue DESC
""")
top.show()'''),
    dict(type="flow", title="Anatomy of a production batch job", items=[
        ("Config", "Paths, schemas, run date"),
        ("Extract", "Read bronze for the run date"),
        ("Transform", "Silver rules, gold aggregates"),
        ("Validate", "Counts and quality checks"),
        ("Load + log", "Overwrite partition, record run"),
    ]),
    dict(type="table", title="Pipeline quality checks", header=["Check", "Example", "If it fails"], rows=[
        ["Not empty", "silver.count() > 0", "Stop the run"],
        ["Unique keys", "No duplicate order_id", "Stop the run"],
        ["Valid ranges", "amount > 0", "Move to rejects"],
        ["Reconciliation", "Gold total equals silver total", "Alert the team"],
    ], note="Fail loudly and early. Silent bad data is worse than a failed job."),

    dict(type="section", title="AI-assisted data engineering", sub="Session 4 (1 hr): Codex drafts, you verify",
         new=True),
    dict(type="flow", title="Generate a transformation, then verify it", new=True, items=[
        ("Specify", "Inputs, rules, output columns"),
        ("Generate", "Codex writes the PySpark"),
        ("Read", "Every line, every filter"),
        ("Verify", "Known answer, counts, totals"),
        ("Keep or fix", "Only code you can explain"),
    ], note="Verification is the job. The code is cheap; wrong numbers in a report are expensive."),
    dict(type="cards", title="How to verify AI-written data code", new=True, items=[
        ("Golden example", "Tiny input with a hand-calculated expected output."),
        ("Row counts", "Before and after every filter and join."),
        ("Reconcile totals", "Sum of gold equals sum of silver."),
        ("Second method", "Check one result with pandas or SQL as well."),
        ("Edge cases", "Nulls, duplicates, zero, boundary values."),
        ("Read the plan", "df.explain() shows hidden shuffles and filters."),
    ]),
    dict(type="code", title="A Codex prompt for a PySpark transformation", new=True, code='''Write a PySpark function sla_metrics(tickets) for SmartDesk.
Input columns: ticket_id, priority (low|medium|high), opened_at, resolved_at (timestamp, may be null).
Rules: SLA minutes are high=60, medium=240, low=1440. Unresolved tickets are excluded.
Duplicate ticket_id rows count once.
Output per priority: tickets, met (resolved within SLA), pct_met rounded to 1 decimal.
Use only pyspark.sql.functions. No UDFs. Add a docstring. Do not read or write files.''',
         note="Give rules and edge cases. Ask for small, pure functions you can test."),
    dict(type="cards", title="SmartDesk step 14: SLA metrics pipeline", items=[
        ("Bronze", "Raw ticket events as received."),
        ("Silver", "Deduplicated tickets with resolution minutes."),
        ("Gold", "SLA met % per priority per day, written as Parquet."),
        ("Verify", "Codex drafts sla_metrics; you check it against a golden example."),
    ]),
    dict(type="callout", title="Hands-on time",
         text="Build a bronze, silver and gold pipeline in PySpark, query it with Spark SQL, then generate one "
              "transformation with Codex and prove it is correct.",
         sub="Print row counts after every step. Surprises in counts are where bugs hide.",
         greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Batch pipelines", "Bronze, silver, gold. Scheduled, idempotent, observable."),
        ("Spark", "Driver plans; executors run partitions. Transformations are lazy."),
        ("SQL and production", "CTEs, windows, Spark SQL; run date, checks, run log."),
        ("AI-assisted DE", "Codex drafts; golden examples, counts and totals verify."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow: quiz on today, then Basics assessment 3.", items=[
        ("Hotel lab", "Follow Day16_Hotel_Lab.md: medallion pipeline output table."),
        ("Workbook", "Complete the Day 16 workbook."),
        ("Pre-read", "Skim the Day 17 pre-read on DevOps and the cloud."),
    ]),
]

PREREAD = dict(title="When Data Gets Big", lede="A light read before Day 16. About 15 minutes, no code required.",
               sections=[
    dict(h="Why read this?", paras=[
        "Yesterday you cleaned a few rows of data with pandas on one computer. But what if a company has billions of "
        "rows, too many for any single machine? Today you meet Apache Spark, a tool that spreads the work across many "
        "computers, and you build a pipeline that could run every night at a real company."]),
    dict(h="1. Many hands make light work", paras=[
        "Imagine counting every vote in a national election alone. It would take years. Instead, thousands of counting "
        "centres each count their own share at the same time, then send totals to a central office. Spark works like "
        "this. A **driver** (the central office) splits the job, and many **executors** (the counting centres) work in "
        "parallel."]),
    dict(h="2. Plan first, then work", paras=[
        "A good chef reads the whole recipe before starting. Spark does the same. When you describe what you want, "
        "Spark only writes it down. When you finally ask for a result, it looks at the whole plan, finds the quickest "
        "route, and then does the work. This is called **lazy evaluation**."]),
    dict(h="3. Raw, clean and ready", table=[
        ["Layer", "Kitchen version", "Data version"],
        ["Bronze", "Groceries as delivered", "Raw data exactly as received"],
        ["Silver", "Washed and chopped", "Cleaned, fixed and de-duplicated"],
        ["Gold", "The finished dish", "Summaries ready for reports"]]),
    dict(h="4. SQL is a way of asking questions", paras=[
        "SQL reads almost like English: \"show me the city and total sales, from the orders table, grouped by city, "
        "biggest first\". Analysts, engineers and many business tools all speak SQL, and Spark does too."],
        box="**Key idea:** a good pipeline can be re-run for any day and always gives the same correct answer. After "
            "every join, count the rows. If the number surprises you, stop and find out why."),
    dict(h="5. A fast assistant still needs checking", new=True, paras=[
        "OpenAI Codex can write a data transformation in seconds. A transformation that looks right can still drop "
        "rows or double-count. Today you learn to check AI-written data code against an answer you already know."]),
    dict(h="6. Think about these before class", bullets=[
        "What large task at work could be split among many people working in parallel?",
        "If a ticket refers to a customer who is not in the customer list, should it appear in the report? Why?",
        "What checks would you want before an SLA report goes to a customer?"],
        after=["Chiri mo tsumoreba yama to naru (塵も積もれば山となる): even dust, piled up, becomes a mountain"]),
])

POSTREAD = dict(title="Spark, Pipelines and SQL: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Medallion layers", "Bronze raw, silver clean, gold aggregated. Each rebuildable from the previous."],
        ["Production batch jobs", "Scheduled, idempotent, partitioned, observable."],
        ["Spark architecture", "Driver plans; executors run tasks on partitions in parallel."],
        ["Lazy evaluation", "Transformations build a plan; actions (show, count, write) run it."],
        ["Transformations", "select, filter, withColumn, when/otherwise, dropDuplicates, groupBy().agg()."],
        ["Joins", "inner, left, left_anti, left_semi. Check row counts after joining."],
        ["SQL and Spark SQL", "WHERE before groups, HAVING after; CTEs, windows; temp views + spark.sql."],
        ["Production pipeline", "Run date parameter, quality checks, overwrite per partition, run log."],
        ["AI-assisted DE (NEW v4)", "Specify rules, let Codex draft, verify with golden examples, counts and totals."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Explicit schemas", paras=[
        "inferSchema reads the data twice and can guess wrong. Production jobs declare the schema."],
        code='schema = "order_id INT, customer_id INT, amount DOUBLE, order_date DATE, city STRING"\n'
             'df = spark.read.csv("orders.csv", header=True, schema=schema)'),
    dict(sub="2. Shuffles and the plan", paras=[
        "groupBy and joins move data between executors so matching keys meet. This shuffle is the most expensive part "
        "of most jobs. Filter early and select only needed columns. Use df.explain() to see the plan."]),
    dict(sub="3. Dynamic partition overwrite", paras=[
        "Only the partitions present in the new data are replaced, so re-running one day does not delete the others."],
        code='spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")\n'
             'gold.write.mode("overwrite").partitionBy("order_date").parquet(path)'),
    dict(sub="4. Scheduling and Delta Lake", paras=[
        "Real pipelines run from a scheduler (cron, Apache Airflow, Azure Data Factory or Databricks Jobs) that passes "
        "the run date, retries and alerts. Delta Lake adds transactions, updates and time travel on top of Parquet."]),
    dict(sub="5. Reviewing AI-written SQL", paras=[
        "Ask Codex to add the business question as a comment above each query, then check the query answers that "
        "question. Common AI mistakes: an inner join that silently drops unknown customers, a filter in WHERE that "
        "belonged in HAVING, and averages of averages."]),
    dict(h="Part C: Check yourself", bullets=[
        "What do the driver and executors each do?",
        "Why does df.filter(...) return instantly even on a huge file?",
        "When would you use a left_anti join?",
        "Why should a pipeline take the run date as a parameter?",
        "Name three ways to verify a transformation that Codex wrote."]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a LAG-based day-over-day revenue change to the gold layer.",
        "Ask Codex for a new gold aggregation, then write a golden-example test for it.",
        "Use a window function to find the slowest-resolved ticket per priority."],
        after=["**Coming up on Day 17:** DevOps and cloud fundamentals, DevSecOps, Azure DevOps, and Basics "
               "assessment 3.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems building PySpark pipelines and SQL. In Colab, Spark is ready after a quick install. "
                    "In VS Code, install Java 17 and pyspark first.", problems=[
    dict(title="Hello Spark", level="Warm-up", concepts="SparkSession, createDataFrame, show",
         text="Start Spark, create a DataFrame of 5 cities with population and country, print the schema, show the "
              "rows and count them.",
         sample="root\n |-- city: string\n |-- population: long\n...\nCount: 5",
         hints=['spark.createDataFrame(list_of_tuples, ["city", "population", "country"])']),
    dict(title="Filter, Derive and Stay Lazy", level="Easy", concepts="filter, withColumn, when, laziness",
         text="From the orders data, keep amount > 0, trim city names, and add a size column: large (>= 1000), medium "
              "(>= 300) or small. Time the transformations and then count(); explain the difference.",
         sample="|order_id|city |amount|size |\n|1002    |Tokyo|1200.0|large|\nTransformations: 0.01 s | count(): 1.8 s",
         hints=["Chain F.when(...).when(...).otherwise(...).", "time.perf_counter()"]),
    dict(title="Join Detective", level="Medium", concepts="inner, left, left_anti",
         text="Join orders with customers using inner and left joins and compare row counts. Use left_anti to list "
              "orders whose customer is missing.",
         sample="orders: 10 | inner: 8 | left: 10\nOrders with unknown customer: 1009, 1010",
         hints=["Count before and after every join."]),
    dict(title="CTE and Window in Spark SQL", level="Medium", concepts="WITH, RANK() OVER, temp views",
         text="Register orders as a temp view. Using a CTE for daily city revenue, rank cities within each day and "
              "return only rank 1 per day. Confirm the result matches the same query in SQLite.",
         sample="2026-11-12 | Tokyo     | 4500.0\n2026-11-13 | Bengaluru | 3100.0\nSpark result == SQLite result: True",
         hints=["RANK() OVER (PARTITION BY order_date ORDER BY revenue DESC)"]),
    dict(title="Medallion Pipeline", level="Challenging", concepts="bronze, silver, gold, Parquet",
         text="Write raw data as bronze Parquet, clean it into silver, join and aggregate into gold daily revenue by "
              "city, partitioned by date. Re-run and show counts are unchanged.",
         sample="bronze: 12 | silver: 9 | gold: 7\nRe-run: same counts",
         hints=['mode("overwrite") makes re-runs idempotent.']),
    dict(title="Verify a Codex Transformation", level="Challenging", concepts="AI-assisted DE, golden examples",
         new=True,
         text=["Use the Codex prompt from the deck (or the notebook's online cell) to generate sla_metrics(tickets). "
               "Build a golden example of 6 tickets with a hand-calculated answer. Run the generated function, compare, "
               "and list every difference.",
               "Then check one number a second way (pandas or SQL) and write a short verdict: keep, fix or reject."],
         sample="golden: high 1/2 met (50.0%), medium 2/2 (100.0%), low 0/1 (0.0%)\n"
                "generated: high 1/3 met (33.3%)  <- duplicate ticket counted twice\nverdict: fix (add dropDuplicates)",
         hints=["Include a duplicate, an unresolved ticket and a ticket exactly on the SLA boundary.",
                "Note the prompt and roughly how many tokens it used."]),
    dict(title="Parameterised Pipeline with Quality Gates", level="Stretch", concepts="run date, checks, run log, PyTest",
         text="Write run(run_date) that processes one day through silver and gold, checks not-empty, unique keys and "
              "reconciliation, overwrites the gold partition and appends to a run log. Write PyTest tests for each "
              "check.",
         sample='run("2026-11-13") -> bronze 3, silver 3, gold 3\nRe-run -> same counts, log has 2 rows\n4 passed',
         hints=["class PipelineError(Exception): pass", "Use a session-scoped local[1] SparkSession fixture."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "The raw layer of a medallion pipeline is called ________.",
        "In Spark, the ________ plans the job and the executors run the tasks.",
        "A chunk of data processed by one task is called a ________.",
        "Spark does not run transformations until an ________ is called.",
        "To add or replace a column, use ________.",
        "A join that returns left rows with no match is a ________ join.",
        "The SQL clause that filters groups after aggregation is ________.",
        "To query a Spark DataFrame with SQL, first call createOrReplace________.",
        "Checking that gold totals equal silver totals is a ________ check.",
        "A tiny input with a hand-calculated answer used to verify AI-written code is a ________ example.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the driver and executors using the election analogy.",
        "When should you use a left join instead of an inner join?",
        "List four things that make a batch job production ready.",
        "Codex wrote a PySpark transformation that runs without errors. Why is that not enough, and how do you verify it?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "df = spark.createDataFrame([(1,), (1,), (2,)], ['id'])\nprint(df.dropDuplicates(['id']).count())",
        "orders: 10 rows, customers: 8 rows, 2 orders have no matching customer.\n"
        "print(orders.join(customers, 'customer_id', 'inner').count())   # each customer_id is unique",
        "SELECT city, COUNT(*) FROM orders WHERE amount > 0 GROUP BY city HAVING COUNT(*) > 1;\n"
        "-- rows: (Tokyo, 5), (Tokyo, -1), (Osaka, 3), (Pune, 4), (Pune, 9)\n-- which cities are returned?",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a transformation that keeps orders above 500 and adds a column amount_with_tax."),
        dict(q="Write a groupBy that counts orders and sums revenue per city."),
        dict(q="Write SQL with a CTE that finds the average daily revenue per city."),
        dict(q="Write a Codex prompt for a PySpark transformation that gives the rules, edge cases and output columns."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Medallion layers, Spark DataFrames and joins, Spark SQL, a production-style pipeline and "
                         "verifying a Codex-generated transformation", cells=[
    ("md", "## 1. Setup\nColab includes Java, so PySpark works after a quick install. In VS Code, install **Java 17** "
           "(for example Eclipse Temurin) and then `pip install pyspark`."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q pyspark openai tiktoken scikit-learn

# ===== Option B: VS Code / local (run in your terminal once) =====
# 1. Install Java 17 and check:  java -version
# 2. pip install pyspark pandas openai tiktoken scikit-learn
import os, sqlite3, time
import pandas as pd
from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder
         .master("local[1]")
         .appName("day16")
         .config("spark.sql.shuffle.partitions", "2")   # small data, fewer partitions
         .getOrCreate())
spark.sparkContext.setLogLevel("ERROR")
print("Spark", spark.version)'''),
    ("md", "## 2. Raw data (bronze input)"),
    ("code", '''%%writefile orders.csv
order_id,customer_id,amount,order_date,city
1001,1,250.50,2026-11-12, Bengaluru
1002,2,1200,2026-11-12,Tokyo
1002,2,1200,2026-11-12,Tokyo
1003,3,,2026-11-12,Osaka
1004,4,-20,2026-11-13,Pune
1005,5,560,2026-11-13,Chennai
1006,6,90.25,2026-11-13,Kyoto
1007,1,3100,2026-11-13,Bengaluru
1008,2,3300,2026-11-12,Tokyo
1009,99,780,2026-11-14,Pune
1010,98,150,2026-11-14,Osaka
1011,3,410,2026-11-14,Osaka'''),
    ("code", '''%%writefile customers.csv
customer_id,name,segment
1,Asha,retail
2,Kenji,enterprise
3,Mei,retail
4,Ravi,retail
5,Priya,enterprise
6,Hana,retail'''),
    ("code", '''orders_raw = spark.read.csv("orders.csv", header=True, inferSchema=True)
customers = spark.read.csv("customers.csv", header=True, inferSchema=True)
orders_raw.printSchema()
orders_raw.show(5)
print("Raw orders:", orders_raw.count(), "| Customers:", customers.count())'''),
    ("md", "## 3. Lazy evaluation in action"),
    ("code", '''t = time.perf_counter()
plan = (orders_raw.filter(F.col("amount") > 0)
        .withColumn("amount_tax", F.col("amount") * 1.18)
        .select("order_id", "city", "amount_tax"))
print(f"Transformations: {time.perf_counter() - t:.3f} s  (nothing ran yet)")
t = time.perf_counter()
print("Rows:", plan.count())
print(f"Action count(): {time.perf_counter() - t:.3f} s  (the whole plan ran)")'''),
    ("md", "## 4. Silver: clean and enrich"),
    ("code", '''silver = (orders_raw
    .dropDuplicates(["order_id"])
    .filter(F.col("amount").isNotNull() & (F.col("amount") > 0))
    .withColumn("city", F.trim("city"))
    .withColumn("order_date", F.to_date("order_date"))
    .withColumn("size", F.when(F.col("amount") >= 1000, "large")
                         .when(F.col("amount") >= 300, "medium")
                         .otherwise("small")))
silver.orderBy("order_id").show()
print("Silver rows:", silver.count())'''),
    ("md", "### TODO 1: Add a column `weekday` using `F.date_format(\"order_date\", \"E\")` and count orders per weekday."),
    ("code", "# TODO: write your code here"),
    ("md", "## 5. Joins: check counts every time"),
    ("code", '''inner = silver.join(customers, "customer_id", "inner")
left = silver.join(customers, "customer_id", "left")
unknown = silver.join(customers, "customer_id", "left_anti")

print("silver:", silver.count(), "| inner:", inner.count(), "| left:", left.count())
print("Orders with unknown customer:", [r.order_id for r in unknown.orderBy("order_id").collect()])
left.select("order_id", "name", "segment", "amount").orderBy("order_id").show()'''),
    ("md", "## 6. Gold: aggregate and write the medallion layers"),
    ("code", '''gold = (left
    .groupBy("order_date", "city")
    .agg(F.count("*").alias("orders"),
         F.round(F.sum("amount"), 2).alias("revenue"),
         F.round(F.avg("amount"), 2).alias("avg_order"))
    .orderBy("order_date", F.desc("revenue")))
gold.show()

orders_raw.write.mode("overwrite").parquet("lake/bronze/orders")
silver.write.mode("overwrite").parquet("lake/silver/orders")
gold.write.mode("overwrite").partitionBy("order_date").parquet("lake/gold/daily_city_revenue")
print(sorted(os.listdir("lake/gold/daily_city_revenue")))
print("Gold rows:", spark.read.parquet("lake/gold/daily_city_revenue").count())'''),
    ("md", "### TODO 2: Re-run the cell above and confirm the gold row count is unchanged. Then try `mode(\"append\")`. "
           "Which mode makes the job idempotent?"),
    ("md", "## 7. SQL refresher in SQLite, then the same query in Spark SQL"),
    ("code", '''sv = silver.select("order_id", "customer_id", "amount", F.col("order_date").cast("string").alias("order_date"),
                   "city").toPandas()
conn = sqlite3.connect(":memory:")
sv.to_sql("orders", conn, index=False)
customers.toPandas().to_sql("customers", conn, index=False)
q = lambda sql: pd.read_sql(sql, conn)

# Business question: revenue per customer segment, including unknown customers
print(q("""
SELECT COALESCE(c.segment, 'unknown') AS segment, ROUND(SUM(o.amount), 2) AS revenue
FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id
GROUP BY COALESCE(c.segment, 'unknown') ORDER BY revenue DESC
"""))'''),
    ("code", '''# Business question: the top city on each day (CTE + window function)
top_city_sql = """
WITH daily AS (
    SELECT order_date, city, ROUND(SUM(amount), 2) AS revenue
    FROM orders
    GROUP BY order_date, city
),
ranked AS (
    SELECT *, RANK() OVER (PARTITION BY order_date ORDER BY revenue DESC) AS rnk
    FROM daily
)
SELECT order_date, city, revenue FROM ranked WHERE rnk = 1 ORDER BY order_date
"""
sqlite_result = q(top_city_sql)

silver.withColumn("order_date", F.col("order_date").cast("string")).createOrReplaceTempView("orders")
spark_result = spark.sql(top_city_sql)
spark_result.show()
same = [tuple(r) for r in spark_result.collect()] == [tuple(r) for r in sqlite_result.itertuples(index=False)]
print("Spark result == SQLite result:", same)'''),
    ("md", "### TODO 3: Write a query with `LAG` that shows each day's total revenue and the change from the previous day."),
    ("code", "# TODO: write your code here"),
    ("md", "## 8. A production-style pipeline: run date, checks and a run log"),
    ("code", '''%%writefile pipeline.py
import time
from pyspark.sql import DataFrame, functions as F

class PipelineError(Exception):
    pass

def to_silver(bronze: DataFrame) -> DataFrame:
    return (bronze.dropDuplicates(["order_id"])
            .filter(F.col("amount").isNotNull() & (F.col("amount") > 0))
            .withColumn("city", F.trim("city")))

def check_not_empty(df: DataFrame, name: str):
    if df.count() == 0:
        raise PipelineError(f"{name} is empty")

def check_unique(df: DataFrame, key: str):
    if df.count() != df.select(key).distinct().count():
        raise PipelineError(f"duplicate {key}")

def to_gold(spark, silver: DataFrame, customers: DataFrame) -> DataFrame:
    silver.createOrReplaceTempView("silver")
    customers.createOrReplaceTempView("dim_customers")
    return spark.sql("""
        SELECT s.city, COALESCE(c.segment, 'unknown') AS segment,
               COUNT(*) AS orders, ROUND(SUM(s.amount), 2) AS revenue
        FROM silver s LEFT JOIN dim_customers c ON s.customer_id = c.customer_id
        GROUP BY s.city, COALESCE(c.segment, 'unknown')
    """)

def check_reconciles(silver: DataFrame, gold: DataFrame):
    s = silver.agg(F.round(F.sum("amount"), 2)).first()[0]
    g = gold.agg(F.round(F.sum("revenue"), 2)).first()[0]
    if abs(s - g) > 0.01:
        raise PipelineError(f"gold {g} != silver {s}")

def run(spark, orders: DataFrame, customers: DataFrame, run_date: str, out_path: str, log: list):
    start = time.perf_counter()
    bronze = orders.filter(F.col("order_date") == run_date)
    silver = to_silver(bronze)
    check_not_empty(silver, "silver")
    check_unique(silver, "order_id")
    gold = to_gold(spark, silver, customers)
    check_reconciles(silver, gold)
    gold.write.mode("overwrite").parquet(f"{out_path}/order_date={run_date}")
    entry = {"run_date": run_date, "bronze": bronze.count(), "silver": silver.count(),
             "gold": gold.count(), "seconds": round(time.perf_counter() - start, 2)}
    log.append(entry)
    return entry'''),
    ("code", '''import importlib, sys
sys.path.insert(0, os.getcwd())
import pipeline
importlib.reload(pipeline)
bronze_orders = orders_raw.withColumn("order_date", F.col("order_date").cast("string"))
run_log = []
for d in ["2026-11-12", "2026-11-13", "2026-11-14"]:
    print(pipeline.run(spark, bronze_orders, customers, d, "lake/gold/daily", run_log))
print("Re-run:", pipeline.run(spark, bronze_orders, customers, "2026-11-13", "lake/gold/daily", run_log))
pd.DataFrame(run_log)'''),
    ("md", "## 9. Tests for the quality gates"),
    ("code", '''%%writefile test_pipeline.py
import pytest
from pyspark.sql import SparkSession
import pipeline

@pytest.fixture(scope="session")
def spark():
    s = SparkSession.builder.master("local[1]").appName("tests").getOrCreate()
    yield s

def test_silver_removes_bad_and_duplicate_rows(spark):
    df = spark.createDataFrame([(1, 1, 10.0, "d", " A "), (1, 1, 10.0, "d", " A "), (2, 1, -5.0, "d", "B")],
                               ["order_id", "customer_id", "amount", "order_date", "city"])
    out = pipeline.to_silver(df).collect()
    assert len(out) == 1 and out[0].city == "A"

def test_empty_raises(spark):
    df = spark.createDataFrame([], "order_id INT")
    with pytest.raises(pipeline.PipelineError):
        pipeline.check_not_empty(df, "silver")

def test_duplicates_raise(spark):
    df = spark.createDataFrame([(1,), (1,)], ["order_id"])
    with pytest.raises(pipeline.PipelineError):
        pipeline.check_unique(df, "order_id")'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!python -m pytest -q test_pipeline.py

# ===== Option B: VS Code =====
# Terminal: pytest -q test_pipeline.py'''),
    ("md", "## 10. NEW (v4): AI-assisted data engineering: generate a transformation with Codex and verify it\n"
           "We ask for `sla_metrics(tickets)` (SmartDesk step 14). Online, the cell asks the model. Offline, it loads a "
           "saved AI draft. Then we verify it against a **golden example** with a hand-calculated answer."),
    ("helpers",),
    ("code", '''SPEC = """Write a PySpark function sla_metrics(tickets) for SmartDesk.
Input columns: ticket_id, priority (low|medium|high), opened_at, resolved_at (timestamp, may be null).
Rules: SLA minutes are high=60, medium=240, low=1440. Unresolved tickets are excluded.
Duplicate ticket_id rows count once.
Output per priority: tickets, met (resolved within SLA), pct_met rounded to 1 decimal.
Use only pyspark.sql.functions as F. No UDFs. Return only Python code defining sla_metrics."""

SAVED_AI_DRAFT = """from pyspark.sql import functions as F

def sla_metrics(tickets):
    sla = (F.when(F.col("priority") == "high", 60)
            .when(F.col("priority") == "medium", 240)
            .otherwise(1440))
    minutes = (F.col("resolved_at").cast("long") - F.col("opened_at").cast("long")) / 60
    return (tickets
            .filter(F.col("resolved_at").isNotNull())
            .withColumn("met", (minutes < sla).cast("int"))
            .groupBy("priority")
            .agg(F.count("*").alias("tickets"), F.sum("met").alias("met"))
            .withColumn("pct_met", F.round(F.col("met") / F.col("tickets") * 100, 1)))
"""

draft = llm(SPEC) if ONLINE else SAVED_AI_DRAFT
draft = draft.strip().removeprefix("```python").removesuffix("```").strip()
print(f"Prompt tokens: {count_tokens(SPEC)} | source: {'live model' if ONLINE else 'saved offline draft'}\\n")
print(draft)
ns = {}
exec(draft, ns)            # we only run code we have read, in a notebook, on toy data
sla_metrics_ai = ns["sla_metrics"]'''),
    ("md", "### Golden example\nSix rows, answer worked out by hand **before** running anything:\n\n"
           "| ticket | priority | minutes to resolve | met? |\n|---|---|---|---|\n"
           "| T1 | high | 30 | yes |\n| T2 | high | 90 | no |\n| T2 (duplicate row) | high | 90 | counts once |\n"
           "| T3 | medium | 240 | yes (exactly on the SLA counts as met) |\n| T4 | medium | 100 | yes |\n"
           "| T5 | low | not resolved | excluded |\n\n"
           "Expected: high 2 tickets, 1 met, 50.0%; medium 2 tickets, 2 met, 100.0%; no low row."),
    ("code", '''from datetime import datetime, timedelta
t0 = datetime(2026, 11, 17, 9, 0)
rows = [("T1", "high", t0, t0 + timedelta(minutes=30)), ("T2", "high", t0, t0 + timedelta(minutes=90)),
        ("T2", "high", t0, t0 + timedelta(minutes=90)), ("T3", "medium", t0, t0 + timedelta(minutes=240)),
        ("T4", "medium", t0, t0 + timedelta(minutes=100)), ("T5", "low", t0, None)]
golden = spark.createDataFrame(rows, "ticket_id string, priority string, opened_at timestamp, resolved_at timestamp")
expected = {"high": (2, 1, 50.0), "medium": (2, 2, 100.0)}

def check(fn, name):
    got = {r.priority: (r.tickets, r.met, r.pct_met) for r in fn(golden).collect()}
    ok = got == expected
    print(f"{name:<10} {'PASS' if ok else 'FAIL'}  got={got}")
    return ok

_ = check(sla_metrics_ai, "AI draft")'''),
    ("md", "### Review notes (offline draft)\n"
           "* **Duplicates:** no `dropDuplicates(\"ticket_id\")`, so T2 counts twice.\n"
           "* **Boundary:** uses `<` instead of `<=`, so T3 (exactly 240 minutes) is marked as missed.\n"
           "* Everything else (null filter, SLA table, rounding) matches the rules.\n\n"
           "Verdict: **fix**. The reviewed version below changes only those two lines."),
    ("code", '''def sla_metrics(tickets):
    sla = (F.when(F.col("priority") == "high", 60)
            .when(F.col("priority") == "medium", 240)
            .otherwise(1440))
    minutes = (F.col("resolved_at").cast("long") - F.col("opened_at").cast("long")) / 60
    return (tickets
            .dropDuplicates(["ticket_id"])                         # fix 1: count each ticket once
            .filter(F.col("resolved_at").isNotNull())
            .withColumn("met", (minutes <= sla).cast("int"))       # fix 2: on the SLA counts as met
            .groupBy("priority")
            .agg(F.count("*").alias("tickets"), F.sum("met").alias("met"))
            .withColumn("pct_met", F.round(F.col("met") / F.col("tickets") * 100, 1)))

_ = check(sla_metrics, "reviewed")

# Second method: the same number with pandas
pdf = golden.toPandas().drop_duplicates("ticket_id").dropna(subset=["resolved_at"])
pdf["mins"] = (pdf.resolved_at - pdf.opened_at).dt.total_seconds() / 60
pdf["met"] = pdf.mins <= pdf.priority.map({"high": 60, "medium": 240, "low": 1440})
print(pdf.groupby("priority").met.mean().mul(100).round(1).to_dict())'''),
    ("md", "### TODO 4 (SmartDesk step 14): add a `day` column (date of `opened_at`) so gold shows SLA met % per "
           "priority per day, write it as Parquet partitioned by day, and extend the golden example to two days."),
    ("code", "# TODO: write your code here"),
])
