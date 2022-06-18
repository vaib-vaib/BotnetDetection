"""
Written by Vaibhavi Ambarkar
for the cybersecurity engage program 2022

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

#reading the dataset
dataset = pd.read_csv('capture20110810.binetflow.2format')

#Getting the bot net data
dataset = dataset[dataset['Label'].str.contains('Botnet')] 

#printing the size of data
print('Rows:',dataset.shape[0], 'Columns:', dataset.shape[1])
dataset.sample(5) #printing the 5 rows
#Rows: 40961 Columns: 33

#returns the number of unique values for each column
dataset['Label'].nunique() #68

# Removed all the columns with missing value > 30%
dataset = dataset.loc[:, dataset.isnull().mean() < 0.3] 

# Changing the datatype of the columns
dataset = dataset.astype({"Proto":'category',"Sport":'category',"Dport":'category',"State":'category','StartTime':'datetime64[s]','LastTime':'datetime64[s]'})

# getting duration from the columns 'LastTime' and 'StartTime'
dataset['duration'] = abs(dataset['LastTime'].dt.second - dataset['StartTime'].dt.second) 

#Dropping the column SrcAddr and DstAddr since they contain unique ip
dataset.drop(columns=['SrcAddr','DstAddr','LastTime','StartTime'],inplace=True) 

categorical_columns = dataset.select_dtypes(exclude=['int64', 'float64']).columns.values      

#Building the model        
dataset = pd.get_dummies(dataset,columns=categorical_columns[:-1],drop_first=True)
X = dataset.loc[:, dataset.columns != 'Label']
y = dataset.loc[:, dataset.columns == 'Label']

#Train-test split
Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2,random_state=1)

#using the decision tree model - Accuracy Score: 99.0 %
descision_tree_model = DecisionTreeClassifier()
descision_tree_model.fit(Xtrain,ytrain)
prediction = descision_tree_model.predict(Xtest)
print('Decision Accuracy Score:',round(accuracy_score(ytest,prediction)*100),'%')

#using rhe naive bayes model - Accuracy Score: 94.0 %
multinomial_naive_bayes = GaussianNB()
multinomial_naive_bayes.fit(Xtrain,ytrain)
prediction_naive = multinomial_naive_bayes.predict(Xtest)
print('Naive Bayes Accuracy Score:',round(accuracy_score(ytest,prediction_naive)*100),'%')