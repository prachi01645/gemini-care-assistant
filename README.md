![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-prototype-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![IoT](https://img.shields.io/badge/IoT-monitoring-blue)
![GSoC](https://img.shields.io/badge/Google%20Summer%20of%20Code-Project-blue)


# Gemini Intelligent Care Assistant

AI-powered prototype that analyzes IoT activity logs and generates health or safety alerts using Google's Gemini AI.

This project demonstrates how smart-home sensor data can be converted into meaningful insights using Large Language Models


## Project Overview

In smart homes, IoT devices such as motion sensors, kitchen sensors, and door sensors generate activity data.

This prototype reads that activity data and uses Gemini AI to analyze whether the behavior pattern looks normal or concerning.

Example scenario:

* An elderly person usually moves around every hour
* Sensors detect **no movement for 3 hours**
* The system generates an **alert message**

---

## How the System Works

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

---

## Requirements

You need the following installed:

* Python 3.9 or newer
* pip package manager
* Gemini API key from Google AI Studio

---

## Install Dependencies

Open a terminal and run:

pip install google-generativeai

---

## Get a Gemini API Key

1. Go to Google AI Studio
2. Create an API key
3. Copy the key

Then open **main.py** and replace:

genai.configure(api_key="YOUR_GEMINI_API_KEY")

with your actual API key.

---

## How to Run the Project

Step 1: Clone the repository

git clone https://github.com/prachi01645/gemini-care-assistant

Step 2: Go into the project folder

cd gemini-care-assistant

Step 3: Run the program

python main.py

---

## Example Output

AI Alert:
User has been inactive for 3 hours. Check if assistance is needed.

---

## Example IoT Data

The file **iot_data.json** contains simulated smart home sensor activity.

Example:

{
"user": "elderly_patient_01",
"activity_log": [
{"time": "08:00", "activity": "woke_up"},
{"time": "08:30", "activity": "breakfast"},
{"time": "10:00", "activity": "no_movement"}
]
}

---

## Possible Future Improvements

* Real-time sensor data streaming
* Mobile alerts for caregivers
* Anomaly detection algorithms
* Integration with health monitoring devices
* Dashboard for visualizing activity patterns

---

## Goal of This Prototype

This prototype demonstrates how AI models like Gemini can interpret IoT activity signals and transform them into meaningful insights for healthcare and assisted living systems.

---
## Future Improvements

- Real-time IoT sensor integration
- Mobile notifications for caregivers
- Web dashboard for monitoring activity
- Machine learning anomaly detection
- Integration with health monitoring devices

## Author

Prachi – AI and software enthusiast building prototypes for open-source projects and developer programs.

