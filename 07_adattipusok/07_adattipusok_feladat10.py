# https://sulipy.hu/adattipusok/halmaz?tab=feladatok

x = [i for i in range(11)]
y1 = set(i*2 + 3 for i in x)
y2 = set(i*3 + 1 for i in x)

print(y1)
print(y2)

# Metszet:
print(y1 & y2)
# Unio:
print(y1 | y2)
# Kulonbseg:
print(y1-y2)
print(y2-y1)

