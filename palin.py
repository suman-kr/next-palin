def findNextPalindrome(n):
    try:
        n = [i for i in str(n)]
        l = len(n) - 1
        a = set(n)
        if len(a) == 1 and '9' in a:
            return "Your number: {}".format('1{}1'.format('0'*l))
        else:
            if len(n) % 2 == 0:
                center = len(n) // 2 
                left = n[:center]
                new = left+left[::-1]
                # print(new)
                if int(''.join(new)) <= int(''.join(n)):
                    for i in range(center-1,-1,-1):
                        if new[i] != '9':
                            new[i] = str(int(new[i]) + 1)
                            new[i+1] = str(int(new[i+1]) + 1)
                            break
                        else:
                            new[i] = str((int(new[i]) + 1 )%10)
                            new[i-1] = str((int(new[i-1]) + 1)% 10)
                            new = new[:center]
                            new += new[::-1]
                            break

                return "Your number: {}".format(''.join(new))
            else:
                center = len(n) // 2
                left = n[:center]
                new = left + list(n[center]) + left[::-1]
                if int(''.join(new)) <= int(''.join(n)):
                    for i in range(center , -1 , -1):
                        if n[i] != '9':
                            n[i] = str(int(n[i])+1)
                            left = n[:center]
                            new = left + list(n[i]) + left[::-1]
                            break
                        else:
                            n[i] = str((int(n[i]) + 1 ) % 10)
                            n[i-1] = str((int(n[i-1]) + 1 ) % 10)
                            left = n[:center]
                            new = left + list(n[i]) + left[::-1]
                            break

                return "Your number: {}".format(''.join(new))
    except:
        return "Not a Number! :("