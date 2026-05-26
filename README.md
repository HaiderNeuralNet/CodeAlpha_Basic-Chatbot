# 🤖 CodeAlpha Basic Chatbot

> A simple, beginner-friendly Python chatbot that responds to user inputs with personalized responses — built with pure Python, no external libraries required.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Code Theory](#-code-theory)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Key Concepts Used](#-key-concepts-used)
- [Sample Output](#-sample-output)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 About the Project

This project was built as **Task 2** of a Python beginner assignment at CodeAlpha. The goal is to build a simple chatbot that:

- Accepts text input from users
- Matches keywords using conditional statements
- Responds with appropriate pre-defined answers
- Handles unknown inputs with a fallback message
- Provides exit commands to end the conversation

**Creator:** Haider Ali Shah

No external APIs, machine learning, or NLP libraries needed — just pure Python!

---

## ✨ Features

| Feature | Description |
|---|---|
| 👋 Personalized Greeting | Responds with a warm welcome including the creator's name |
| 🏷️ Name Recognition | Knows and responds when asked "what is my name" |
| ❓ Question Answering | Answers questions like "how are you" and "what is your name" |
| 🆘 Help Command | Responds to "help" with information about capabilities |
| 🚪 Exit Commands | Gracefully ends conversation with "bye", "exit", or "quit" |
| 🔤 Case-Insensitive | Treats "Hello", "HELLO", and "hello" the same way |
| 🛡️ Fallback Handler | Responds gracefully when input isn't understood |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed:



##  1. Clone the repository
git clone https://github.com/HaiderNeuralNet/CodeAlpha_Basic-Chatbot.git

## 2. Navigate into the folder
cd CodeAlpha_Basic-Chatbot

## 3. Run the program
python task2.py

## ⚙️ How It Works
```bash
┌─────────────────────────────────────────────────────┐
│                   PROGRAM FLOW                      │
├─────────────────────────────────────────────────────┤
│  1. Display "Chatbot is running" message            │
│  2. Enter infinite while loop                       │
│  3. Get user input and convert to lowercase         │
│  4. Check conditions in sequence:                   │
│     - Greetings (hello, hi, hey)                    │
│     - "your name" in input                          │
│     - "how are you" in input                        │
│     - "help" in input                               │
│     - "what is my name" in input                    │
│     - Exit commands (bye, exit, quit)               │
│  5. Print appropriate response from functions       │
│  6. Repeat until exit command triggers break        │
└─────────────────────────────────────────────────────┘
```
## 📁 Project Structure
```bash
CodeAlpha_Basic-Chatbot/
│
├── task2.py              # Main chatbot program
└── README.md             # Project documentation
```
## 👨‍💻 Author
First, solve the problem. Then, write the code.

