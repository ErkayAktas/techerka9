import random
import time 
abc=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n','o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü','v', 'y', 'z', 'x', 'w', 'q']
r=input("give a input: \t")
let=""
for i in r:
    if i==" ":
        let+=i
        continue
    random.shuffle(abc)
    for j in abc:
        time.sleep(0.1)
        print(let+j)
        if j==i:
            let+=i
            break