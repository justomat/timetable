
def download():
url = "http://webspace.apiit.edu.my/"\
    "intake-timetable/download_timetable/" + \
    file_name

u = urllib2.urlopen(url)
f = open(file_name, 'wb')

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