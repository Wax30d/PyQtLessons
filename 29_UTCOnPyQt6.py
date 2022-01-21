"""
Our planet is a sphere; it revolves round its axis.
The Earth rotates towards the east, so the Sun rises at different times in different locations.
The Earth rotates once in about 24 hours.
Therefore, the world was divided into 24 time zones.
In each time zone, there is a different local time.
This local time is often further modified by the daylight saving.
There is a pragmatic need for one global time.
One global time helps to avoid confusion about time zones and daylight saving time.
The UTC (Universal Coordinated time) was chosen to be the primary time standard.
UTC is used in aviation, weather forecasts, flight plans, air traffic control clearances, and maps.
Unlike local time, UTC does not change with a change of seasons.
"""

from PyQt6.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print('Local datetime: ', now.toString(Qt.DateFormat.ISODate))
print('Universal datetime: ', now.toUTC().toString(Qt.DateFormat.ISODate))

print(f'The offset from UTC is: {now.offsetFromUtc()} seconds')
