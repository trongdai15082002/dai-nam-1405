import matplotlib.pyplot as plt
import numpy as np
divisions [ "Div-A", "Div-6", "Div-c", "Div-D", "Div-E"]
boys_average_marks = [68, 67, 77, 61, 70]
girls_average_marks = [72, 97, 69, 69, 66]

index = np. arange(5)
width = 0.30
plt. bar(index, boys_average_marks, width, color="blue", label="Boys Marks")
plt. bar(index, girls_average_marks, width, color="red", label="Girls Marks, bottom=boys_average_marks")

pit.title("vertically Stacked Bar Graphs")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.xticks (index, divisions)
plt.legend("best")
plt.show()