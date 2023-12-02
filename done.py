import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#loading the file
dt = pd.read_csv("C:\\Users\\OWNER\\Downloads\\exercise.zip")

#descriptive analysis on the data
desc = dt.describe()

#analyzing the salary of workers
x = dt.salary.value_counts()
def salary_chart():
    for keys,value in x.items():
        plt.xlabel('Salary')
        plt.ylabel('Number of workers')
        plt.bar(keys , value)
    plt.show()

#ckecking for trends in the satsfaction of workers
y = dt.satisfaction_level
def satisfaction_chart():
    plt.xlabel('Workers Satisfaction Level')
    plt.ylabel('Number of Workers')
    plt.hist(y, bins = 4, rwidth= 0.9)
    plt.tight_layout()
    plt.show()

#visualization on the department
def department():
    y = dt.Department.value_counts()
    for keys, values in y.items():
        plt.xlabel('Department')
        plt.ylabel('Workers')
        plt.xticks(rotation = 45, ha= 'right')
        plt.bar(keys,values)
        plt.tight_layout()
    plt.show()

#work Accident
def work_accident():
    z = dt.Work_accident.value_counts()
    plt.pie(z, labels=["No", "Yes"])
    plt.show()

#last_evaluation
def last_evaluation():
    w = dt.last_evaluation
    plt.xlabel("last_evaluation")
    plt.ylabel("Number of worker")
    plt.hist(w, bins = 10, rwidth=0.9)
    plt.grid(True)
    plt.show()

#time_spend_company: THIS ONE STRESSED ME A LOT
def time_spend_company():
    v = dt.time_spend_company.value_counts()
    for k, vl in v.items():  
        plt.bar(k, vl)
    plt.show()

#average_monthly_hours
def average_montly_hours():
    w = dt.average_montly_hours
    plt.xlabel("average_montly_hours")
    plt.ylabel("Workers")
    plt.hist(w, bins = 5, rwidth= 0.8)
    plt.grid(True)
    plt.show()

#bivarate analysis
#time spent  and projects 
def tim_spent_project():
    x = dt.number_project
    y = dt.time_spend_company
    t = np.corrcoef(x,y)
    print("the corrrelation between them is:", t)
    plt.xlabel("Number of projects")
    plt.ylabel("years spentt in company")
    plt.scatter(x,y, color= 'r')
    plt.show()

#monthly salary and department
def salary_department():
    x = dt.salary
    y= dt.Department
    cont = pd.crosstab(x,y)
    return cont

#satisfaction and last evaluation
def satisfaction_evaluation():
    x = dt.satisfaction_level
    y = dt.last_evaluation
    corr = np.corrcoef(x,y)
    print(corr)

#accident and promotion
def accident_promotion():
    y = dt.Work_accident
    x = dt.promotion_last_5years
    z = dt.left
    ct = pd.crosstab(y, [x,z])
    cr = np.corrcoef(y,[x,z])
    print(ct)
    print(cr)

#department_left
def dept_left():
    y = dt.Department
    x = dt.left
    z = pd.crosstab(x,y)
    print(z)
    return z

#salary and left
def sal_left():
    x = dt.salary
    y = dt.left
    z = pd.crosstab(x,y)
    print(z)
