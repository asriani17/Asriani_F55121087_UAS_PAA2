import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def print_iterations(arr):
    iterations = min(5, len(arr))
    iter_str = ""
    for i in range(iterations):
        iter_str += f"Iterasi {i + 1}: {arr[:i + 1]}\n"
    return iter_str

def sort_and_analyze(arr, sort_func):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    computation_time = end_time - start_time

    result_str = f"Sebelum pengurutan: {arr}\n"
    result_str += f"Setelah pengurutan: {sorted_arr}\n"
    result_str += f"Waktu komputasi: {computation_time:.6f} detik\n\n"
    result_str += "Iterasi:\n"
    result_str += print_iterations(arr)
    result_str += print_iterations(sorted_arr[::-1])

    return result_str

def analyze_algorithm(choice):
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    if choice == 1:
        result_str = sort_and_analyze(arr, bubble_sort)
    elif choice == 2:
        result_str = sort_and_analyze(arr, insertion_sort)
    else:
        result_str = "Pilihan tidak valid."

    print(result_str)

def get_user_choice():
    print("Pilih algoritma pengurutan:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    choice = input("Masukkan pilihan (1/2): ")
    while choice not in ['1', '2']:
        print("Pilihan tidak valid. Mohon masukkan pilihan yang benar.")
        choice = input("Masukkan pilihan (1/2): ")
    return int(choice)

def main():
    while True:
        choice = get_user_choice()
        analyze_algorithm(choice)

        play_again = input("Apakah Anda ingin memilih lagi? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()
