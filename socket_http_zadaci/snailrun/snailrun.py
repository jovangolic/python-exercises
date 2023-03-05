#Potrebno je napraviti program trka puzeva.Svaki puz predstavlja jednu runnable klasu.
#Run metod svake runnable klase sadrzi petlju koja se izvrsava 10 puta i u svakoj iteraciji sadrzi pauzu u
#slucajnom izabranom intervalu od 3 sekunde.Svaki puz ima svoju traku u kojoj se prikazuje do kog je broja trenutno dosao.
#Kada petlja u run metodi dodje do nule, ispisuje se na izlazu da je puz na toj niti dosao do cilja.

import threading,time,random
class Snail(threading.Thread):
    def __init__(self,idn):
        super().__init__()
        self.idn = idn
    def run(self):
        loop = 10
        while loop >= 0:
            loop -= 1
            time.sleep(random.randint(1,5))
            print(f"{loop}".rjust(self.idn))
        print(f"Snail {self.idn} finished")
for i in range(50):
    Snail(i).start()     
