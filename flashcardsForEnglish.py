import csv
import random

if __name__ == '__main__':
    while True:
        with open('eng.csv', encoding='UTF-8_sig') as f:
            reader = csv.reader(f)
            l = []
            write = []
            left = 0
            for row in reader:
                if len(row) != 0:
                    l.append(row)
                    write.append(row)
                    if row[2] == '1':
                        left += 1
            
            print('全 ' + str(left) + ' 問')
            print('"]":わかった！　":":覚えた！')
        while True:
            i = random.randint(0, len(l) - 1)
            if l[i][2] != '1':
                continue

            print(l[i][0])
            input()
            print(l[i][1])

            command = input()
            if command.lower() == ']':
                print('  (　-`ω-)✧ わかった！')
                del l[i]
                left -= 1
                print('------------------------残り ' + str(left) + " 問")
            elif command.lower() == ':':
                print('ﾟ+｡:.ﾟヾ(≧∇≦*)/ 覚えた！.:｡+ﾟ')
                left -= 1
                print('------------------------残り ' + str(left) + " 問")

                for row in write:
                    if row[0] == l[i][0]:
                        row[2] = '0'
                        l[i][2] = '0'
                        break
                with open('eng.csv', 'w', encoding='UTF-8_sig', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(write)
            else:
                print('◆◆◆◆◆◆◆◆ (・_・)わからん……◆◆◆◆◆◆◆◆')
                print('------------------------')

            if left == 0:
                print('  旦_(-ω- ,,)一周しました。')
                print('')
                break
    
        



