import time


class Clock:
    def __init__(self, hour, minute, second, clock_type=0):  # compiles the clock
        self.hour = hour
        self.minute = minute
        self.seconds = second
        self.type = clock_type

    def __str__(self):
        if self.type == 0:  # used to print the 24 hour clock
            clock_24 = '{:02}:{:02}:{:02}'.format(self.hour, self.minute, self.seconds)
            return clock_24
        elif self.hour >= 13:  # used to print the pm hours of the 12 hour clock
            clock_12_pm = '{:02}:{:02}:{:02} pm'.format(self.hour % 12, self.minute, self.seconds)
            return clock_12_pm
        else:  # used to print the am hours of the 12 hour clock
            clock_12_am = '{:02}:{:02}:{:02} am'.format(self.hour % 12, self.minute, self.seconds)
            return clock_12_am

    def tick(self):  # used to increment the seconds by one when called
        self.seconds += 1
        if self.seconds == 60:  # resets the seconds at 60 and increments the minutes one
            self.seconds = 0
            self.minute += 1
            if self.minute == 60:  # resets the minutes at 60 and increments the hours one
                self.hour += 1
                self.minute = 0
                if self.hour == 24:  # resets the hours after it hits 24
                    self.hour = 0


if __name__ == '__main__':
    while True:
        hours = int(input('Enter the current hour '))
        minutes = int(input('Enter the current minutes '))
        seconds = int(input('Enter the current seconds '))
        clock_type = input('type 1 for 12 hour clock hit enter for 24 hour ')
        clock = Clock(hours, minutes, seconds, clock_type)  # calls the Clock class
        while True:  # prints the time and increments the time every second
            print(clock)
            clock.tick()
            time.sleep(1)
