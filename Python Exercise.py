file = open("results.txt", "w")
file.write("The prime numbers between " + "1 " + "and " + "250 " + "are:" + "\n")

for num in range(1,251):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            file.write(str(num) + "\n")

print("The prime numbers are stored in the /home/ec2-user/results.txt file.")
file.close()
