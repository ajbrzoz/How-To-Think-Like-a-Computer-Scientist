# Exercise 15.8.6

# Implement a solution to the Tower of Hanoi using three stacks to keep track of the disks.


def hanoi(n, fromp, top, withp):
    if n >= 1:
        hanoi(n - 1, fromp, withp, top)
        move_disk(fromp, top)
        hanoi(n - 1, withp, top, fromp)


def move_disk(fp, tp):
    print('{} --> {}'.format(fp, tp))


hanoi(3, 'A', 'C', 'B')
