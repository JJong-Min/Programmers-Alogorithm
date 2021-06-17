def main():
    f = open('sample_input.txt')
    T = int(f.readline())
    for i in range(T):
        camels = []
        f.readline()
        camels = list(map(int, f.readline().split()))
        
        if len(camels) == 1:
            print('#', str(i+1),' ', str(camels[0]), sep ='')
        
        else:
            cnt = 0
            to_cross_camels = []
            time = 0
            while camels:
                camels.sort()
                to_cross_camels.sort()

                if cnt%2 == 1:
                    camel_time = to_cross_camels.pop(0)
                    camels.append(camel_time)
                    time += camel_time
                    cnt += 1
                elif cnt%4 == 0:
                    to_cross_camels.append(camels.pop(0))
                    camel_time = camels.pop(0)
                    to_cross_camels.append(camel_time)
                    time += camel_time
                    cnt += 1
                else:
                    camel_time = camels.pop()
                    to_cross_camels.append(camel_time)
                    to_cross_camels.append(camels.pop())
                    time += camel_time
                    cnt += 1
            print('#', str(i+1),' ', str(time), sep ='')

main()

