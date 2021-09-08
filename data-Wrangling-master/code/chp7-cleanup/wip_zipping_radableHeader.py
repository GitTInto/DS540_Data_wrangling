from csv import reader

data_rdr = reader(open('../../data//unicef/mn.csv', 'rb'))
header_rdr = reader(open('../../data//unicef/mn_headers.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]

# Checking if the length mismatches, if there is a mismatch, meaning either files have extra headers , less headers or missmatches.
# print len(data_rows[0])
# print len(header_rows)


# Remove extra headers from the header list
# bad_rows = []
#
# for h in header_rows:
#     if h[0] not in data_rows[0]:
#         bad_rows.append(h)
#
# for h in bad_rows:
#     header_rows.remove(h)
#
# print len(header_rows)



# Find extra headers in data list

all_short_headers = [h[0] for h in header_rows]

for header in data_rows[0]:
    if header not in all_short_headers:
        print 'mismatch!', header