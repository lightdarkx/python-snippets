def uglyNum(n):

    ugly = [1]
    i2 = i3 = i5 = 0

    nextMultipleof2 = 2
    nextMultipleof3 = 3
    nextMultipleof5 = 5
    
    for i in range(1,n):

        nextUglyNumber = min(nextMultipleof2, nextMultipleof3, nextMultipleof5)
        #print(f"{nextUglyNumber}")
        ugly.append(nextUglyNumber)
        #ugly[i] = nextUglyNumber

        if (ugly[i] == nextMultipleof2):
            i2 += 1
            nextMultipleof2 = ugly[i2]*2
        if (ugly[i] == nextMultipleof3):
            i3 += 1
            nextMultipleof3 = ugly[i3]*3
        if (ugly[i] == nextMultipleof5):
            i5 += 1
            nextMultipleof5 = ugly[i5]*5
    #print(ugly)
    return ugly[-1]


def main():

    print("Enter the value of n")
    n = int(input())
    #n = 150

    #ans[] = uglyNum(n)

    print(f"{uglyNum(n)}")

if __name__ == "__main__":
        pass

main()        

#print(f"{uglyNum(7)}")
