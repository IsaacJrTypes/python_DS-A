import queue
import time
import random
class Ticket:
    def __init__(self,ticket_num = None,ts= None):
        self.ticket_num = ticket_num
        self.ts = ts
    def __str__(self):
        return "num: " + str(self.ticket_num) +", timestamp: " + str(self.ts)
def createQ(num):
    q = queue.Queue()
    for i in range(num):
        new_ticket = Ticket(i,time.time())
        q.put(new_ticket)
        random_number = random.randrange(num)
        #print(random_number)
        time.sleep(random_number)
        #print(new_ticket)

    return q
def processQ(q):
    while not q.empty():
        ticket = q.get()
        print("Processed ticket, " + ticket.__str__())

def main():
    q = createQ(3)
    processQ(q)



main()