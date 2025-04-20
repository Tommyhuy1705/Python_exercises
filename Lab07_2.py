# Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến 100 sau đó tạo 1 menu cho phép thực hiện các công việc sau:
# In ra danh sách vừa tạo.
# In đảo ngược danh sách.
# Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
# tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
# đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
# In ra vị trí các phần tử là số nguyên tố.
# tìm các số duy nhất (không trùng lặp) trong danh sách.
# liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
# In ra các đoạn con trong danh sách giảm liên tiếp.
import random
import os
import math
def menu():
    print('1.\tIn ra danh sách vừa tạo')
    print('2.\tIn đảo ngược danh sách')
    print('3.\tSắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted)')
    print('4.\tTìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng')
    print('5.\tDếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện')
    print('6.\tIn ra vị trí các phần tử là số nguyên tố')
    print('7.\tTìm các số duy nhất (không trùng lặp) trong danh sách')
    print('8.\tLiệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó')
    print('9.\tIn ra các đoạn con trong danh sách giảm liên tiếp')
    print('10.\tThoat')

def create_list(n):
    cList = []
    for i in range(n):
        num = random.randint(1, 100)
        cList.append(num)
    return cList

def descending_sublist(lst):
    result = []
    temp = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            temp.append(lst[i])
        else:
            if len(temp) > 1:
                result.append(temp)
            temp = [lst[i]]
    if len(temp) > 1:
        result.append(temp)
    
    return result

if __name__ == '__main__':
    menu()
    n = int(input('Enter number of items in list: '))
    cList = create_list(n)
    n = input('Enter your choice: ')
    if n == '1':
        print(cList)
    elif n == '2':
        print(cList[::-1])
    elif n == '3':
        print(sorted(cList))
    elif n == '4':
        max = 0
        ind = 0
        for i in range(len(cList)):
            if max <= cList[i]:
                max = cList[i]
                ind = i
        print(f'Phan tu lon nhat trong danh sach: {max}')
        print(f'Vi tri phan tu lon nhat cuoi cung: {ind}')
    elif n == '5':
        print(cList)
        x = int(input('Nhap gia tri X: '))
        countX = 0
        for i in range(len(cList)):
            if x == cList[i]:
                countX += 1
                print(i)
        print(countX)
    elif n == '6':
        print(cList)
        for i in range(len(cList)):
            for j in range(2, int(math.sqrt(i) + 1)):
                if cList[i] % j != 0:
                    print(i)
    elif n == '7':
        print(cList)
        same_list = []
        for i in range(len(cList)):
            if cList[i] not in cList[i+1:]:
                same_list.append(cList[i])            
        print(same_list)
    elif n == '8':
        dict = {}
        # dict[i] = count if i not in dict and i != ' ' in (for i in cList)
        for i in cList:
            if i not in dict and i != ' ':
                count = cList.count(i)
                dict[i] = count
        print(dict)
    elif n == '9':
        print(cList)
        sublists = descending_sublist(cList)
        print('Cac doan giam lien tiep: ')
        for sub in sublists:
            print(sub)
    else:
        os.system('cls')


