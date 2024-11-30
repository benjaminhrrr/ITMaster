DAY = 86400
HOUR = 3600
MINUTE = 60

s = int(input('Ingrese un período de tiempo en s: '))

days = s // DAY
hs = (s % DAY) // HOUR
min = (s % HOUR) // MINUTE
s_restantes = s % 60

if DAY < s < (DAY * 2):
    print(f'''
{s} segundos equivalen a:
{days} día, {hs} hs, {min} min y {s_restantes} seg.''')
else:
    print(f'''
{s} segundos equivalen a:
{days} días, {hs} hs, {min} min y {s_restantes} seg.''')
