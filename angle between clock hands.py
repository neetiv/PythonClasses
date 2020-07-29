inp = input("Give a time(format h:m):  ")
lst = inp.split(':')

h = int(lst[0])
m = int(lst[1])

if h == 12:
    h = 0
if m == 60:
    m = 0
if h<= 24 and h > 12:
    h = h-12

m_angle = 6*m
h_angle = 0.5*(h*60+m)

angle = abs(h_angle-m_angle)
angle = min(360 - angle, angle)

print(angle)
