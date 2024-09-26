class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        if not any(map(lambda k: start<k[1] and end>k[0],self.bookings)):
            self.bookings.append([start,end])
            return True
        return False
    
my_obj = MyCalendar()
print(my_obj.book(10,20))
print(my_obj.book(15,25))
print(my_obj.book(20,30))