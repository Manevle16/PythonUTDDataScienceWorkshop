import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sal = pd.read_csv("C:/Users/Manev/github/Manevle16/PythonUTDDataScienceWorkshop/October27/Salaries.csv")
print(sal.head())
print(sal.columns)
print("# of entries:", len(sal.index))
print("Average BasePay: ", round(sal["BasePay"].mean(), 2))
print("Highest amount of overtime pay:", sal["OvertimePay"].max())
print("JOSEPH DRISCOLL amount paid w/ benefits:", sal[(sal["EmployeeName"] == "JOSEPH DRISCOLL")].iloc[0]["TotalPayBenefits"])
print("Highest paid person: ", sal[(sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max())].iloc[0]["EmployeeName"])
print("Lowest paid person: ", sal[(sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min())].iloc[0]["EmployeeName"])
print("Average pay between 2011 - 2014:", round(sal[(sal["Year"] > 2011) & (sal["Year"] < 2014)]["BasePay"].mean(),2))
print("Number of unique title names:", len(sal["JobTitle"].unique()))
print("Top 5 most common job titles: ", end="")
print(*sal["JobTitle"].value_counts().index[0:5], sep=", ")
jobCounts = sal["JobTitle"].value_counts(ascending=True)
amount = 0
for count in jobCounts:
    if(count != 1):
        break
    amount += 1
print("Job titles with only 1 person in 2013:", amount)
print("Number of job titles with chief:", sal["JobTitle"].str.contains("Chief").value_counts()[True])
jobTitleLengths = sal["JobTitle"].apply(len)
plt.plot(jobTitleLengths, sal["BasePay"])
plt.xlabel("Job Title Name Length")
plt.ylabel("Salary")
plt.show()
