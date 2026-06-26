# CodeAlpha Cyber Security Internship

## 📌 Overview

This repository contains the projects completed as part of the **CodeAlpha Cyber Security Internship**. The internship focused on developing practical cybersecurity skills through hands-on projects involving network analysis, phishing awareness, and secure code review.

## 🚀 Internship Tasks

### **Task 1 – Basic Network Sniffer**

A simple **Network Packet Sniffer** developed using **Python**, **Flask**, and **Scapy** that captures live network traffic and displays packet information through a web-based dashboard.

#### Features

* Capture live network packets
* Display Source IP Address
* Display Destination IP Address
* Identify Protocol Type (TCP, UDP, ICMP)
* Display Packet Length
* Real-time packet monitoring
* Web-based interface
* Built using Flask and Scapy

#### Technologies Used

* Python 3
* Flask
* Scapy
* HTML
* CSS
* JavaScript

#### Learning Outcomes

* Understanding packet sniffing concepts
* Working with network protocols
* Flask web application development
* Real-time packet visualization
* Network traffic analysis using Scapy

---

### **Task 2 – Phishing Awareness Training**

A cybersecurity awareness presentation created to educate users about phishing attacks, social engineering techniques, and safe online practices.

#### Topics Covered

* Introduction to Phishing
* Types of Phishing Attacks
* Recognizing Phishing Emails
* Identifying Fake Websites
* Social Engineering Techniques
* Prevention Best Practices
* Real-World Phishing Examples
* Interactive Quiz

#### Learning Objectives

After completing the presentation, users will be able to:

* Understand phishing attacks and how they work
* Identify phishing emails and fake websites
* Recognize social engineering tactics
* Apply cybersecurity best practices
* Respond safely to phishing attempts

---

### **Task 3 – Secure Code Review with Bandit**

A comprehensive secure coding review of a Python Flask application using **Bandit**, an open-source Static Application Security Testing (SAST) tool, combined with manual code inspection.

#### Objectives

* Perform secure code review
* Conduct static security analysis
* Identify vulnerabilities
* Assess security risks
* Recommend remediation strategies
* Document secure coding practices

#### Tools Used

* Python
* Flask
* Bandit
* Git
* GitHub

#### Static Security Analysis

**Command Used**

```bash
bandit -r . -x .venv
```

#### Security Finding

**High Severity**

* Flask Debug Mode Enabled (`debug=True`)

**Risk**

* Exposure of stack traces
* Disclosure of application structure
* Leakage of environment information
* Sensitive debugging data

**Recommended Fix**

```python
app.run(debug=False)
```

or

```python
app.run()
```

#### Review Methodology

```
Source Code
      │
      ▼
Static Analysis (Bandit)
      │
      ▼
Manual Code Inspection
      │
      ▼
Risk Assessment
      │
      ▼
Security Recommendations
      │
      ▼
Remediation
```

#### Secure Coding Recommendations

* Disable debug mode in production
* Validate user inputs
* Handle exceptions securely
* Protect sensitive information
* Use environment variables for configuration
* Keep dependencies updated
* Apply the Principle of Least Privilege
* Perform regular security analysis
* Follow secure coding standards

#### Learning Outcomes

* Secure Software Development
* Static Application Security Testing (SAST)
* Python Security Analysis
* Vulnerability Assessment
* Risk Analysis
* Secure Coding Practices
* Security Documentation

---

# 🛠️ Technologies Used

* Python
* Flask
* Scapy
* Bandit
* HTML
* CSS
* JavaScript
* Git
* GitHub

---

# 📂 Repository Structure

```
CodeAlpha-CyberSecurity-Internship/
│
├── Task1-Basic-Network-Sniffer/
│
├── Task2-Phishing-Awareness-Training/
│
├── Task3-Secure-Code-Review-with-Bandit/
│
└── README.md
```

---

# 🎯 Skills Gained

* Network Packet Analysis
* Python Programming
* Flask Web Development
* Network Security Fundamentals
* Phishing Detection
* Cybersecurity Awareness
* Static Application Security Testing (SAST)
* Secure Coding Practices
* Vulnerability Assessment
* Risk Analysis
* Security Documentation
* Git & GitHub

---

# 📚 Internship Outcome

Through this internship, I gained practical experience in cybersecurity by building a network packet sniffer, developing phishing awareness training material, and conducting a secure code review using automated static analysis and manual inspection. These projects strengthened my understanding of network security, secure software development, cybersecurity awareness, and industry-standard security practices.

---

# 👩‍💻 Author

**Nandana Premkumar**

Developed as part of the **CodeAlpha Cyber Security Internship**.

---

## 📄 License

This repository is intended for **educational and learning purposes** as part of the CodeAlpha Internship Program.
