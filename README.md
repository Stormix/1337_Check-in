# 1337_Check-in

[![GitHub issues](https://img.shields.io/github/issues/Stormiix/1337_Check-in.svg?style=flat-square)](https://github.com/Stormiix/1337_Check-in/issues)
[![GitHub forks](https://img.shields.io/github/forks/Stormiix/1337_Check-in.svg?style=flat-square)](https://github.com/Stormiix/1337_Check-in/network)
[![GitHub stars](https://img.shields.io/github/stars/Stormiix/1337_Check-in.svg?style=flat-square)](https://github.com/Stormiix/1337_Check-in/stargazers)

A POC python script that checks if check-in is available or not.
## Setup

1. Clone the repository

```
  git clone https://github.com/Stormiix/1337_Check-in.git
```

## Installation

1. Install Python
2. Install pip
3. Install packages from requirements.txt

```
  pip install -r requirements.txt
```

## Configure the script

1. Download the web drivers from the [releases](https://github.com/Stormiix/1337_Check-in/releases) page and add them to a "Drivers/" folder
2. Modify main.py and change both lines 7 & 8:

```python
    email = "your email address"
    password = "your password"
```
P.S : You can also change the scraper's delay time, by default it's 2sec

## Run the script

```
  python main.py
```
  
# Resources
**ChromeDriver**
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

**Selenium**
[Selenium](http://www.seleniumhq.org/)<br>
