while True:
    while True:
        print("welcome to numbering system converter ")
        print("please select a choice")
        print("A) insert a new number")
        print("B) Exit Program")

        choice = input()
        if choice == 'A':
            num = int(input("please insert a number: "))
            break
        elif choice == 'B':
            print("Thank you for using this program")
            exit()
        else:
            print("please select a valid choice")

    while True:
        print("please select the base you want to convert a number from: ")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) hexadecimal")

        choice2 = input()
        if choice2 != 'A' and choice2 != 'B' and choice2 != 'C' and choice2 != 'D':
            print("please select a valid choice")
        else:
            break

    while True:
        print("please select the base you want to convert a number to: ")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) hexadecimal")

        choice3 = input()
        if choice3 != 'A' and choice3 != 'B' and choice3 != 'C' and choice3 != 'D':
            print("please select a valid choice")
        else:
            break


    count=0
    result=''
    result2=0
    result3=''


    if choice2 == choice3:
        print(num)
    elif choice2 == 'A':
        if choice3 == 'B':
            while num != 0:
                sum = num % 2
                result = str(sum) + result
                num = num // 2
            print(result)
        elif choice3 == 'C':
            while num != 0:
                sum = num % 8
                result = str(sum) + result
                num = num // 8
            print(result)
        elif choice3 == 'D':
            while num != 0:
                sum = num % 16
                if sum == 10:
                    result = 'A' + result
                elif sum == 11:
                    result = 'B' + result
                elif sum == 12:
                    result = 'C' + result
                elif sum == 13:
                    result = 'D' + result
                elif sum == 14:
                    result = 'E' + result
                elif sum == 15:
                    result = 'F' + result
                else:
                    result = str(sum) + result
                num = num // 16
            print(result)

    elif choice2 == 'B':
        if choice3 == 'A':
            while num > 0:
                sum = num % 10
                result2 = result2 + sum * pow(2, count)
                count = count + 1
                num = num // 10
            print(result2)
        elif choice3 == 'C':
            while num > 0:
                for i in range(3):
                    result = str(num % 10) + result
                    num = num // 10
                    if num <= 0:
                        break
                num2 = int(result)
                result = ''
                while num2 > 0:
                    sum = num2 % 10
                    result2 = result2 + sum * pow(2, count)
                    count = count + 1
                    num2 = num2 // 10

                result3 = str(result2) + result3
                result2 = 0
                count = 0
            print(result3)
        elif choice3 == 'D':
            while num > 0:
                for i in range(4):
                    result = str(num % 10) + result
                    num = num // 10
                    if num <= 0:
                        break
                print(result)
                num2 = int(result)
                result = ''
                while num2 > 0:
                    sum = num2 % 10
                    result2 = result2 + sum * pow(2, count)
                    count = count + 1
                    num2 = num2 // 10

                if result2 == 10:
                    result3 = 'A' + result3
                elif result2 == 11:
                    result3 = 'B' + result3
                elif result2 == 12:
                    result3 = 'C' + result3
                elif result2 == 13:
                    result3 = 'D' + result3
                elif result2 == 14:
                    result3 = 'E' + result3
                elif result2 == 15:
                    result3 = 'F' + result3
                else:
                    result3 = str(result2) + result3
                result2 = 0
                count = 0
            print(result3)

    elif choice2 == 'C':
        if choice3 == 'A':
            while num > 0:
                sum = num % 10
                result2 = result2 + sum * pow(8, count)
                count = count + 1
                num = num // 10
            print(result2)
        elif choice3 == 'B':
            while num > 0:
                sum = num % 10
                while sum != 0:
                    sum2 = sum % 2
                    result = str(sum2) + result
                    sum = sum // 2

                if len(result) == 2:
                    result3 = '0' + result + result3
                elif len(result) == 1:
                    result3 = '00' + result + result3
                else:
                    result3 = result + result3
                result = ''
                num = num // 10
            print(result3)
        elif choice3 == 'D':
            while num > 0:
                sum = num % 10
                while sum != 0:
                    sum2 = sum % 2
                    result = str(sum2) + result
                    sum = sum // 2

                if len(result) == 2:
                    result3 = '0' + result + result3
                elif len(result) == 1:
                    result3 = '00' + result + result3
                else:
                    result3 = result + result3
                result = ''
                num = num // 10

            num = int(result3)
            result = ''
            while num > 0:
                for i in range(4):
                    result = str(num % 10) + result
                    num = num // 10
                    if num <= 0:
                        break
                num = int(result)

                result = ''
                result2 = 0
                result3 = ''
                while num > 0:
                    for i in range(4):
                        result = str(num % 10) + result
                        num = num // 10
                        if num <= 0:
                            break
                    print(result)
                    num2 = int(result)
                    result = ''
                    while num2 > 0:
                        sum = num2 % 10
                        result2 = result2 + sum * pow(2, count)
                        count = count + 1
                        num2 = num2 // 10

                    if result2 == 10:
                        result3 = 'A' + result3
                    elif result2 == 11:
                        result3 = 'B' + result3
                    elif result2 == 12:
                        result3 = 'C' + result3
                    elif result2 == 13:
                        result3 = 'D' + result3
                    elif result2 == 14:
                        result3 = 'E' + result3
                    elif result2 == 15:
                        result3 = 'F' + result3
                    else:
                        result3 = str(result2) + result3
                    result2 = 0
                    count = 0
                print(result3)