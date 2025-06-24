# 📊 Demographic Data Analyzer

## Overview

This project performs an in-depth analysis of demographic data extracted from the **1994 U.S. Census** using **Python and Pandas**. It answers a variety of real-world socio-economic questions related to **age, education, income, work hours, occupation, and nationality**.

As a **data scientist**, this project showcases proficiency in:
- Cleaning and transforming real-world datasets
- Extracting statistical insights from categorical and numerical data
- Leveraging Python (Pandas) for exploratory data analysis (EDA)

---

## 👨🏽‍💻 Author

**Eniitan Oluwatoyin Shadrack**  
_Data Scientist | Lecturer | Community Health Data Analyst_  
📫 `oluwatoyin.eniitan2020@gmail.com`

---

## 📂 Dataset

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult)
- Title: Adult Income Dataset
- Description: Data was extracted from the 1994 U.S. Census database
- Format: CSV (`adult.data.csv`)

---

## 🧠 Questions Answered

1. 📈 How many people of each race are represented in this dataset?
2. 👨 What is the average age of men?
3. 🎓 What percentage of people have a Bachelor's degree?
4. 💼 What percentage of people with **advanced education** (Bachelors, Masters, Doctorate) earn more than 50K?
5. 📉 What percentage of people **without advanced education** earn more than 50K?
6. ⏱️ What is the **minimum number of work hours** per week?
7. 💰 What percentage of those working **minimum hours** earn more than 50K?
8. 🌍 Which **country has the highest percentage** of people earning more than 50K?
9. 🇮🇳 What is the **most common occupation** among those earning >50K in **India**?

---

## 🧪 Sample Output (Abbreviated)

```python
{
  'race_count': White    27816
                Black     3124
                Asian     1039
                ...
  'average_age_men': 39.4,
  'percentage_bachelors': 16.4,
  'higher_education_rich': 46.5,
  'lower_education_rich': 17.0,
  'min_work_hours': 1,
  'rich_percentage_min_hours': 10.0,
  'highest_earning_country': 'India',
  'highest_earning_country_percentage': 41.9,
  'top_IN_occupation': 'Prof-specialty'
}
