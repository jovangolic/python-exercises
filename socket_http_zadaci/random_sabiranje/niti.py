#Kreirati program koji pokrece pet niti. Svaka nit bira slucajan broj od 1 do 10. Nakon sto sve niti zavrse sabiraju se
#sve generisane vrednosti

import threading,random
'''class MyThread(threading.Thread):
    def __init__(self,idn):
        super().__init__()
        self.idn = idn
    def run(self):
        print("thread is running")
niti,total = [],0
for i in range(5):
    niti.append(MyThread(random.randint(1,10)))
    niti[i].start()
    total += niti[i].idn
    niti[i].join()
print("zbir vrednosti je: ",total)'''

#drugi nacin
'''locker = threading.Lock()
class MyThread(threading.Thread):
    def __init__(self,idn):
        super().__init__()
        self.idn = idn
    def run(self):
        total = 0
        locker.acquire()
        for i in range(5):
            total+=i
        print("thread is running")
        locker.release()
niti,total = [],0
for i in range(5):
    niti.append(MyThread(random.randint(1,10)))
    niti[i].start()
    total += niti[i].idn
    niti[i].join()
print("zbir vrednosti je: ",total) '''
