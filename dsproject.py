import matplotlib.pyplot as plt
import pandas as pd


data = {'Sales': [100, 120, 150, 180], 'Month': ['Jan', 'Feb', 'Mar', 'Apr']}
df = pd.DataFrame(data)


fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns


ax[0].plot(df['Month'], df['Sales'])
ax[0].set_title('Sales by Month')
ax[0].set_xlabel('Month')
ax[0].set_ylabel('Sales')


ax[1].hist(df['Sales'], bins=5)
ax[1].set_title('Sales Distribution')
ax[1].set_xlabel('Sales')
ax[1].set_ylabel('Frequency')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
