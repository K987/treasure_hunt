import matplotlib.pyplot as plt


plt.ion()
for i in range(1,10):
    y = i
    plt.plot(y)
    plt.title('num')
    plt.draw()
    plt.pause(1)
    plt.clf()