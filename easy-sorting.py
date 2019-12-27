cookies = [
    ["baklava",10],
    ["cupavci",2],
    ["bananice",8],
    ["Aljonka",9],
    ["kremopita",10],
    ["miska",5]
]

def best(cookies):
  return cookies[1]
cookies.sort(key=best)

print(cookies)
