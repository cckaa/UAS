## UAS BAHASA PEMOGRAMAN
#### SOAL : Membuat program sederhana untuk melakukan scraping data web menggunakan package BeautifulSoap4. Sumber web scrapping bebas, misalnya perkiraan cuaca dari website bmkg, jadwal sholat dan website kemenag dan lain sebagainya.

#### JAWAB :

1. Untuk memulai proses coding pertama-tama kalian harus menginstall library Beautiful soup terlebih dahulu.
   Untuk menginstall library Beautiful soup dapat dilakukan dengan mengetikkan perintah pip3 install beautifulsoup tapi sebelumnya pastikan anda telah menginstall      PIP terlebih dahulu dengan menggunakan perintah apt-get install python3-pip .
   
2. Dari scritb scrapping shopee kita menggunakan 2 buah url Api.
   Api yang pertama kita gunakan untuk mencari toko berdasarkan ids tokonya. Url Api yang digunakan pada proses pencarian nama toko ini adalah seperti berikut ini :

       https://shopee.co.id/api/v1/shop_ids_by_username/
       
3. Akan tetapi saat mengakses Api tersebut kita membutuhkan sebuah Http header seperti berikut ini :

        "accept-encoding": "gzip, deflate, br",
            "content-type": "application/json",
            "if-none-match": "55b03-1ae7d4aa7c47753a96c0ade3a9ea8b35",
            "origin": "https://shopee.co.id",
            "referer": "https://shopee.co.id/asusofficialshop",
            "x-api-source": "pc",
            "x-csrftoken": "8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "cookie": 'SPC_IA=-1; SPC_EC=-; SPC_F=QpolQhTSikpnxRXO6T4RjIW8ZGHNBmBn; REC_T_ID=ac80cdde-0e7d-11e9-a8c2-3c15fb3af585; SPC_T_ID="e4t1VmH0VKB0NajA1BrHaDQlFRwWjTZT7o83rrHW+p16sTf1NJK7ksWWDicCTPq8CVO/S8sxnw25gNR0DLQz3cv7U3EQle9Z9ereUnPityQ="; SPC_SI=k2en4gw50emawx5fjaawd3fnb5o5gu0w; SPC_U=-; SPC_T_IV="in3vKQSBLhXzeTaGwMInvg=="; _gcl_au=1.1.557205539.1546426854; csrftoken=8XtQ7bHlv09rlx5U4NPN6rmavFn7MvTO; welcomePkgShown=true; bannerShown=true; _ga=GA1.3.472488305.1546426857; _gid=GA1.3.1348013297.1546426857; _fbp=fb.2.1546436170115.11466858'

4. Setelah tokonya ketemu kemudian kita lakukan scrapping data-data produknya pada toko tersebut dengan menggunakan url Api berikut ini :
    
       https://shopee.co.id/api/v2/search_items/?match_id={}&order=desc&page_type=shop
 
5. Untuk mengaksesnya pun dibutuhkan header seperti berikut ini :

       'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
       
6. Setelah semuanya selesai kemudian jalankan scribt tersebut .
7. Anda dapat mulai melakukan scrapping data dari website shoppe sekarang hanya dengan menginputkan ids nama toko pada shopee.
