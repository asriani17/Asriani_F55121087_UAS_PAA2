**UAS PAA2**

**Asriani_F55121087**

**Hasil analysis algorithm**

# **bubble sort and insertion sort**

**a. Worst case:**

-Kasus terburuk terjadi ketika elemen-elemen dalam array terurut secara terbalik (dalam urutan menurun).
-Dalam hal ini, Bubble Sort dan Insertion Sort akan menghabiskan waktu komputasi paling lama.
-Kompleksitas waktu Bubble Sort dalam kasus terburuk adalah O(n^2).
-Kompleksitas waktu Insertion Sort dalam kasus terburuk juga adalah O(n^2).
-Iterasi pada setiap langkah pengurutan akan mencapai jumlah maksimum.

**b. Best case:**
-Kasus terbaik terjadi ketika elemen-elemen dalam array sudah terurut dengan benar (dalam urutan menaik).
-Dalam hal ini, Bubble Sort dan Insertion Sort akan memiliki waktu komputasi yang paling cepat.
-Kompleksitas waktu Bubble Sort dalam kasus terbaik adalah O(n) karena tidak ada pertukaran yang perlu dilakukan.
-Kompleksitas waktu Insertion Sort dalam kasus terbaik adalah O(n) karena tidak perlu menggeser elemen.
-Iterasi pada setiap langkah pengurutan akan mencapai jumlah minimum.

c. Average case:
-Kasus rata-rata terjadi ketika elemen-elemen dalam array tidak terurut dengan benar, namun tidak dalam urutan terbalik yang ekstrem.
-Dalam hal ini, Bubble Sort dan Insertion Sort akan memiliki waktu komputasi dan iterasi yang berada di antara kasus terbaik dan kasus terburuk.
-Kompleksitas waktu Bubble Sort dalam kasus rata-rata adalah O(n^2).
-Kompleksitas waktu Insertion Sort dalam kasus rata-rata juga adalah O(n^2).
-Jumlah iterasi pada setiap langkah pengurutan akan bervariasi tergantung pada keadaan array.

# **TSP dan Djikstra**

**a. Worst Case:**
-Untuk algoritma TSP (Travelling Salesman Problem): Pada kasus terburuk, kompleksitas waktu algoritma TSP adalah O(n!), di mana n adalah jumlah vertex dalam graph. Ini karena algoritma TSP menggunakan pendekatan brute force yang menguji semua kemungkinan permutasi dari vertex untuk mencari jalur terpendek. Oleh karena itu, waktu komputasi akan meningkat secara eksponensial seiring bertambahnya jumlah vertex.

-Untuk algoritma Dijkstra: Pada kasus terburuk, kompleksitas waktu algoritma Dijkstra adalah O(V^2), di mana V adalah jumlah vertex dalam graph. Hal ini terjadi ketika semua vertex harus dikunjungi dan diuji untuk mengupdate jarak terpendek. Jika graph sangat besar, kompleksitas ini dapat menjadi cukup tinggi.

**b. Best case:**
-Untuk algoritma TSP (Travelling Salesman Problem): Pada kasus terbaik, jika jumlah vertex dalam graph sangat kecil, maka waktu komputasi algoritma TSP akan relatif cepat. Namun, karena algoritma TSP menggunakan pendekatan brute force, kompleksitas waktu akan tetap tinggi ketika jumlah vertex meningkat.
-Untuk algoritma Dijkstra: Pada kasus terbaik, jika graph sangat sederhana dan hanya memiliki beberapa vertex, maka waktu komputasi algoritma Dijkstra akan relatif cepat. Kompleksitas waktu tergantung pada jumlah vertex dan tingkat keterhubungan di antara mereka. Jika graph sangat kompleks dan terhubung dengan baik, kompleksitas waktu akan meningkat.

**c. Average case:**
-Untuk algoritma TSP (Travelling Salesman Problem): Rata-rata kasus pada algoritma TSP tidak memiliki kompleksitas waktu yang ditentukan secara pasti. Namun, secara umum, kompleksitas waktu algoritma TSP cenderung tinggi karena pendekatannya yang memerlukan pengujian semua kemungkinan permutasi.

-Untuk algoritma Dijkstra: Rata-rata kasus pada algoritma Dijkstra juga tidak memiliki kompleksitas waktu yang ditentukan secara pasti. Namun, algoritma Dijkstra cenderung lebih efisien daripada algoritma TSP dalam banyak kasus karena kompleksitasnya yang lebih rendah (O(V^2)) dan pendekatannya yang menggunakan pendekatan greedy.
