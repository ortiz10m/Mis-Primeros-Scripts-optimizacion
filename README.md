# 👁️ Vigilante Daemon (System Optimization Suite)

*Evolution of my early optimization scripts into a professional architecture.*

Originally a collection of basic bash scripts, this repository has been fully refactored into an enterprise-grade, zero-overhead background service written in Python. It strictly monitors RAM usage directly from the Linux Kernel (`/proc/meminfo`) to completely avoid the performance penalty of calling external commands.

---

## 🚀 Architecture & Features
- **Zero Overhead Polling:** Reads direct Kernel memory states (O(1) complexity) instead of relying on `free` or `awk` subprocesses.
- **Graceful Shutdown:** Implements Python's `signal` module to intercept OS kill signals (`SIGINT`, `SIGTERM`) for safe termination.
- **Professional Logging:** Maintains a permanent execution history at `/tmp/vigilante_daemon.log`.
- **Native OS Integration:** Triggers non-intrusive Linux desktop notifications via `notify-send` during critical memory states.

## 📥 Deployment
Requires Python 3. No external `pip` dependencies needed.

```bash
# Clone the repository
git clone [https://github.com/ortiz10m/Mis-Primeros-Scripts-optimizacion.git](https://github.com/ortiz10m/Mis-Primeros-Scripts-optimizacion.git)

# Enter the directory
cd Mis-Primeros-Scripts-optimizacion

# Run the daemon
python3 vigilante.py

## 🤝 Support & Connect
Great software is built with discipline and an obsession for optimization step by step. 

* 🎥 **Follow the journey:** For deep dives into system architecture, clean code, and the stoic mindset required to build great things, join the community on my YouTube channel: **DavOS**. Let's build efficiently.
