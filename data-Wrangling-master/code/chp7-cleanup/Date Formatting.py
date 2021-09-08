from csv import reader

data_rdr = reader(open('../../data/unicef/mn.csv', 'rb'))
header_rdr = reader(open('../../data/unicef/mn_headers_updated.csv', 'rb'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

print len(header_rows)

all_short_headers = [h[0] for h in header_rows]
skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

del all_short_headers

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
        new_data.append(new_row)


zipped_data = []

for drow in new_data:
    zipped_data.append(zip(header_rows, drow))

# print zipped_data[0]


# for x in zipped_data[0]:
#     print 'Question: {[1]}\nAnswer: {}'.format(x[0], x[1])



from datetime import datetime

start_string = '{}/{}/{} {}:{}'.format(
    zipped_data[0][8][1], zipped_data[0][7][1], zipped_data[0][9][1],
    zipped_data[0][13][1], zipped_data[0][14][1])

#print start_string

start_time = datetime.strptime(start_string, '%m/%d/%Y %H:%M')

#print start_time


from datetime import datetime

end_time = datetime(
    int(zipped_data[0][9][1]), int(zipped_data[0][8][1]),
    int(zipped_data[0][7][1]), int(zipped_data[0][15][1]),
    int(zipped_data[0][16][1]))


print ('Interview start time:', start_time)
print ('Interview start time:', end_time)

