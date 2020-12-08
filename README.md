# Fraud Analysis 
A project on fraud analysis of insurance claims.

### Requirements

    - Python3
        - mimesis     4.1.2 (elizabeth is no longer available)
        - faker       5.0.1
        - matplotlib  3.2.0
        - numpy       1.19.1
        - pandas      1.1.5
        - sklearn     0.0
        - pydotplus   2.0.2
        - openpyxl    3.0.5
    - Grahviz
        - Windows -> https://graphviz.org/download/
        - Unix -> sudo apt-get install graphviz

Note: This repository isn't maintained often, use at your own discretion. Error handling was not a priority when scripting.

## Installation
```bash
pip install -r requirements.txt
```
After the required packages are installed you can simply run the scripts from the phases below.


## Phases

#### Create Database
Create the database with meaningful random data.
```bash
python createDatabase.py
```
            
#### Cleaning the data
Cleaning invalid data/rows that does not meet a defined criteria. Fills in data using samples or a mean/median.
```bash
python cleaning.py

```    
#### EDA
Exploratory Data Analysis - understand the data and data types as well as some statistics and graphing to see the distribution, correlation, anomalies and outliers of the data. 
```bash
python eda.py
```
    
 
#### PPDM
Privacy Preserving Data Mining - suppress, generalize, anatomization, perturbation, categorize, k-anonymity is done in order to preserve privacy so that sensitive attributes cannot identify a person without having the entire dataset. This makes the data safer in an instance the data is leaked, it makes it harder to impersonate someone.  
```bash
python ppdm.py
```
    
#### Machine learning
Machine leaning was used to detect fraudulent insurance claims. This uses a simple decision tree classifier and was trained with 70/30 train/test ratio. The accuracy of the prediction was ~99% with 73117 training elements and 18280 testing elements. The tree can be seen in `insurance.pdf`.  
```bash
python machine_learning.py
```    
