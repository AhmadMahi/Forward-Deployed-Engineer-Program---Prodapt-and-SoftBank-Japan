"""Network diagnostics used by tier-2 support."""
import subprocess


def ping_host(host, count=1, dry_run=True):
    """Ping a cell-site gateway. dry_run returns the command without running it (used in tests)."""
    cmd = "ping -c %d %s" % (count, host)
    if dry_run:
        return cmd
    return subprocess.call(cmd, shell=True)
