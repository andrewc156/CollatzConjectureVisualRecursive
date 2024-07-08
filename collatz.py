import matplotlib.pyplot as plt

def collatz(a,count,x,y):
    if a!= 1:
        y.append(a)
        x.append(count)
        if a % 2 == 0:
            a = a / 2
            count+=1
        else:
            a = a * 3 + 1
            count+=1
        collatz(a,count,x,y)
    else:
        x.append(count)
        y.append(a)
        plt.plot(x, y)
        plt.xlabel('Iteration#')
        plt.ylabel('Value')
        plt.title('Collatz Conjecture')
        plt.show()
        print(f"It took {count} iterations to reach 1")


number = int(input("What number would you like to try? "))
collatz(number,0,[],[])
