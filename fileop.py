str = "hello, the author is omkar"
fo = open("foo.txt", "wb+")

print "Name of file: ", fo.name


print "Closed or not: ", fo.closed
print "Opening Mode: ", fo.mode
print "Softspace flag: ", fo.softspace

fo.write(str)

filereader = fo.read(10);

print "File Insight:::    ", filereader

fo.close()