import time

class TrafficLight:
    __color = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for led, time_work in self.__color.items():
            print(f'{led} {time_work} сек')
            time.sleep(time_work)

if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()