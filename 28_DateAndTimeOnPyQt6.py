"""
PyQt6 has QDate, QDateTime, QTime classes to work with date and time.
The QDate is a class for working with a calendar date in the Gregorian calendar.
It has methods for determining the date, comparing, or manipulating dates.
The QTime class works with a clock time.
It provides methods for comparing time, determining the time and various other time manipulating methods.
The QDateTime is a class that combines both QDate and QTime objects into one object.
"""
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

datetime = QDateTime.currentDateTime()

print(datetime.toString())

time = QTime.currentTime()
print(time.toString(Qt.DateFormat.ISODate))
