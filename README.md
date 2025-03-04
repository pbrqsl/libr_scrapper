# Librus Scraper

## Overview
Librus Scraper is a Python tool I built as one of my first portfolio projects to automate monitoring grades and messages on the [Librus](https://portal.librus.pl) educational platform, widely used in Polish schools. It logs into the portal, scrapes student grades and messages, compares them to previous data, and sends updates via Telegram—perfect for parents or students who want to stay informed without constant manual checks.

This was an early dive into web scraping, file handling, and notifications, and it taught me a ton about automation and modular code. Since then, I’ve leveled up my skills, but this project remains a cool example of solving a real-world problem with code!

## Features
- **Automated Login**: Uses Selenium to log into Librus with a username and password.
- **Grade & Message Scraping**: Extracts grades and messages from the portal.
- **Change Detection**: Compares new data with saved files to spot updates.
- **Telegram Notifications**: Sends alerts about new grades or messages to a specified user.
- **Local Storage**: Saves data to files for persistence and comparison.
- **Logging**: Tracks activity in a `logs.txt` file for debugging.

## Technologies Used
- **Python 3**: Core language.
- **Selenium**: Web automation and scraping.
- **Logging**: Basic activity tracking.
- **File I/O**: JSON-like data storage.
- **Telegram API** (via custom `Message` class): Notifications.

## Prerequisites
- **Python 3.6+**: Installed on your system.
- **Chrome Browser**: For Selenium to control.
- **ChromeDriver**: Matching your Chrome version, downloadable from [here](https://chromedriver.chromium.org/downloads).
- **Dependencies**: Install via pip:
  ```bash
  pip install selenium
