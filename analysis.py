import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided in the business case
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'Score': [4.72, 2.82, 8.04, 3.26]
}
industry_target = 4.5
df = pd.DataFrame(data)

# Calculate the average score
average_score = df['Score'].mean()
print(f"Calculated Average Score: {average_score:.2f}")

# Set plot style
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Create the line plot for quarterly scores
plt.plot(df['Quarter'], df['Score'], marker='o', linestyle='-', color='b', label='Quarterly Score')

# Add the average line
plt.axhline(y=average_score, color='green', linestyle='--', label=f'Average Score ({average_score:.2f})')

# Add the industry target line
plt.axhline(y=industry_target, color='red', linestyle=':', label=f'Industry Target ({industry_target})')

# Add titles and labels for clarity
plt.title('2024 Quarterly Patient Satisfaction Scores', fontsize=16)
plt.ylabel('Satisfaction Score (1-10)', fontsize=12)
plt.xlabel('Quarter', fontsize=12)
plt.ylim(0, 10)  # Set y-axis from 0 to 10 for better context
plt.legend()
plt.grid(True)

# Add data labels to each point on the line plot
for i, txt in enumerate(df['Score']):
    plt.annotate(txt, (df['Quarter'][i], df['Score'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Save the visualization to a file
output_filename = 'patient_satisfaction_chart.png'
plt.savefig(output_filename)

print(f"Chart saved as '{output_filename}'")
