# https://sio2.mimuw.edu.pl/c/oij14-1/p/bas/

glob_reads = [1, 3, 8, 5, 6, 7, 8, 1, float('-inf')]

def count_pools(reads):
    previous = -1
    pools = 1
    for read in reads:
        if read < previous:
            pools += 1
        previous = read
    return pools

print(count_pools(glob_reads))