fp = open("20200615.txt", "w")


cid = "920"
teacher = "phy"
subject = "science"

for i in range(1,6):
    line = "%s_%02d\n"%(cid, i)
    line1 = "/%s/%s/20/%s/%02d.mp4\n"%(subject, teacher, cid, i)
    line2 = "/%s/%s/20/%s/%02d_m.mp4\n\n"%(subject, teacher, cid, i)
    fp.write(line)
    fp.write(line1)
    fp.write(line2)

cid = "921"
for i in range(1,6):
    line = "%s_%02d\n"%(cid, i)
    line1 = "/%s/%s/20/%s/%02d.mp4\n"%(subject, teacher, cid, i)
    line2 = "/%s/%s/20/%s/%02d_m.mp4\n\n"%(subject, teacher, cid, i)
    fp.write(line)
    fp.write(line1)
    fp.write(line2)

cid = "922"
for i in range(1,6):
    line = "%s_%02d\n"%(cid, i)
    line1 = "/%s/%s/20/%s/%02d.mp4\n"%(subject, teacher, cid, i)
    line2 = "/%s/%s/20/%s/%02d_m.mp4\n\n"%(subject, teacher, cid, i)
    fp.write(line)
    fp.write(line1)
    fp.write(line2)

fp.close()