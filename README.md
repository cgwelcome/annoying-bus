# AnnoyingBus

AnnoyingBus is a MegaBus schedule extractor written in Python. The software extracts Megabus schedules within the range of date selected by the user, and they are displayed in a table format. The schedules comprise of the departure time, arrival time, duration, price. 

At this stage of development, AnnoyingBus features only trips from Toronto to Montreal, or Montreal to Toronto, and it is not yet available on the pip package management. Feel free to contribute to this project.

### Installation
Setup a virtual environment
```sh
$ mkdir annoyingbus
$ cd annoyingbus
$ virtualenv venv
$ source venv/bin/activate
```
Install the dependencies
```sh
$ pip install -r requirement.txt
```

### Quick Demonstration
By default, the software extracts the current date schedule from Toronto to Montreal
```python
>>> from annoyingbus import AnnoyingBus
>>> bus = AnnoyingBus()
>>> content = bus.search()
>>> content.show_all()
```
```
Megabus - Extracting day 1
ViaRail - Extracting day 1
Company    Origin    Destination    Date        Departure    Arrival    Duration      Price
---------  --------  -------------  ----------  -----------  ---------  ----------  -------
Megabus    Toronto   Montreal       2016-11-01  00:30        06:40      06:10            24
Megabus    Toronto   Montreal       2016-11-01  06:30        12:15      05:45            10
ViaRail    Toronto   Montreal       2016-11-01  06:40        11:57      05:17            61
ViaRail    Toronto   Montreal       2016-11-01  06:40        15:47      09:07            44
Megabus    Toronto   Montreal       2016-11-01  08:00        14:30      06:30            24
ViaRail    Toronto   Montreal       2016-11-01  09:20        14:20      05:00            80
ViaRail    Toronto   Montreal       2016-11-01  09:20        17:57      08:37            61
Megabus    Toronto   Montreal       2016-11-01  10:00        16:20      06:20            10
ViaRail    Toronto   Montreal       2016-11-01  10:45        17:57      07:12            44
ViaRail    Toronto   Montreal       2016-11-01  10:45        20:28      09:43            44
ViaRail    Toronto   Montreal       2016-11-01  11:30        16:47      05:17            80
Megabus    Toronto   Montreal       2016-11-01  12:00        17:45      05:45            24
ViaRail    Toronto   Montreal       2016-11-01  12:20        20:28      08:08            44
Megabus    Toronto   Montreal       2016-11-01  14:00        20:30      06:30            24
ViaRail    Toronto   Montreal       2016-11-01  15:15        20:09      04:54            80
Megabus    Toronto   Montreal       2016-11-01  16:00        21:45      05:45            24
ViaRail    Toronto   Montreal       2016-11-01  17:00        21:49      04:49            44
Megabus    Toronto   Montreal       2016-11-01  17:30        23:15      05:45            10
ViaRail    Toronto   Montreal       2016-11-01  18:00        22:55      04:55            44
Megabus    Toronto   Montreal       2016-11-01  19:00        00:45      05:45            10
Megabus    Toronto   Montreal       2016-11-01  21:00        03:10      06:10            10
```

### Configuration
Search for schedules within 10 days of the current date
```python
>>> bus.days = 10
>>> content = bus.search()
>>> content.show_all()
    ...
```

Search for the July 20, 2016 schedule
```python
>>> from datetime import date
>>> bus.date = date(2016, 7, 20)
>>> content = bus.search()
>>> content.show_all()
    ...
```

Search for schedules within 10 days of July 20, 2016
```python
>>> from datetime import date
>>> bus.date = date(2016, 7, 20)
>>> bus.days = 10
>>> content = bus.search()
>>> content.show_all()
    ...
```
Rerverse the trip, e.g. Montreal to Toronto
```python
>>> bus.reverse_trip()
>>> content = bus.search()
>>> content.show_all()
    ...
```

### Tests
Run all tests
```sh
python -m unittest discover tests
```

### To-Do List
* Support Greyhound

