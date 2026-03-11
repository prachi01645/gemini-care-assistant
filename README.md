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

##  Tech Stack

- Python
- Google Gemini API
- Streamlit
- JSON
   
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

##  API Key Setup

This project uses the Gemini API.

1. Get a free API key from Google AI Studio.

2. Set the environment variable.

Windows:

setx GEMINI_API_KEY "your_api_key_here"

Mac/Linux:

export GEMINI_API_KEY="your_api_key_here"

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
## 📸 Output Example

Below is an example of the AI analyzing IoT activity data.

<img width="1018" height="316" alt="image" src="https://github.com/user-attachments/assets/4481d6ee-78d8-4e48-9e3a-ad2d28d9b5f0" />

## Dashboard Demo

Run the interactive dashboard:

streamlit run src/dashboard.py

## 📊 Dashboard Preview

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/fe9b9e2d-c46a-40ea-9ed3-417a606b08eb" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/b2b4e775-5283-4dcc-a86f-dcf0916993e5" />

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/74e7e6eb-ed79-48af-98d8-41f59d2fbb94" />



   
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
## Future Improvements

• Real IoT sensor integration

• Mobile caregiver alerts

• Machine learning anomaly detection

• Streamlit dashboard improvements

• Integration with smart home devices

## Relevance to Catrobat

This project demonstrates how AI assistants can analyze user activity and generate intelligent insights.

Such AI-powered analysis could help educational tools like Pocket Code understand student learning patterns and provide personalized feedback.

## Author

## Prachi Patel

Computer Science student passionate about Artificial Intelligence, software engineering, and building intelligent applications. Currently exploring AI APIs, cloud technologies, and real-world problem solving through software projects.
