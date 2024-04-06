hour, min = input().split()    
hour = int(hour)    
min = int(min) 

time = input()
time = int(time) 

hour += time//60
min += time%60

if min>=60:
    hour+=1
    min-=60

if hour>=24:
    hour -=24

print(hour,min)