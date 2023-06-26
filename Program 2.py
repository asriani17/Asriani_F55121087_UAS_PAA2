import time

# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp_algorithm(graph, start_vertex):
    num_vertices = len(graph)
    vertex_set = set(range(num_vertices))
    memo = {}

    # Rekursif dengan memoization
    def tsp_helper(curr_vertex, vertex_set):
        # Base case
        if len(vertex_set) == 1:
            return graph[curr_vertex][start_vertex]

        # Mengecek memoization
        memo_key = (curr_vertex, tuple(vertex_set))
        if memo_key in memo:
            return memo[memo_key]

        min_distance = float('inf')
        for next_vertex in vertex_set:
            if next_vertex == start_vertex or next_vertex == curr_vertex:
                continue
            distance = graph[curr_vertex][next_vertex] + tsp_helper(next_vertex, vertex_set - {next_vertex})
            min_distance = min(min_distance, distance)

        # Menyimpan hasil ke dalam memo
        memo[memo_key] = min_distance
        return min_distance

    # Panggil fungsi rekursif
    shortest_path = tsp_helper(start_vertex, vertex_set)
    return shortest_path

# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra_algorithm(graph, start_vertex):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start_vertex] = 0
    visited = [False] * num_vertices

    # Proses iteratif untuk mencari shortest path
    for _ in range(num_vertices):
        min_dist = float('inf')
        min_vertex = -1

        # Mencari vertex dengan jarak terpendek
        for v in range(num_vertices):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v

        visited[min_vertex] = True

        # Update jarak terpendek untuk tetangga yang belum dikunjungi
        for v in range(num_vertices):
            if not visited[v] and graph[min_vertex][v] > 0:
                new_dist = dist[min_vertex] + graph[min_vertex][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    shortest_path = dist
    return shortest_path

# Fungsi untuk menjalankan algoritma TSP
def run_tsp(graph):
    start_time = time.time()
    shortest_path = tsp_algorithm(graph, 0)
    end_time = time.time()

    result = f"Jalur terpendek: {shortest_path}\n"
    result += f"Waktu komputasi: {end_time - start_time} detik"

    return result

# Fungsi untuk menjalankan algoritma Dijkstra
def run_dijkstra(graph, start_vertex):
    start_time = time.time()
    shortest_path = dijkstra_algorithm(graph, start_vertex)
    end_time = time.time()

    result = "Jarak terpendek dari vertex awal:\n"
    for i in range(len(shortest_path)):
        result += f"Vertex {i}: {shortest_path[i]}\n"
    result += f"Waktu komputasi: {end_time - start_time:.6f} detik"

    return result

# Fungsi untuk meminta input pilihan TSP atau Dijkstra dari pengguna
def get_user_choice():
    print("Pilih algoritma:")
    print("1. Travelling Salesman Problem (TSP)")
    print("2. Dijkstra")
    choice = input("Masukkan pilihan (1/2): ")
    while choice not in ['1', '2']:
        print("Pilihan tidak valid. Mohon masukkan pilihan yang benar.")
        choice = input("Masukkan pilihan (1/2): ")
    return int(choice)

# Fungsi utama
def main():
    # Graph
    graph = [
        [0, 12, 10, 0, 0, 0, 12],
        [12, 0, 0, 12, 0, 0, 0],
        [10, 0, 0, 11, 3, 0, 9],
        [0, 12, 11, 0, 11, 10, 0],
        [0, 0, 3, 11, 0, 6, 7],
        [0, 0, 0, 10, 6, 0, 9],
        [12, 0, 9, 0, 7, 9, 0]
    ]

    while True:
        # Meminta input pilihan dari pengguna
        choice = get_user_choice()

        # Menjalankan algoritma yang dipilih dan menampilkan hasilnya
        if choice == 1:
            tsp_result = run_tsp(graph)
            print(tsp_result)
        elif choice == 2:
            start_vertex = 0
            dijkstra_result = run_dijkstra(graph, start_vertex)
            print(dijkstra_result)

        # Meminta input pengguna untuk memilih kembali atau keluar
        play_again = input("Apakah Anda ingin memilih lagi? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == '__main__':
    main()
