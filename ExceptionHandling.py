with open("testExceptionHandling.txt", "w") as f:
    f.write("write the content for exception testing")

try:
    with open("test.txt", "r") as f:
        content = f.read()
        print("content ====>", content)

except FileNotFoundError as e:
    print(e)
