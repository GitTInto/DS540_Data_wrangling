import os
os.chdir('../../data/chp5/')

pdf_txt = 'en-final-table9.txt'
openfile = open(pdf_txt, 'r')

# for line in openfile:
#     print line


# country_line = False
# for line in openfile:
#
#     if country_line:
#         print line
#
#     if line.startswith('and areas'):
#         country_line = True
#     elif country_line:
#         if line == '\n':
#             country_line = False


# country_line = total_line = False
# for line in openfile:
#
#     if country_line or total_line:
#         print line
#
#     if line.startswith('and areas'):
#         country_line = True
#     elif country_line:
#         if line == '\n':
#             country_line = False
#
#     if line.startswith('total'):
#         total_line = True
#     elif total_line:
#         if line == '\n':
#             total_line = False


double_lined_countries = [
    'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Lao People\xe2\x80\x99s Democratic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]


def turn_on_off(line, status, start, end='\n'):
    """
        This function checks to see if a line starts/ends with a certain
        value. If the line starts/ends with that value, the status is
        set to on/off (True/False).
    """
    if line.startswith(start):
        status = True
    elif status:
        if line == end:
            status = False
    return status


# country_line = total_line = False
#
# for line in openfile:
#     if country_line or total_line:
#         print '%r' % line
#
#     country_line = turn_on_off(line, country_line, 'and areas')
#     total_line = turn_on_off(line, total_line, 'total')


def clean(line):
    """
        Cleans line breaks, spaces, and special characters from our line.
    """
    line = line.strip('\n').strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')

    return line


countries = []
totals = []
country_line = total_line = False
previous_line = ''

for line in openfile:
    if country_line:
        if previous_line in double_lined_countries:
            line = ' '.join([clean(previous_line), clean(line)])
            countries.append(line)
        elif line not in double_lined_countries:
            countries.append(clean(line))

    country_line = turn_on_off(line, country_line, 'and areas')
    total_line = turn_on_off(line, total_line, 'total')

    previous_line = line



import pprint
test_data = dict(zip(countries, totals))
pprint.pprint(test_data)