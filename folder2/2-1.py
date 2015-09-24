months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

days = ['st', 'nd', 'rd'] + 17 * ['th'] \
     + ['st', 'nd', 'rd'] + 7 * ['th'] \
     + ['st']

year = raw_input('Year: ')
month = raw_input('Month: ')
day = raw_input('Day: ')

month_number = int(month)
day_number = int(day)

print months[month_number - 1] + ' ' + day + days[day_number - 1] + '. ' + year
