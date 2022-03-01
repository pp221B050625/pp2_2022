import json

x = open('json.txt', 'r')
text = x.read()
a = json.loads(text)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for i in range(3):
    b = a["imdata"][i]["l1PhysIf"]["attributes"]["dn"]
    c = a["imdata"][i]["l1PhysIf"]["attributes"]["descr"]
    d = a["imdata"][i]["l1PhysIf"]["attributes"]["speed"]
    e = a["imdata"][i]["l1PhysIf"]["attributes"]["mtu"]
    print(b, "         ", c, "                 ", d, " ", e)
