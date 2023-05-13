events = ["coding", "dog", "cat", "movie"]
caffe = 0
while True:
    event = input()
    if event == "END":
        break

    if event.lower() in events:
        if event.islower():
            caffe +=1
        elif event.isupper():
            caffe += 2

if caffe > 5:
    print("You need extra sleep")
else:
    print(caffe)
