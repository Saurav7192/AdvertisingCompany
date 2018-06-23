import Data_Reading as DR
import seaborn as sns
import matplotlib.pyplot as plt


#Displot
Age = DR.data.Age
sns.distplot(Age,bins=50);
plt.show()

#Relation between attributes
sns.jointplot("Age", "Area Income", data=DR.data)
plt.show()

#
sns.jointplot("Age", "Daily Time Spent on Site", data=DR.data,kind= "kde")
plt.show()

#
sns.jointplot("Daily Internet Usage", "Daily Time Spent on Site", data=DR.data)
plt.show()

#Relationship b/w all attribute
sns.pairplot(DR.data)
plt.show()



