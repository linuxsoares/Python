from time import time, localtime, sleep

h, m, s = localtime(time())[3:6]

hora = h,m,s 

while hora != '(21, 47, 0)':
    h, m, s = localtime(time())[3:6]
    hora = h,m,s 
    if hora == '(21, 47, 0)':
        sleep(1)
        print 'Hora de ir embora do trabalho UHUUUUU'
    else:
        sleep(1)
        print hora,' Trabalha Gilmar Trabalha'
