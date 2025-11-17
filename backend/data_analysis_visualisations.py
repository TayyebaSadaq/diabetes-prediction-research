import pandas as pd
import matplotlib.pyplot as plt

# ~ Loading the preprocessed data
data = pd.read_csv('data\\preprocessed_data.pkl')

# ~ Checking for outliers - with boxplots (for numerical features ONLY)
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Boxplots for features", fontsize=16) # header for the boxplot
i = 0 # counter for the subplot position
for col in ['BMI', 'Age', 'PhysHlth', 'MentHlth']:
    axs.boxplot(y=data[col], ax=axs[i//2, i%2])
    axs[i//2, i%2].set_title(f'Boxplot of {col}')
    i += 1