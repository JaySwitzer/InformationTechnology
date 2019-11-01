import matplotlib.pyplot as plt

xlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ylist = ["Joe", "Sam", "Alexa", "Hank", "Gavin", "Keith", "Ashton", "Lynn", "Beth", "Yuri"]

plt.xlabel("This is X")
plt.ylabel("This is Y")

plt.title("This is my plot")

plt.plot(xlist, ylist)

plt.show()
