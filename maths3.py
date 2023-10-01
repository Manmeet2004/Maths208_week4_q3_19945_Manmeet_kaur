import datetime
import matplotlib.pyplot as plt

# Data for causes of death and their respective numbers
causes_of_death = [
    'Alz', 'CRD', 'Diab', 'Heart', 'Flu', 'MalNeop', 'Acc',
          'Neph', 'Septice', 'Stroke']

deaths = [
    63.2,56.0, 13.7, 12.5, 12.2, 7.2, 7.2, 5.6, 4.5, 3.4 ]


# Sort the causes and deaths in descending order
sorted_indices = sorted(range(len(deaths)), key=lambda k: deaths[k], reverse=True)
sorted_causes = [causes_of_death[i] for i in sorted_indices]
sorted_deaths = [deaths[i] for i in sorted_indices]

# Calculate cumulative percentages
total_deaths = sum(sorted_deaths)
cumulative_percentages = [sum(sorted_deaths[:i+1]) / total_deaths * 100 for i in range(len(sorted_deaths))]

# Create the Pareto chart
fig, ax1 = plt.subplots()

ax1.bar(sorted_causes, sorted_deaths, color='y', alpha=0.7)
ax1.set_xlabel('Causes of Death')
ax1.set_ylabel('Number of Deaths (x 10,000)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(sorted_causes, cumulative_percentages, color='r', marker='o')
ax2.set_ylabel('Cumulative Percentage', color='r')
ax2.tick_params('y', colors='r')

plt.title('Pareto Chart of Causes of Death in 2006')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")