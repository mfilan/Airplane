import json
import matplotlib.pyplot as plt
import seaborn as sns
Labels = 'Random BackToFront          FrontToBack           BackToFrontGroups        FrontToBackGroups        WindowMiddleAisle      SteffenPerfect      SteffenModified'
labels = []
for i in Labels.split():
    labels.append(i)
with open("STATS.txt") as json_file1:
    STATS = json.load(json_file1)
for k in range(8):
    m = [i[k] for i in STATS]
    sns.distplot(m, hist = False, kde = True,kde_kws = {'linewidth': 3},label= labels[k])
plt.legend(prop={'size': 16}, title = 'Airline')
plt.title('Density Plot with Multiple Strategies')
plt.xlabel('TIME')
plt.ylabel('PERCENTAGE OF OCCURENCE')
plt.show()


