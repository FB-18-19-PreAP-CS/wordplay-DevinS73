def reversed(a,b):
    check1=str(a)
    check2=str(b)
    if len(str(a))==1:
        check1='0'+str(a)
    if len(str(b))==1:
        check2='0'+str(b)
    if check1==check2[::-1]:
        return True
    return False
def solver():
    mom_age=0
    my_age=0
    count=0
    for i in range(1,100):
        mom_age=i
        for j in range(1,100):
            my_age=j
            if reversed(my_age,mom_age):
                a=0
                count=1
                while len(str(mom_age+a))==2:
                    a+=1
                    if reversed(my_age+a,mom_age+a):
                        count+=1
                        if count==6:
                            age=str(my_age+a)
            if count==8:
                if mom_age-my_age>=18:
                    print(age)
            count=0