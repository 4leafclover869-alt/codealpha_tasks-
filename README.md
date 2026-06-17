# Basic Network Sniffer

A simple Network Packet Sniffer developed using **Python, Flask, and Scapy**. This project captures and analyzes network traffic packets and displays packet information through a web-based dashboard.

## Features

* Capture live network packets
* Display Source IP Address
* Display Destination IP Address
* Identify Protocol Type (TCP, UDP, ICMP)
* Display Packet Length
* Real-time packet monitoring
* Simple web-based interface
* Built using Flask and Scapy

## Technologies Used

* Python 3
* Flask
* Scapy
* HTML
* CSS
* JavaScript

## Project Structure

```text
Basic-Network-Sniffer/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Basic-Network-Sniffer.git
```

2. Navigate to the project directory:

```bash
cd Basic-Network-Sniffer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Npcap (Windows only)

Download and install Npcap from:
https://npcap.com

5. Run the application:

```bash
python app.py
```

6. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Output

The application displays:

* Source IP Address
* Destination IP Address
* Protocol Type
* Packet Length
* Total Packets Captured

## Learning Outcomes

* Understanding packet sniffing concepts
* Working with network protocols
* Flask web application development
* Real-time data visualization
* Network traffic analysis using Scapy

## Branch Information

This project is maintained in the **master branch**.

```bash
git checkout master
```

## Author

Developed as part of a Cyber Security and Network Analysis learning project.
