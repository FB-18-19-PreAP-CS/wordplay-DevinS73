def solver():
    count=100000
    c=0
    while True:
        count+=1
        a=str(count)[2:]
        if a==a[::-1]:
            count2=count+1
            a=str(count2)[1:]
            if a==a[::-1]:
                count2+=1
                a=str(count2)[1:5]
                if a==a[::-1]:
                    count2+=1
                    a=str(count2)
                    if a==a[::-1]:
                        print(count)
                        c+=1
        if c==2:
            return True
if __name__=='__main__':
    solver()