# Olympic Medal Prediction and Classification

## 1. Title and Author

* **Project Title**: Olympic Medal Prediction and Classification
* **Prepared for**: UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang
* **Author Name**: Havish Manikya Vakkalanka
* **GitHub Repository**: [GitHub Repo](https://github.com/havish-vakkalanka)
* **LinkedIn Profile**: [LinkedIn Profile](https://www.linkedin.com/in/havishmanikyav/)
* **PowerPoint Presentation**: PowerPoint Presentation
* **YouTube Video**: YouTube Video

---

## 2. Background

### What is it About?
This project focuses on predicting the total medal count won by a country in the Olympics and classifying the type of medal (Gold, Silver, or Bronze). By leveraging historical Olympic data, such as athlete details, event results, and country-specific information (like population and GDP), we aim to create a model that predicts a country's overall medal performance and the specific medals an athlete or team may win.

### Why Does it Matter?
1.  Medal predictions can assist national sports organizations in identifying potential medal winners early, allowing them to focus on athlete training and resource allocation.
2. Countries invest heavily in sports training. By predicting the outcome of competitions, these investments can be better targeted to maximize the number of medals won.
3. By analyzing various factors like GDP, population, and athlete data, we can uncover insights into how countries and individual athletes succeed, helping to drive better decisions at both a national and individual level.

### Research Questions:
1. **Medal Prediction**: Can we predict the total number of medals a country will win based on factors such as GDP, population, and historical Olympic performance?
2. **Medal Classification**: Can we classify the medals (Gold, Silver, Bronze) an athlete or country will win based on various athlete characteristics and event results?
3. How do interactive visualizations using Plotly and Streamlit enhance our understanding of the data and model results?

---

## 3. Data

### Data Sources:
Datasource link: [Olympic Historical Dataset from Olympedia](https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg/data)
* **Olympic Athlete Biography**: Personal details of athletes including height, weight, and birthdate.
* **Olympic Medal Tally History**: Historical data on the number of medals won by each country in different Olympic editions.
* **Olympic Games Summary**: Summary information about each Olympic event (year, city, etc.).
* **Olympic Event Results**: Detailed results of specific events, including rankings and participation.
* **Olympic Country Profiles**: Country details relevant to the Olympics.
* **World Population**: Population data from 1960 to 2020.
* **Countries GDP**: GDP data from 1960 to 2020.

### Data Shape:
* **Olympic Athlete Biography**: 155,861 rows, 10 columns
* **Olympic Medal Tally History**: 1,807 rows, 9 columns
* **Olympic Games Summary**: 64 rows, 11 columns
* **Olympic Event Results**: 7,394 rows, 12 columns
* **Olympic Country Profiles**: 235 rows, 2 columns
* **World Population**: 217 rows, 61 columns
* **Countries GDP**: 120 rows, 63 columns

### Time Period:
* **Olympic Data**: 1896 to 2020
* **Population and GDP Data**: 1960 to 2020

### What Does Each Row Represent?
* **Olympic Athlete Biography**: Each row represents an athlete who participated in the Olympics, detailing their personal attributes like height, weight, and country.
* **Olympic Medal Tally History**: Each row summarizes the medal tally for a specific country in a given Olympic edition.
* **Olympic Games Summary**: Each row provides a summary of an Olympic edition (e.g., 2008 Summer Olympics in Beijing).
* **Olympic Event Results**: Each row contains results for a specific Olympic event, such as 100m Sprint or Weightlifting.
* **Olympic Country Profiles**: Each row represents a country that has participated in the Olympics.
* **World Population**: Each row contains the population data of a country for a specific year.
* **Countries GDP**: Each row contains the GDP data of a country for a specific year.

### Data Dictionary:

| **Column Name** | **Data Type** | **Definition** | **Values (for categorical)** |
|-----------------|---------------|----------------|------------------------------|
| athlete_id      | int           | Unique ID for each athlete | N/A |
| edition_id      | int           | Unique ID for each Olympic edition | N/A |
| country_noc     | string        | National Olympic Committee country code | N/A |
| medal           | string        | Type of medal won by the athlete | Gold, Silver, Bronze |
| event_title     | string        | Title of the Olympic event | Various event titles |
| sport           | string        | Sport in which the athlete participated | Various sports (e.g., Athletics) |
| year            | int           | Year of the Olympic event | N/A |
| population      | float         | Population of the country during that year | N/A |
| gdp             | float         | GDP of the country during that year | N/A |

### Image:

Here’s the data schema representing the datasets used for this project:

![Olympic Data Schema](https://datas.fun/olympic.png)

### Target/Label:
* The target variable for the prediction task is the **total number of medals** a country will win.
* The target variable for the classification task focuses on predicting the **type of medal** (Gold, Silver, or Bronze) based on athlete and event-specific data.

### Features/Predictors:
Key features used for the prediction and classification models include:
* **Athlete Data**: Attributes like height, weight, and sex that may influence an athlete's performance.
* **Event Data**: Information about the sport, event, and year of the competition.
* **Country Data**: Factors like population and GDP, which may affect the country's overall performance in the Olympics.

---

## 4. Developing a Medal Prediction Web App using Streamlit and Plotly

### Overview:

A **Streamlit web app** will be developed to allow users to interact with the Olympic medal prediction and classification models. The app will offer an easy-to-use interface for both individual users and researchers to predict the total medal count for a specific country or athlete in a particular Olympic year. Additionally, the app will showcase **interactive visualizations** to explore historical data and model insights.

### App Features:

* **Input Forms**:
    - Users can input country details such as specific Olympics year to predict the total number of medals that country will win.
    - Users can also input athlete-specific details, such as sport, height, weight, and country, to predict the type of medal (Gold, Silver, or Bronze) that the athlete might win in their event.

* **Predictions**:
    - The app will use the pre-trained models to predict the total medal count for a selected country in a given Olympics year based on socio-economic and historical data.
    - For individual athletes, the app will classify the type of medal (Gold, Silver, or Bronze) based on their characteristics and sport.

* **Visualization with Plotly**:
    - The app will feature **interactive visualizations** showing:
        1. **Historical Medal Data**: A breakdown of medals won by different countries over various Olympic years, allowing users to explore past performance trends.
        2. **Predicted Medal Outcomes**: Visual representations of the predicted medal counts for countries or athletes based on user inputs.
        3. **Country and Athlete Comparisons**: Users will be able to compare multiple countries or athletes' predicted outcomes on the same chart, making it easier to identify key trends.

* **Dynamic Visualization Dashboard**:
    - A customizable dashboard will allow users to adjust parameters (like country, year, and athlete characteristics) and instantly see updated predictions and visualizations. This feature will provide insights into how different factors (e.g., sport, country’s GDP, and population) influence medal predictions.

This app will serve as a comprehensive tool for sports analysts, athletes, and fans to predict Olympic outcomes and explore patterns in historical Olympic data.

---

## 5. Conclusion

Summarize your work and its potential application.

---
