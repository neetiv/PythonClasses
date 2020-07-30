inp = input("Give a time (format hour:minute:seconds):  ")
lst = inp.split(':')

h = int(lst[0])
m = int(lst[1])
s = int(lst[2])

if h == 12:
    h = 0
if m == 60:
    m = 0
if s == 60:
    s = 0
if h<= 24 and h > 12:
    h = h-12

s_angle = 6*s
m_angle = (6*m)+(s/10)
h_angle = (h*30)+(m/2)+(s/120)

angle1 = abs(h_angle-m_angle)
angle1 = min(360 - angle1, angle1)

angle2 = abs(m_angle-s_angle)
angle2 = min(360-angle2, angle2)

angle3 = abs(h_angle-s_angle)
angle3 = min(360-angle3, angle3)

print("Angle between Minute and Hour Hand:", angle1)
print("Angle between Second and Minute Hand:", angle2)
print("Angle between Second and Hour Hand:", angle3)
