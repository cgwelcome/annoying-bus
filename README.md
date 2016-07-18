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
Extracting day 1
Montreal >>> Toronto
Departure          Arrival            Duration      Price
-----------------  -----------------  ----------  -------
07/20/16 00:15:00  07/20/16 06:20:00  6:05          37.00
07/20/16 06:30:00  07/20/16 12:25:00  5:55          42.00
07/20/16 08:00:00  07/20/16 14:30:00  6:30          42.00
07/20/16 09:30:00  07/20/16 15:15:00  5:45          42.00
07/20/16 11:30:00  07/20/16 18:00:00  6:30          42.00
07/20/16 13:30:00  07/20/16 19:15:00  5:45          37.00
07/20/16 15:30:00  07/20/16 21:15:00  5:45          37.00
07/20/16 17:00:00  07/20/16 23:30:00  6:30          32.00
07/20/16 19:00:00  07/21/16 00:45:00  5:45          32.00
07/20/16 21:00:00  07/21/16 03:00:00  6:00          32.00
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
python -m unittest discover
```

### To-Do List
* Sqlite storage
* Support Via Train, Greyhound
* Support more destination

