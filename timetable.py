import csv
import os.path
import urllib2
import zipfile
 
filename = 'timetableCSV.zip'
url = 'http://webspace.apiit.edu.my/intake-timetable/download_timetable/'

def download():
    u = urllib2.urlopen(url+filename)
    f = open(filename, 'wb')

    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading data: %s bytes" % (file_size)

    file_size_dl = 0
    block_sz = 8  # bytes
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        print status,
    f.close()
    print "\nDone!\n"

def parse(row):
    result = {}

    result['intake'] = row[1]
    
    nod, date = row[2].split()
    d, m, y = date.split('-')

    result['date'] = {
        'nod': nod,
        'd': d,
        'm': m,
        'y': y
    }

    start, end = row[3].split('-')

    result['time'] = {
        'start': start,
        'end': end
    }

    result['building'] = row[4]
    result['room'] = row[5]
    result['module'] = row[6]
    result['lecturer'] = row[7]

    # print row
    print result


if not os.path.isfile(filename):
    download()
else:
    print "File present, skipping download...\n"

with zipfile.ZipFile("timetableCSV.zip") as zf:
    with zf.open(zf.namelist()[0]) as csvf:
        reader = csv.reader(csvf)
        for row in reader:
            parse(row)

