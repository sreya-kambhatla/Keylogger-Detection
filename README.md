# 🔐 Keylogger Detection & Monitoring Toolkit

## Overview

Keylogger Detection & Monitoring Toolkit is a Python-based security project designed to **detect suspicious keylogging behavior** by monitoring system processes, file system activity, and clipboard usage. The project combines rule-based detection techniques with optional machine learning and cryptographic utilities to analyze, flag, and log potentially malicious behavior.

This repository demonstrates practical applications of:

* System process monitoring
* Suspicious file activity detection
* Clipboard inspection
* Basic threat logging
* Encryption key generation and decryption utilities
* ML-assisted process analysis
* Task snapshot collection and data preparation

It is intended for **educational, research, and defensive security experimentation**.

---

## ✨ Features

### Core Detection Module

* Monitors running processes using `psutil`
* Flags suspicious Python processes that resemble keylogger execution patterns
* Tracks newly created `.txt`, `.wav`, and `.png` files in monitored directories
* Logs suspicious file events to CSV for audit trails
* Monitors clipboard activity for unusually large captured content

### Machine Learning Module

* Collects process snapshots
* Prepares process datasets for analysis
* Integrates ML-based detection workflows
* Supports CSV-based training and evaluation data

### Cryptography Utilities

* Encryption key generation
* File decryption support
* Key storage handling for secure workflows

### Logging & Data Output

* CSV-based logging of suspicious files
* Process snapshot exports
* Structured datasets for ML experiments

---

## 🧱 Project Structure

```
Keylogger-Detection-main/
│
├── KeyLogger_Detection/
│   ├── Keylogger Detector.py
│   ├── Keylogger.py
│   ├── Requirements.txt
│   ├── suspicious_files.csv
│   └── Cryptography/
│       ├── GenerateKey.py
│       ├── DecryptFile.py
│       └── encryption_key.txt
│
├── Keylogger_Detection_ML/
│   ├── ML Integration.py
│   ├── Task Manager.py
│   ├── WebScraping.py
│   ├── process_data.csv
│   └── task_manager_snapshot.csv
```

---

## ⚙️ Requirements

Install dependencies before running the project.

```
pip install -r Requirements.txt
```

Typical dependencies include:

* psutil
* pywin32
* csv (standard library)
* os (standard library)
* time (standard library)

> Note: This project is currently Windows-focused due to Win32 API clipboard monitoring.

---

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/Keylogger-Detection.git
cd Keylogger-Detection
```

### 2. Install Dependencies

```
pip install -r KeyLogger_Detection/Requirements.txt
```

### 3. Configure Monitoring Path

Edit the directory path inside:

```
KeyLogger_Detection/Keylogger Detector.py
```

Update:

```
file_path = "YOUR_TARGET_DIRECTORY"
```

### 4. Run the Detector

```
python "Keylogger Detector.py"
```

The script will continuously monitor:

* Running processes
* File creation patterns
* Clipboard behavior

---

## 🧠 Machine Learning Workflow (Optional)

The ML module can be used to:

* Capture task manager snapshots
* Build process datasets
* Run ML-assisted detection experiments

Run from the ML directory:

```
python "Task Manager.py"
python "ML Integration.py"
```

---

## 🔑 Cryptography Tools

Generate encryption keys and decrypt files using:

```
python GenerateKey.py
python DecryptFile.py
```

These utilities support secure handling and experimentation with protected files.

---

## 📊 Output Files

The toolkit produces several artifacts:

* `suspicious_files.csv` → flagged file events
* `process_data.csv` → ML dataset inputs
* `task_manager_snapshot.csv` → process snapshots

These can be used for:

* Threat analysis
* Model training
* Behavioral research

---

## ⚠️ Limitations

* Primarily designed for Windows systems
* Detection rules are heuristic-based and may produce false positives
* Not intended as a production antivirus replacement
* Requires manual directory configuration

---

## 🎯 Use Cases

* Academic cybersecurity projects
* Defensive security demonstrations
* Behavioral malware detection experiments
* ML-based process classification studies

---

## 🛡️ Ethical Use Notice

This project is built for **defensive and educational purposes only**. Do not deploy monitoring or detection tools on systems without proper authorization.

---

## 📌 Future Improvements

* Real-time alert notifications
* Behavioral scoring engine
* Anomaly detection models
* Centralized dashboard
* Automated response actions

---

## 👥 Contributors

* Sreya Kambhatla — Developer
* Nitya Ramachandran — Developer

---

Sreya Kambhatla<br>
Data Analyst | Business Analyst<br>
SQL • Python • Power BI • Analytics Engineering


