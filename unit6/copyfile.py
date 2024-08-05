with open("data.txt", "r") as infile, open("example.txt", "a") as outfile:
 content = infile.read()
 outfile.write(content)