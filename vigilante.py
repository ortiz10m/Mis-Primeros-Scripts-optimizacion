#!/usr/bin/env python3
"""
VIGILANTE DAEMON - Core Memory Monitor
Architecture: OOP, Zero-Overhead Kernel Polling & Native Logging
"""

import time
import subprocess
import signal
import sys
import logging
from typing import Dict

# ==========================================
# ENTERPRISE CONFIGURATION
# ==========================================
THRESHOLD_PERCENT = 80.0
CHECK_INTERVAL_SEC = 60
COOLDOWN_SEC = 300
LOG_FILE = "/tmp/vigilante_daemon.log"

class VigilanteDaemon:
    def __init__(self, threshold: float, interval: int, cooldown: int) -> None:
        """Initializes the daemon parameters and logging subsystem."""
        self.threshold = threshold
        self.interval = interval
        self.cooldown = cooldown
        self.is_running = True
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Configures enterprise-grade logging to both terminal and file."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(LOG_FILE),
                logging.StreamHandler(sys.stdout)
            ]
        )
        logging.info("Vigilante Daemon initialized. Awaiting execution.")

    def shutdown(self, signum=None, frame=None) -> None:
        """Graceful shutdown sequence capturing OS signals."""
        logging.info("Shutdown signal received. Terminating Vigilante Daemon safely...")
        self.is_running = False
        sys.exit(0)

    def get_kernel_memory(self) -> float:
        """Reads /proc/meminfo directly for O(1) zero-overhead RAM calculation."""
        try:
            mem_stats: Dict[str, int] = {}
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if "MemTotal" in line or "MemAvailable" in line:
                        parts = line.split()
                        mem_stats[parts[0].strip(':')] = int(parts[1])

            if 'MemTotal' not in mem_stats or 'MemAvailable' not in mem_stats:
                return 0.0

            total = mem_stats['MemTotal']
            available = mem_stats['MemAvailable']
            used = total - available
            
            return (used / total) * 100.0

        except Exception as e:
            logging.error(f"Kernel read failure: {e}")
            return 0.0

    def trigger_alert(self, usage: float) -> None:
        """Fires a native OS notification and logs the critical event."""
        title = "🚨 VIGILANTE: CRITICAL RAM"
        message = f"Memory at {usage:.1f}%. System intervention recommended."
        
        logging.warning(f"THRESHOLD BREACHED: {message}")
        try:
            subprocess.run(["notify-send", "-u", "critical", title, message], check=False)
        except FileNotFoundError:
            logging.error("Failed to send notification: 'notify-send' dependency missing.")

    def run(self) -> None:
        """Main polling loop with smart sleeping to preserve CPU cycles."""
        logging.info(f"Monitoring Kernel memory. Threshold set to: {self.threshold}%")
        
        # Register signals for clean exit (Ctrl+C or kill commands)
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

        while self.is_running:
            usage = self.get_kernel_memory()
            
            if usage > self.threshold:
                self.trigger_alert(usage)
                logging.info(f"Entering cooldown phase for {self.cooldown} seconds...")
                time.sleep(self.cooldown)
            else:
                time.sleep(self.interval)

# --- BOOT SEQUENCE ---
if __name__ == "__main__":
    daemon = VigilanteDaemon(
        threshold=THRESHOLD_PERCENT,
        interval=CHECK_INTERVAL_SEC,
        cooldown=COOLDOWN_SEC
    )
    daemon.run()
