def diagonaladd(arr):
    prim_diag = 0
    sec_diag = 0

    for i in range(len(arr)):
        # adding the first diagonal matrix i.e 11,5,-12
        # print(arr[i][i])
        prim_diag += arr[i][i]
        # adding the second diagonal matrix i.e 4,5,10
        sec_diag += arr[i][-1-i]
    diff = (prim_diag - sec_diag)
    print(f'The expected output for the difference between the diagonal lines a matrix array is: {abs(diff)}')

diagonaladd( [[11,2,4],[4,5,6],[10,8,-12]])