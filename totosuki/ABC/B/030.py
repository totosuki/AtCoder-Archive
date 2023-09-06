h, m = map(int, input().split())
h %= 12
h_angle = (30 * h) + (30 * (m / 60))
m_angle = 6 * m
print(min([abs(h_angle - m_angle), 360 - abs(h_angle - m_angle)]))
# if abs(h_angle - m_angle) == 180:
#   print(180)
# elif h_angle == m_angle:
#   print(0)
# else:
#   print(min([abs(h_angle - m_angle), 360 - abs(h_angle - m_angle)]))