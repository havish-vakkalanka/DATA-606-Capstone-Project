# 1. Title and Author
- **Project Title**: Olympic Medal Prediction  
- **Capstone Prepared For**: UMBC Data Science Master’s Program by Dr. Chaojie (Jay) Wang  
- **Author**: Havish Manikya Vakkalanka  
- **GitHub Repository**: [GitHub Repository](https://github.com/havish-vakkalanka)  
- **LinkedIn Profile**: [LinkedIn Profile](https://www.linkedin.com/in/havishmanikyav/)  
- **PowerPoint Presentation**: [PowerPoint Presentation](https://docs.google.com/presentation/d/1FNZ1NlEzT5i9QThrYIV6JzASX8G70uPW/edit#slide=id.p1)  
- **YouTube Video**: [YouTube Video](https://youtu.be/52mAAX4Iku8?si=dHYsoDWotXGxm6UY)


# 2. Background  
### What is it about?  
This project focuses on predicting the total number of medals a country will win in the Olympic Games, as well as predicting the distribution of medals (Gold, Silver, Bronze). By utilizing historical data such as Olympic athlete details, event results, and country-specific information like GDP and population, this project builds predictive models to forecast Olympic medal outcomes. The models used are machine learning algorithms, particularly Random Forest, for both regression (total medal prediction) and classification (medal type prediction).  

### Why does it matter?  
Predicting medal counts is critical for national sports organizations and governments to allocate resources effectively. By identifying potential medal-winning athletes and understanding the impact of socioeconomic factors like GDP and population, countries can optimize training efforts, invest in the right sports, and maximize their chances of winning more medals. Additionally, interactive data visualizations provide key insights that inform strategic decisions in sports management.  

### Research Questions:  
- **Medal Prediction**: Can we predict the total number of medals a country will win based on factors like GDP, population, and historical performance in the Olympics?  
- **Interactive Visualizations**: How do tools like Plotly and Streamlit enhance our understanding of the dataset and model predictions?  

# 3. Data  
### Data Sources:  
Datasource link: [Olympic Historical Dataset from Olympedia](https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg/data)
- **Olympic Athlete Biography**: Personal details of athletes including height, weight, and country.  
- **Olympic Medal Tally History**: The number of medals won by each country in each Olympic edition.  
- **Olympic Games Summary**: Overview of each Olympic event (year, host city, etc.).  
- **Olympic Event Results**: Detailed results for Olympic events, including rankings.  
- **Olympic Country Profiles**: Information on participating countries.  
- **World Population**: Population data for countries from 1960 to 2020.  
- **Countries GDP**: GDP data for countries from 1960 to 2020.  

### Data Size:  
- **Olympic Athlete Biography**: 155,861 rows, 10 columns  
- **Olympic Medal Tally History**: 1,807 rows, 9 columns  
- **Olympic Event Results**: 7,394 rows, 12 columns  
- **World Population**: 217 rows, 61 columns  
- **Countries GDP**: 120 rows, 63 columns  

### Time Period:  
- **Olympic Data**: 1896 to 2020  
- **GDP and Population Data**: 1960 to 2020  

### Data Dictionary:  
- **Columns**:
    - `athlete_id (int)`: Unique ID for each athlete  
    - `edition_id (int)`: Unique ID for each Olympic edition  
    - `country_noc (string)`: Country code  
    - `medal (string)`: Medal type (Gold, Silver, Bronze)  
    - `event_title (string)`: Olympic event title  
    - `sport (string)`: Sport in which the athlete participated  
    - `year (int)`: Year of the Olympic event  
    - `population (float)`: Population of the country during that year  
    - `gdp (float)`: GDP of the country during that year  

### Target/Label Variables:  
- **Regression**: Total number of medals won by a country (target for medal count prediction).  
- **Features/Predictors**: GDP, population, athlete details (height, weight), sport participation, event details, etc.

# 4. Exploratory Data Analysis (EDA)  

### 4.1 Data Preprocessing and Cleaning  
In this stage, the dataset was prepared for model training by identifying and addressing issues like missing values, duplicates, and feature types.  

- **Missing Values**:
    - **Target Variable (Total Medal Count)**: The target variable did not have missing values. However, some features like **GDP** and **population** had missing data. These were imputed using **median imputation** for numerical features to preserve the distribution, as GDP and population are critical predictors for country-level Olympic performance.
    - For categorical features, missing values were handled by using **mode imputation** or by removing rows when appropriate.  

- **Duplicates**:
    - Duplicate rows were identified based on **athlete_id** and **edition_id** (as athletes can participate in multiple Olympics). These duplicates were removed to ensure that each row represented a unique observation and to avoid model bias.  

- **Feature Types**:
    - The dataset contained both **numerical** (e.g., GDP, population, height, weight) and **categorical** (e.g., country code, sport name) features. **Label encoding** was used for categorical variables (e.g., medal types, countries), while **one-hot encoding** was applied to sport types to represent them appropriately for the model.  

### 4.2 Outlier Detection and Removal  
Outliers can greatly impact the model’s performance, especially for regression tasks. These were identified using the **Interquartile Range (IQR)** method:  

- **Outliers in GDP and Population**:
    - Extreme values in GDP and population were flagged. Very small or extremely large countries were carefully reviewed. For example, countries with minimal populations that do not participate in many sports events were either excluded or their values transformed (e.g., using a log transformation) to minimize their impact.

- **Athlete Features (Height and Weight)**:
    - Outliers in athlete height and weight were also addressed. Values outside the typical range for human attributes were either corrected or removed, ensuring that the data remained within realistic bounds.

### 4.3 Feature Engineering  
Feature engineering enhances the model’s predictive power by creating new, informative features:  
- **Participated**: A binary feature was created to mark whether an athlete participated in an event based on the Olympic Event Results. This feature helps in excluding athletes who did not compete in an event.  
- **Event Duration**: For certain events, a new feature was created to capture the duration of the event (in minutes), which might influence medal outcomes for endurance-based sports. This new feature provided context for events that require different levels of endurance, which could impact the athlete's performance and consequently the medal prediction.

### 4.4 Data Visualization and Insights  
The EDA visualizations provided critical insights into the relationships between features and their influence on medal counts:  

- **Histogram: Total Medal Distribution**:  
    - The histogram revealed that most countries won fewer than 50 medals, with a few countries winning significantly more. This skewed distribution suggested the need for special handling of countries with extremely high medal counts, as they could disproportionately influence model predictions.  

- **Scatter Plot: GDP vs. Total Medals**:  
    - The scatter plot between **GDP** and **total medals** showed a weak positive correlation. Countries with higher GDP generally tended to win more medals, suggesting that economic investment in sports correlates with better performance. However, the relationship was not strong enough to rely solely on GDP as a predictor for medal outcomes.  

- **Scatter Plot: Population vs. Total Medals**:  
    - A positive correlation between **population size** and **total medals** was evident, indicating that countries with larger populations tend to have more athletes and more opportunities to win medals. However, this correlation was weaker than expected, and factors like training and sport specialization were not fully captured.  

- **Box Plot: Medal Distribution by Sport**:  
    - This visualization showed the distribution of medals across different sports. **Athletics** and **Swimming** had a broader range of medals, while sports like **Archery** had more concentrated results. This visualization helped identify which sports were more competitive and had a greater variety of medal outcomes.  

- **Correlation Heatmap**:  
    - The heatmap revealed key relationships between **GDP**, **population**, and **athlete attributes** (height, weight). The **positive correlation** between GDP and population was expected, but it was also clear that certain athlete characteristics (e.g., height for high-jump events) had significant predictive power for medal outcomes.

# 5. Model Training  

### 5.1 Model Selection  
The objective was to predict the total medal count a country would win in a given Olympic year, using features like GDP, population, and athlete data. Several regression models were considered for this task, and the **Random Forest Regressor** was chosen as the best model for the following reasons:  

- **Random Forest Regressor**:  
    - Random Forest is an ensemble method that uses multiple decision trees to improve accuracy and reduce overfitting. It is particularly effective in capturing **non-linear relationships** between features, which is crucial for predicting total medal counts since these factors (GDP, population, etc.) have complex interactions. Random Forest also provides **feature importance**, which helps us understand which features are most influential for predicting medal outcomes.  

- **XGBoost**:  
    - This gradient boosting algorithm was also tested, as it is known for its speed and effectiveness in large datasets. While it showed some promise, it did not significantly outperform Random Forest in capturing the interactions between country-level economic and demographic factors.

- **Logistic Regression**:  
    - Logistic regression was used as a **baseline model** for classification tasks. However, since the focus of this project was on regression, it was used primarily for comparison.  

### 5.2 Model Training and Evaluation  
The training process involved multiple steps to ensure the models were robust and could generalize well on unseen data:  

- **Train-Test Split**:  
    - The dataset was split into an **80% training** and **20% test** set. This division allowed for training the model on a large portion of the data and testing it on a smaller portion to evaluate its performance on unseen data.  

- **Cross-Validation**:  
    - **K-Fold cross-validation** was used to ensure that the model's performance was stable across different subsets of the data. This step helps mitigate the risk of overfitting and ensures the model generalizes well across different data points.

- **Hyperparameter Tuning**:  
    - The **hyperparameters** of the Random Forest model were optimized using **Grid Search** and **Randomized Search** to find the best combination of parameters, such as the **number of trees** (n_estimators), **maximum depth** (max_depth), and the **minimum number of samples required to split a node** (min_samples_split). These parameters significantly influence the model’s performance, and tuning them allowed us to achieve optimal results.

### 5.3 Model Performance and Metrics  
The performance of the model was evaluated using various metrics that assess both the accuracy and efficiency of the predictions:  

- **R² Score**:  
    - The **R² score** is the key metric for evaluating the regression model. It measures how well the model explains the variance in the total medal count. An **R² score of 0.85** indicated that the model was able to explain 85% of the variance in the target variable, which is a strong result for a predictive model.  

- **Mean Squared Error (MSE)**:  
    - **MSE** was used to measure the average squared difference between predicted and actual medal counts. A lower MSE indicates better model performance. The MSE was consistently low, reflecting the model's ability to make accurate predictions.

- **Mean Absolute Error (MAE)**:  
    - MAE was also used to quantify the average magnitude of error in the predicted total medal counts. This metric helped us understand the typical magnitude of prediction errors, which was found to be acceptable for practical purposes.

### 5.4 Feature Importance Analysis  
One of the advantages of using **Random Forest** is the ability to assess **feature importance**. The analysis showed that **GDP**, **population**, and **athlete characteristics** (height, weight) were the most important predictors for the total medal count.  

- **GDP and Population**:  
    - Both these features were highly influential in predicting the number of medals a country would win. This makes sense, as countries with larger economies and populations tend to have more resources to invest in sports training and infrastructure.  

- **Athlete Data (Height and Weight)**:  
    - **Athlete characteristics** were important, particularly for sports like high jump or swimming. These features helped refine the model’s accuracy when predicting outcomes in certain sports where physical attributes play a significant role.

# 6. Application of the Trained Models  
A **Streamlit** app was developed for users to interact with the trained models. The app allows users to input features like:  
- Athlete count, GDP, population, sport type, and event count, and receive predictions on the total medal count for a given country in a specified Olympic year.  
- The input is processed, categorical variables are encoded, and the **Random Forest Regressor** predicts the medal count based on the provided features.  

The app was developed using:  
- **Streamlit** for the user interface.  
- **joblib** to load the trained Random Forest models.  
- **Interactive visualizations** (via **Plotly**) to explore historical trends in medal counts and understand how different factors influence medal predictions.

# 7. Conclusion  
### Summary of Work:  
This project developed a **Random Forest Regressor** model to predict the total number of Olympic medals a country would win based on factors like GDP, population, and athlete data. We built an interactive **Streamlit** web application that allows users to input specific details and receive real-time predictions.  

### Practical Application:  
The model and app can be used by sports analysts, national sports organizations, and policymakers to better allocate resources, improve training strategies, and increase the chances of winning Olympic medals by targeting key areas such as GDP, population, and athlete characteristics.  

### Limitations:  
- **Limited data scope**: The models are based on historical data, which may not account for real-time changes or unquantifiable factors like athlete injuries.  
- **Model simplifications**: Although Random Forest performs well, it might oversimplify some relationships, and more complex models could potentially improve prediction accuracy.  

### Lessons Learned:  
- **Feature engineering** was crucial for improving the model's accuracy by creating meaningful new features.  
- The iterative development of the model and continuous testing helped refine the features.

### Future Research Directions:  
- Incorporating more detailed athlete-specific data, injury history, or psychological factors could improve prediction accuracy.  
- Experimenting with more sophisticated machine learning algorithms, such as XGBoost, neural networks, or deep learning, could lead to enhanced performance.  
- A mobile version of the Streamlit app could improve accessibility, allowing users to make predictions on-the-go.
