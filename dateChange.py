from datetime import *

with open('inicio.txt','r') as f:
    startDate = f.read()

with open('final.txt','r') as f:
    endDate = f.read()

startDate = startDate.strip()
endDate = endDate.strip()

startDate = datetime.strptime(startDate, '%Y-%m-%d')
endDate = datetime.strptime(endDate, '%Y-%m-%d')

startDate = startDate + timedelta(days=1)
endDate = endDate + timedelta(days=1)

with open('inicio.txt','w+') as f:
    f.write(str(startDate).split(' ')[0])

with open('final.txt','w+') as f:
    f.write(str(endDate).split(' ')[0])
