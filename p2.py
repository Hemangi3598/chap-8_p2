# wapp to learn dictionary
#declare
d1 = {}
d2 = {"idli":50, "dosa":75, "wada":60}
print(d2)

#add / change
d2["upma"] = 40;		print(d2)
d2[' idli'] = 65;		print(d2)
d2.update({'momo':100});	print(d2)
d2.update({"s/w":20, "ts/w":30});print(d2)

#remove
d2.pop("wada");			print(d2)
#d2.pop("wada");		print(d2)
d2.popitem();			print(d2)
d2.clear();			print(d2)

d2 = {"idli":50, "dosa":75, "wada":60}
#access
print(d2["idli"])
# print(d2["momo"])
print(d2.get("idli"))
print(d2.get("momo"))





