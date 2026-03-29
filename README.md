# QueuePro---Smart-Queue-Management-System
QueuePro is a smart queue management system engineered to eliminate physical lines. It features remote user check-ins, dynamic wait time calculations, and a real-time administrative dashboard for staff. Built with C, Python, and Vanilla JS.
QueuePro - Smart Queue Management System

QueuePro is a comprehensive digital queue management ecosystem engineered to eliminate the congestion and friction of physical waiting lines. It features remote user check-ins, dynamic wait time calculations, and a real-time administrative dashboard for staff.

Developed as an academic project for a "Principles of Software Engineering" course, this system prioritizes algorithmic efficiency and clean UI/UX without relying on heavy web frameworks.

📑 Table of Contents

About the Project

Key Features

System Architecture

Tech Stack

Project Structure

Getting Started

Usage Guide

Roadmap

Contributing

License

📖 About the Project

In high-traffic environments such as financial institutions, healthcare facilities, and customer service centers, physical waiting lines create severe bottlenecks. QueuePro replaces these chaotic physical queues with an organized, transparent, and remote digital workflow.

By utilizing foundational data structures (implemented in C and Python) paired with a responsive Vanilla JS frontend, QueuePro demonstrates how core software engineering principles can solve real-world logistical problems.

🚀 Key Features

Remote Digital Check-In: Users can request a virtual ticket and select their required service remotely via a web portal.

Dynamic Wait Time (ETA): Calculates accurate wait times using a custom algorithm: User Position × Historical Average Service Time.

Live Administrative Dashboard: A sleek UI for staff to monitor active queues in real-time.

Inline Editable States: Staff can quickly reassign service types for any user on the fly without refreshing the page.

Asynchronous Toast Notifications: Visual alerts instantly notify staff when a new ticket is generated or the next user is called.

Zero-Dependency Frontend: Fast, lightweight DOM manipulation using pure Vanilla JavaScript.

🏗️ System Architecture

QueuePro is conceptually divided into input processing, logic management, and output rendering:

Input Module: Collects user data (Name, Service Type) via web forms or terminal prompts.

Logic & State Module: Maintains the Queue state using dynamic array lists or memory pointers. Handles the Enqueue (Join) and Dequeue (Call Next) operations.

Output & UI Module: Renders the current state of the queue, generates visual tickets, and updates the ETA clock.

🛠️ Tech Stack

Frontend: HTML5, CSS3, Vanilla JavaScript (ES6+)

Backend Algorithms: C, Python 3

Data Structures Used: Structs, Classes, Array-based Queues, Pointers

Design & UI: Glassmorphism aesthetics, Google Fonts (Inter, Outfit), FontAwesome Icons

📂 Project Structure

QueuePro/
│
├── frontend/
│   ├── index.html          # Main User/Admin Dashboard UI
│   ├── style.css           # UI Styling (Glassmorphism/Clean Themes)
│   └── script.js           # Vanilla JS DOM & State Management
│
├── backend_logic/
│   ├── queue_logic.c       # C implementation of queue structs and pointers
│   └── queue_logic.py      # Python implementation of OOP queue classes
│
├── docs/
│   ├── QueuePro_Report.pdf # Comprehensive Project Report
│   └── Presentation.html   # HTML-based modular slide deck
│
└── README.md               # Project documentation


⚙️ Getting Started

Prerequisites

To run the different components of this project, you will need:

A modern web browser (Chrome, Firefox, Safari)

Python 3.x (to run the Python logic scripts)

GCC Compiler (to compile the C logic scripts)

Installation & Execution

1. Running the Frontend Interface

No build tools (like npm or webpack) are required.

# Clone the repository
git clone [https://github.com/yourusername/QueuePro.git](https://github.com/yourusername/QueuePro.git)

# Navigate to the frontend folder
cd QueuePro/frontend

# Open index.html directly in your preferred web browser
# (On macOS: open index.html | On Windows: start index.html)


2. Testing the Backend Logic (Python)

cd backend_logic
python queue_logic.py


3. Testing the Backend Logic (C)

cd backend_logic
gcc queue_logic.c -o queue
./queue


💡 Usage Guide

Customer Flow

Open the QueuePro Dashboard.

Locate the Check-In section.

Enter your Name and select the required Service Type (e.g., Support, Billing).

Click "Join Queue". A digital ticket will be generated displaying your Ticket ID, Position, and Estimated Wait Time.

Admin/Staff Flow

View the Queue Monitor table to see all active waiting customers.

Use the "Call Next" button to automatically dequeue the first person in line.

Watch the system automatically recalculate wait times for all remaining users.

If a user needs a different service, use the Inline Dropdown in the table to update their status instantly.

🗺️ Roadmap

Future enhancements planned for the QueuePro ecosystem:

[ ] Database Integration: Implement PostgreSQL or MongoDB for persistent queue state storage.

[ ] REST API: Convert the Python logic into a Flask/FastAPI backend.

[ ] SMS Notifications: Integrate Twilio API to send users text messages when it is their turn.

[ ] Mobile App: Build a native mobile application using React Native or Flutter.

🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

Distributed under the MIT License. See LICENSE for more information.

⭐ If you found this project helpful or inspiring, please consider leaving a star on the repository!
