"""Drift watch: input drift (ticket categories, message length) and provider or model drift (golden set score)."""
import math
from collections import Counter

PSI_ALERT = 0.2


def psi(expected, actual, categories):
    """Population stability index between two lists of labels."""
    e, a = Counter(expected), Counter(actual)
    total = 0.0
    for c in categories:
        pe = max(e[c] / len(expected), 1e-4)
        pa = max(a[c] / len(actual), 1e-4)
        total += (pa - pe) * math.log(pa / pe)
    return round(total, 3)


def length_drift(baseline_lengths, current_lengths, tolerance=0.3):
    b = sum(baseline_lengths) / len(baseline_lengths)
    c = sum(current_lengths) / len(current_lengths)
    return abs(c - b) / b > tolerance, round(c / b, 2)


def provider_drift(scores_by_day, drop=0.05):
    """Scheduled eval (CI or Codex automation) runs the golden set daily on the same prompt and model name.
    A drop larger than `drop` against the first day means the provider changed behaviour."""
    first = scores_by_day[0][1]
    return [(day, s) for day, s in scores_by_day if first - s > drop]


def drift_alerts(baseline_cats, current_cats, baseline_len, current_len, scores_by_day):
    alerts = []
    p = psi(baseline_cats, current_cats, ["billing", "network", "account", "other"])
    if p > PSI_ALERT:
        alerts.append(f"category drift: PSI {p} > {PSI_ALERT}")
    drifted, ratio = length_drift(baseline_len, current_len)
    if drifted:
        alerts.append(f"message length drift: x{ratio}")
    for day, s in provider_drift(scores_by_day):
        alerts.append(f"provider drift on {day}: golden set score {s}")
    return alerts
