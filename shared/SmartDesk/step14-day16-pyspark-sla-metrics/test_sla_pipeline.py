import pytest

pyspark = pytest.importorskip("pyspark")

from sla_pipeline import gold, sample_events, silver, spark_session  # noqa: E402


@pytest.fixture(scope="module")
def spark():
    s = spark_session()
    yield s
    s.stop()


def test_gold_metrics(spark):
    rows = {r["category"]: r for r in gold(silver(sample_events(spark))).collect()}
    assert rows["billing"]["breaches"] == 1          # ticket 2: 8 hours on a 4 hour SLA
    assert rows["network"]["breach_rate"] == 0.5     # ticket 4 breached, ticket 1 did not


def test_duplicates_dropped_and_open_excluded(spark):
    s = silver(sample_events(spark))
    assert s.count() == 6
    assert "account" in {r["category"] for r in gold(s).collect()}
