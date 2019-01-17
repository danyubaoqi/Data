import csv
a=open("data.csv","r",encoding="utf-8")
data=csv.reader(a)
dd={"基本信息":"","标签":"","关注":"","职业":""}
b=open("data2.csv","w",encoding="utf-8")
b.write("基本信息,标签,关注,职业\n")
for i in data:
    if i[1]=="基本信息":
        pp=[dd[j] for j in dd]
        print(pp)
        b.write(",".join(pp))
        b.write("\n")
        dd = {"基本信息": "", "标签": "", "关注": "", "职业": ""}
    dd[i[1]]=i[3]