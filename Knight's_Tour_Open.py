# Python3 program to solve Knight Tour problem using Backtracking

# Ukuran Papan Catur
ukuran_papan = 8

def apakah_aman(x, y, papan):
    '''
        Fungsi utilitas untuk memeriksa apakah i,j adalah indeks yang valid
        untuk papan catur berukuran N*N
    '''
    if (x >= 0 and y >= 0 and x < ukuran_papan and y < ukuran_papan and papan[x][y] == -1):
        return True
    return False

def cetak_solusi(ukuran_papan, papan):
    '''
        Fungsi utilitas untuk mencetak matriks Papan Catur
    '''
    for i in range(ukuran_papan):
        for j in range(ukuran_papan):
            print(papan[i][j], end=' ')
        print()

def solve_knight_tour(ukuran_papan):
    '''
        Fungsi ini memecahkan masalah Knight Tour menggunakan
        Backtracking. Fungsi ini utamanya menggunakan solve_knight_tour_util()
        untuk memecahkan masalahnya. Ini mengembalikan False jika tidak ada tour
        yang lengkap mungkin, sebaliknya mengembalikan True dan mencetak tournya.
        Harap dicatat bahwa mungkin ada lebih dari satu solusi,
        fungsi ini mencetak salah satu solusi yang memungkinkan.
    '''

    # Inisialisasi matriks Papan
    papan = [[-1 for i in range(ukuran_papan)] for i in range(ukuran_papan)]

    # move_x dan move_y mendefinisikan langkah berikutnya dari Knight.
    # move_x adalah untuk nilai x koordinat berikutnya
    # move_y adalah untuk nilai y koordinat berikutnya
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Karena Knight awalnya berada di blok pertama
    papan[0][0] = 0

    # Penghitung langkah untuk posisi knight
    pos = 1

    # Memeriksa apakah solusi ada atau tidak
    if (not solve_knight_tour_util(ukuran_papan, papan, 0, 0, move_x, move_y, pos)):
        print("Solusi tidak ada")
    else:
        cetak_solusi(ukuran_papan, papan)

def solve_knight_tour_util(ukuran_papan, papan, curr_x, curr_y, move_x, move_y, pos):
    '''
        Fungsi utilitas rekursif untuk memecahkan masalah Knight Tour
    '''

    if (pos == ukuran_papan ** 2):
        return True

    # Coba semua langkah berikutnya dari koordinat x, y saat ini
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (apakah_aman(new_x, new_y, papan)):
            papan[new_x][new_y] = pos
            if (solve_knight_tour_util(ukuran_papan, papan, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking
            papan[new_x][new_y] = -1
    return False

# Kode Pengendali
if __name__ == "__main__":
    # Panggil Fungsi
    solve_knight_tour(ukuran_papan)
