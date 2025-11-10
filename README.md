# SVCMON
A service that monitors other services. Based on Python.

## Background
When supporting certain software in a corporate setting, the server-side service often experiences issues and goes down.  
This causes disruptions to customers, and the fastest way to resolve them is usually by restarting the service on the server side.  

With this monitoring software, I aim to collect simple statistics and automatically handle these service interruptions.

**Why not fix the issue directly?**  Well, I'm not allowed to access the source code of the software I'm supporting.

**Why Python?** The goal is to install this on the customer's server, and Python is the only language available to me without disturbing existing services. Also, this technically isn't an official software provided by my employer.

## Requirements
- **Python:** 3.9  
- **OS tested:** Rocky Linux 9.4  
- **Dependencies:** None (intentionally limited to built-in Python 3.9 modules)

---

## Setup
### 1. SQLite
1. Rename dal/data_blank.db to dal/data.db.
2. Fill in ports and services in the port and service tables.

### 2. Services
| Service | Description |
| --- | --- |
| `svcmon.service` | Main service, also hosts a web view. Default port: 8888 |
| `svcmon-check.service` | Scheduled task to check ports and services |
| `svcmon-check.timer` | Timer that executes svcmon-check.service every hour at 00 minutes |

### 3. Server Directoy
Upload all files to `/opt/svcmon/`.  
If you prefer a different directory, make sure to update the `ExecStart` path in the service and timer files accordingly.