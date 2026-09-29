import numpy as np
marks=np.array([90,80,50,40,65,70,85,98,48,54])
mean=np.mean(marks)
median = np.median(marks)
maximum = np.max(marks)
minimum = np.min(marks)
std = np.std(marks)
above_average = marks[marks > mean]
marks_2d = marks.reshape(2, 5)

print (f"Mean: {mean}\nmedian: {median}\n maximum: {maximum}\n minimum: {minimum}\nstd: {std}\nabove_average: {above_average}\n marks_2d: {marks_2d}")