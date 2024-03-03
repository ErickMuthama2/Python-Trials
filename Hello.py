print('Enter 1 for circle')
print('Enter 2 for rectangle')
print('Enter 3 for triangl')
ch=int(input('Enter your choice:'))      
#elif
if ch==1:
    r=int(input('Enter your radius in cm:'))
    ar=3.14*r**2
    print(f'your area is {ar} cm squared')
elif ch==2:
    l=int(input('Enter your lenght in cm:'))
    w=int(input('Enter your width in cm:'))
    ar=l*w
    print(f'your area is {ar} cm squared')
elif ch==3:
    b=int(input('Enter your base in cm:'))
    h=int(input('Enter your height in cm:'))
    ar=0.5*b*h
    print(f'your are is {ar} cm squared')




