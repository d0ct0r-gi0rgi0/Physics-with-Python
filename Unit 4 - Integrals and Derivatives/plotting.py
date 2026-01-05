def plotting(x, y):
    import matplotlib.pyplot as plt
    plt.plot(x, y, color = 'mediumorchid')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    return