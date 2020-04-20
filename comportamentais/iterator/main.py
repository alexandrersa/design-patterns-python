class RadioStation:
    def __init__(self, frequency):
        self.__frequency = frequency

    @property
    def frequency(self):
        return self.__frequency


class StationList:
    def __init__(self):
        self.__stations = list()
        self.__counter = 0

    def add(self, radio_station):
        self.__stations.append(radio_station)

    def remove(self, frequency):
        for index in range(0, len(self.__stations)):
            if self.__stations[index].frequency == frequency:
                self.__stations.pop(index)
                break
        else:
            print("Radio station not found")

    def count(self):
        return len(self.__stations)

    def current(self):
        return self.__stations[self.__counter].frequency

    def key(self):
        return self.__counter

    def __next__(self):
        self.__counter += 1

    def rewind(self):
        self.__counter = 0


if __name__ == "__main__":

    station_list = StationList()
    station_list.add(RadioStation(89))
    station_list.add(RadioStation(101))
    station_list.add(RadioStation(102))
    station_list.add(RadioStation(103.2))

    print(f"Stations: {station_list.count()}")
    station_list.remove(89)
    print(f"Stations: {station_list.count()}")

    print(f"Current Station: {station_list.current()}")
    next(station_list)
    print(f"Current Station: {station_list.current()}")
