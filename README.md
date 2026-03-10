![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-prototype-green)
 
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![IoT](https://img.shields.io/badge/IoT-monitoring-blue)
![GSoC](https://img.shields.io/badge/Google%20Summer%20of%20Code-Project-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)



# Gemini Intelligent Care Assistant

# Gemini IoT Care Assistant

An AI-powered intelligent care assistant that interprets IoT activity data and generates context-aware insights using the Gemini API.

This project demonstrates how responsible AI can support caregivers and families by transforming raw IoT activity signals into understandable alerts and explanations.

This project demonstrates how smart-home sensor data can be converted into meaningful insights using Large Language Model


## Project Overview

In smart homes, IoT devices such as motion sensors, kitchen sensors, and door sensors generate activity data.

This prototype reads that activity data and uses Gemini AI to analyze whether the behavior pattern looks normal or concerning.

Example scenario:

* An elderly person usually moves around every hour
* Sensors detect **no movement for 3 hours**
* The system generates an **alert message**
 2ea15b926419142eb538323bcb68c74dadeb7abf

---

# Features

HEAD
- IoT activity data ingestion
- Pattern detection for abnormal behavior
- Explainable alerts with confidence scores
- AI-generated explanations using Gemini
- Role-based responses for caregivers, family members, and supervisors

The project follows a simple pipeline:

IoT Sensors → Activity Data → AI Analysis → Alert

1. IoT sensors generate activity logs
2. The logs are stored in a JSON file
3. Python reads the data
4. Gemini AI analyzes the activity pattern
5. The system prints an alert if needed
   
## Quick Start

Follow these steps to run the prototype.

### 1. Clone the repository

git clone https://github.com/prachi01645/gemini-care-assistant.git

### 2. Move into the project folder

cd gemini-care-assistant

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the program

python src/main.py

## Requirements

- Python 3.9+
- pip

## Demo

Example activity data:

[
 {"time": "08:00", "activity": "woke_up"},
 {"time": "08:30", "activity": "breakfast"},
 {"time": "09:00", "activity": "movement_detected"},
 {"time": "10:00", "activity": "no_movement"},
 {"time": "11:00", "activity": "no_movement"}
]

Example system output:

AI Alert:
User inactive for extended period. Check assistance.

---
## Dashboard Demo

Run the interactive dashboard:

streamlit run src/dashboard.py
   
## System Architecture

            +------------------+
            |  IoT Sensors     |
            | (Motion, Door)   |
            +---------+--------+
                      |
                      v
             +----------------+
             | iot_data.json  |
             | Activity Logs  |
             +-------+--------+
                     |
                     v
              +-------------+
              |  main.py    |
              | Data Reader |
              +------+------+
                     |
                     v
        +-----------------------------+
        | Gemini AI Analysis Engine   |
        +--------------+--------------+
                       |
                       v
               +---------------+
               | AI Alert      |
               | Output        |
               +---------------+
---

## Project Structure

gemini-care-assistant/

main.py – main program that runs the AI analysis
iot_data.json – sample IoT activity dataset
README.md – project documentation
>>>>>>> 2ea15b926419142eb538323bcb68c74dadeb7abf

---

# Project Structure
