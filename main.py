import re
import statistics
from collections import Counter

#open the HTML file in read mode
with open("index.html", "r") as file:
    #read the contents into a string
    html_content = file.read()

#extracting all the colours from the HTML file
colour_extraction = r"<td>(?:MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY)</td>\s*<td>(.*?)</td>"
colours = re.findall(colour_extraction, html_content, re.DOTALL)

#to make a list for the extracted colours
colour_list = []
for row in colours:
    colour_list.extend([x.strip().title() for x in row.split(",")])

#frequency of the colours and a dictionary of the colours
colours_count = Counter(colour_list)
colour_dict = dict(colours_count)

#mean, median, most worn and variance of the colours
mean_value = statistics.mean(colour_dict.values())
mean_colour = min(colour_dict, key=lambda x: abs(colour_dict[x] - mean_value))

meadian_value = statistics.median(colour_dict.values())
median_colour = min(colour_dict, key=lambda k: abs(colour_dict[k] - meadian_value))

most_worn_colour = max(colour_dict, key=colour_dict.get)
variance_value = statistics.variance(colour_dict.values(), xbar=mean_value) 

print(f"The mean colour is : {mean_colour}")
print(f"The median colour is : {median_colour}")
print(f"The most worn colour is : {most_worn_colour}")
print(f"The variance of colours is : {variance_value}")

#probability of red choosen at random.
total_colours = len(colour_list)
red_occurrences = colour_list.count("Red")
probability_of_red = red_occurrences / total_colours
print(f"The probabilty of choosing red is: {probability_of_red}") 