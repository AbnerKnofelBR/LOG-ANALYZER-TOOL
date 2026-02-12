# LOG-ANALYZER-TOOL

Log Analyzer Tool
Overview

Log Analyzer Tool is a simple Python-based utility designed to assist Application Support Engineers in identifying recurring production issues through automated log file analysis.

The tool scans server log files and generates a summarized incident report, highlighting critical patterns such as HTTP 500 errors, timeouts, and database connection failures.

This project demonstrates practical troubleshooting logic commonly used in production support environments.

Features

Reads and processes log files line by line

Detects:

HTTP 500 Internal Server Errors

Timeout occurrences

Database connection failures

Generates a clear incident summary report

Simple and easy to extend for additional patterns

Why This Project Matters

In production environments, fast root cause identification is essential.

This tool simulates part of the incident investigation workflow by automatically identifying recurring failure patterns in log files, reducing manual inspection time and improving response efficiency.

It reflects core responsibilities of a Support Engineer:

Incident analysis

Log inspection

Pattern recognition

Production stability mindset

Technologies Used

Python 3

File handling

Basic string pattern matching

How to Run

Clone the repository:

git clone https://github.com/yourusername/log-analyzer.git


Navigate to the project folder:

cd log-analyzer


Run the script:

python analyzer.py

Sample Output
=== INCIDENT REPORT ===
500 Errors: 2
Timeouts: 2
Database Errors: 1

Future Improvements

Add timestamp grouping

Export report to CSV or JSON

Add severity scoring

Detect additional error patterns

Implement real-time monitoring

Author

Abner Nathanson Knofel Silva
Application Support Engineer | Python | SQL | Production Troubleshooting
