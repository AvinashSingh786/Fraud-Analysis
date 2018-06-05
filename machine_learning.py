import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
import pandas as pd
from Color import Color
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import sqlite3
import pydotplus


# mmnist = input_data.read_data_sets("data", one_hot=True)
def load_data():
    print(Color.YELLOW + "Opening Database" + Color.END)
    conn = sqlite3.connect('insurance.db')
    print(Color.YELLOW + Color.UNDERLINE + "Reading data ..." + Color.END)
    df = pd.read_sql_query("SELECT * FROM Claims", conn, coerce_float=True,
                           parse_dates=["Date_Of_Birth", "Policy_Start",
                                        "Policy_End", "Date_Of_Loss", "Date_Of_Claim"])

    iris = load_iris()



    iris.feature_names = ['Sum_Insured', 'Policies_Revenue', 'Broker_ID', 'Claim_Amount']
    iris.target_names = ['Fraud','NOT Fraud']
    tmp = df['Fraudulent_Claim'].astype(str).replace('*', 0)
    tmp = tmp.astype(str).replace('', 1).astype(int)
    iris.target = tmp.astype(int).values
    # df = df[['Sum_Insured', 'Policies_Revenue', 'Broker_ID', 'Claim_Amount']]
    iris.data = np.dstack( (df['Sum_Insured'].astype(np.float), df['Policies_Revenue'].astype(np.float),
                            df['Broker_ID'].astype(np.int), df['Claim_Amount'].astype(np.float)) )[0]

    return iris


# Set learning params
learning_rate = 0.01
training_iteration = 30
batch_size = 100
display_step = 2


iris = load_data()

test_idx = [0, 1198]
# print("Test")
# print(iris.target[0])
# print(iris.target[1198])

train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

#training
# train_target = np.delete(iris.target, test_idx)
# train_data = np.delete(iris.data, test_idx, axis=0)
#
#
# testing
# test_target = iris.target[test_idx]
# test_data = iris.data[test_idx]


clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print("Training set: " + str(len(train_target)))
print("Testing set: " + str(len(test_target)))
# print(clf.predict(test_data))
pred = clf.predict(test_data)

score = metrics.accuracy_score(test_target, pred)
print("Accuracy: " + str(score*100.0))


#viz code
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,
                     filled=True, rounded=True, impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("insurance.pdf")

