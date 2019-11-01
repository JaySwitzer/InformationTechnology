import matplotlib.pyplot as plt

xlist = [3, 16, 69, 97, 53, 22, 74, 41, 55, 36]
ylist = ["Joe", "Sam", "Alexa", "Hank", "Gavin", "Keith", "Ashton", "Lynn", "Beth", "Yuri"]

plt.xlabel("This is X")
plt.ylabel("This is Y")

plt.title("This is my plot")

plt.pie(xlist)

plt.show()
