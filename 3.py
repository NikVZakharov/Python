for i in range(4):
    max=0
    if a>max_of_four:
        max_of_four=a
    if b>max_of_four:
        max_of_four=b   
    if c>max_of_four:
        max_of_four=c 
    if d>max_of_four:
        max_of_four=d
#your_code
a, b, c, d = list(map(int, input().split()))
print(max_of_four(a, b, c, d))