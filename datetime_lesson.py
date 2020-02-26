from datetime import timedelta, datetime
import locale
locale.setlocale(locale.LC_ALL, 'english')

dt_now = datetime.now()
delta_days = timedelta(days=1)
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print("Yesterday was "
      + str(datetime.strftime(dt_now - delta_days, '%A %d %B %Y'))
      + ".")
print('Today is '
      + str(datetime.strftime(dt_now, '%A %d %B %Y'))
      + '.')
print("Month ago was "
      + str(datetime.strftime(dt_now
                              - (delta_days * 31), '%A %d %B %Y'))
                              + ".")
print(date_dt)
