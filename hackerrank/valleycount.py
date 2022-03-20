def valley_count(step):
    valley=0
    current=0
    for i in step:
        previous=current
        if i=='U':
            current+=1
        if i=='D':
            current-=1
        if current==0 and i!=0:
            if previous==-1:
                valley+=1
    print(valley)

valley_count('UDDDUDUU')