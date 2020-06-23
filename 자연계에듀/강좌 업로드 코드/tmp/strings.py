fp = open("fields.txt", "r")

lines = fp.read().split()
fp.close()

fp = open("mem2.txt", "w")
for line in lines:
    field1 = line[2]+line[3:-1].lower()
    field2 = line[2:-1].lower()
    #string = "private String %s;\n"%(field)
    string = "public String get%s() { return %s;}\n"%(field1, field2)
    fp.write(string)
    string = "public void set%s(String %s) {this.%s = %s;}\n"%(field1, field2, field2, field2)
    fp.write(string)

fp.close()