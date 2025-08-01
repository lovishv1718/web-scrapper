# 📰 Hindustan Times - News Headline Scraper

A Python-based scraper that extracts all the major article headlines from the homepage of [HindustanTimes.com](https://www.hindustantimes.com), bypassing anti-scraping measures using Selenium and storing results in a clean CSV file.

---

## 🔍 Description

This project scrapes the latest news headlines along with their URLs from Hindustan Times and stores them in a CSV file (`headlines.csv`). It is built using Selenium and BeautifulSoup, ensuring accurate extraction even from JavaScript-rendered content.

---

## ✨ Features

- ✅ **Extracts major headlines** from the homepage of Hindustan Times.
- ✅ **Cleans unwanted data** (filters out promo lines like “Don’t Miss”).
- ✅ **Stores data in CSV format** for easy use and analysis.
- ✅ **Handles JavaScript content** using Selenium (mimics real browser).
- ✅ **Headless browser mode** for silent/background scraping.

---

## 🚀 How to Use

### 1. 📦 Install Dependencies

Ensure you have Python installed, then install the required libraries:

```bash
pip install selenium beautifulsoup4 webdriver-manager
