# Rollback test notes

1. Deploy release 2026.12.2 as canary at 10% (`CANARY_PERCENT=10`).
2. Watch quality, error rate, latency and cost per query for the canary bucket (step 30 dashboards).
3. Simulated problem: canary cost per query 40% higher than stable.
4. Roll back: `POST /admin/canary?percent=0` with the admin token from Key Vault. All users return to stable at once.
5. Result: `test_rollback_needs_admin_token` proves the switch and that it is protected.
