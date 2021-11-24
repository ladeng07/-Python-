def tri(num):
        if num == 1:
                print([1])
                return [1]
        else:
                l = tri(num -1)
                if num - 2 == 0:
                        print([1,1])
                        return [1,1]
                else:
                        lst = [1]
                        count = 1
                        while num - 1 > count:
                                lst.append(l[count - 1] + l[count])
                                count += 1
                        lst.append(1)
                        print(lst)
                        return lst
tri(10)
