import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips, style="smoker")

plt.show()