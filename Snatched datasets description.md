1. [Muenster BarcodeDB](https://www.uni-muenster.de/PRIA/en/forschung/index.shtml)

"""
    Muenster BarcodeDB
    │   N95-2592x1944_scaledTo1024x768bilinear_v1.md5
    │   N95-2592x1944_scaledTo1600x1200bilinear_v1.md5
    │   N95-2592x1944_scaledTo640x480bilinear_v1.md5
    │   N95-2592x1944_scaledTo800x600bilinear_v1.md5
    │   N95-2592x1944_scaledTo800x600NN_v1.md5
    │   N95-2592x1944_v1.md5
    │   readme.html
    │
    ├───N95-2592x1944_scaledTo1024x768bilinear_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_scaledTo1024x768bilinear_v1.md5
    │   │
    │   └───N95-2592x1944_scaledTo1024x768bilinear
    │           *.jpg
    │
    ├───N95-2592x1944_scaledTo1600x1200bilinear_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_scaledTo1600x1200bilinear_v1.md5
    │   │
    │   └───N95-2592x1944_scaledTo1600x1200bilinear
    │           *.jpg
    │
    ├───N95-2592x1944_scaledTo640x480bilinear_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_scaledTo640x480bilinear_v1.md5
    │   │
    │   ├───N95-2592x1944_scaledTo640x480bilinear
    │   │       .DS_Store
    │   │       *.jpg
    │   │
    │   └───__MACOSX
    │       └───N95-2592x1944_scaledTo640x480bilinear
    │               ._.DS_Store
    │
    ├───N95-2592x1944_scaledTo800x600bilinear_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_scaledTo800x600bilinear_v1.md5
    │   │
    │   └───N95-2592x1944_scaledTo800x600bilinear
    │           *.jpg
    │
    ├───N95-2592x1944_scaledTo800x600NN_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_scaledTo800x600NN_v1.md5
    │   │
    │   └───N95-2592x1944_scaledTo800x600NN
    │           *.jpg
    │
    ├───N95-2592x1944_v1
    │   │   MuensterBarcodeDB_v1.txt
    │   │   N95-2592x1944_v1.md5
    │   │
    │   └───N95-2592x1944
    │           *.jpg
    │
    ├───nokia-N95-1024-768
    │   └───nokia-N95-1024-768
    │           *.jpg
    │
    └───nokia-N95-5-Mio
        └───nokia-N95-Imgs
                *.jpg
   """

    Конечные папки (кроме _MACOSX) содержат .jpg изображения. Все из них - крупно снятые 1d баркоды. На некоторых изображениях есть искажения: засветы, небольшие деформации упаковки (следовательно и помятые баркоды), размытость. На некоторых изображениях (редко) встречаются сразу несколько 1d баркодов, при этом  некоторые из них могут быть видны лишь частично, другие могут иметь иные искажения. Разметки нет. Есть лицензия, она предполагает лишь некоммерческое свободное использование, для коммерческого использования необходимо обратиться к авторам датасета. Если  датасет используется для некоммерческого использования, необходимо указывать авторство датасета.

3. [DEAL KAIST Lab Barcode Main](https://1drv.ms/u/s!Atg_Cq2yco129l2Ji_HrZv0oGkQT?e=agxvMF)

"""
    barcode_bb
    │   rec.txt
    │   single_test.txt
    │   train.txt
    │   val.txt
    │
    ├───rec
    │       *.jpg
    │
    └───single_test
            *.jpg
"""

    Папки single_test и rec содержат .jpg изображения. Все из них - 1d баркоды, в основном сняты крупно. Изображения разных размеров. На некоторых изображениях есть искажения. В основном по 1 баркоду на изображение (может где-то есть больше, но я не нашел).
    Файлы rec.txt и single_test.txt содержат разметку изображений из папок rec и single_test соответственно, в формате: "имя_файла.jpg x1 y1 x2 y2 0\n". Нормировки по масштабу нет, т.е. x1 x2 y1 y2 принимают значения от 0 до ширины и высоты изображения в пикселях соответственно.
    Файлы val.txt и train.txt также содержат разметку в таком же формате, .jpg для нее взяты из папки rec (!это не точно, я проверил только по парочке названий файлов, все они были из папки rec, но есть вероятность того, что некоторые другие могут быть из папки single_test!)

4. [DEAL KAIST Lab Barcode EAN-8](https://1drv.ms/u/s!Atg_Cq2yco129m6GG5s7izwntNPZ?e=enKB7G)

"""
    e8_bb
    │   e8.txt
    │
    └───e8
            *.jpg
"""

    Папка e8 содержит .jpg изображения, все из которых - 1d баркоды, сняты достаточно крупно, бывают искажения. Датасет маленький (всего несколько сотен изображений). В основном по 1 баркоду на изображение.
    Файл e8.txt содержит разметку изображений из папки e8 в формате: "имя_файла.jpg x1 y1 x2 y2 0\n". Нормировки по масштабу нет, т.е. x1 x2 y1 y2 принимают значения от 0 до ширины и высоты изображения в пикселях соответственно.

5. [Arte-Lab Medium Barcode 1D #1]([https://1drv.ms/u/s!Atg_Cq2yco129m-K-8CkvrGHtJ4p?e=2jiaaw](http://artelab.dista.uninsubria.it/downloads/datasets/barcode/medium_barcode_1d/medium_barcode_1d.html)http://artelab.dista.uninsubria.it/downloads/datasets/barcode/medium_barcode_1d/medium_barcode_1d.html)

"""
    Testing
    │       *.jpg
    │       *.txt
    │
    ├───Training
    │       *.jpg
    │       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат крупно снятые 1d баркоды, с редкими искажениями. Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

6. [Arte-Lab Medium Barcode 1D #2](http://artelab.dista.uninsubria.it/downloads/datasets/barcode/medium_barcode_1d/medium_barcode_1d.html)

"""
    Testing
    │       *.jpg
    │       *.txt
    │
    ├───Training
    │       *.jpg
    │       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат крупно снятые 1d баркоды, с редкими искажениями. Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

7. [Arte-Lab Hough Transform Barcode 1D](http://artelab.dista.uninsubria.it/downloads/datasets/barcode/hough_barcode_1d/hough_barcode_1d.html)

"""
    Testing
    │       *.jpg
    |       *.txt
    │
    ├───Training
    │       *.jpg
    |       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат крупно снятые 1d баркоды, с редкими искажениями. Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

8. [InventBar](https://onedrive.live.com/?authkey=%21AKXkkIuTEa8bGMc&id=2937E7810656A67B%211159&cid=2937E7810656A67B)

"""
    Testing
    │       *.jpg
    |       *.txt
    │
    ├───Training
    │       *.jpg
    |       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат крупно снятые 1d баркоды, с редкими искажениями (редко, но встречаются изображения с несколькими баркодами, иногда даже есть 2d). Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

9. [Arte-Lab Rotated Barcode](https://onedrive.live.com/?authkey=%21AKXkkIuTEa8bGMc&id=2937E7810656A67B%211159&cid=2937E7810656A67B)

"""
    Testing
    │       *.jpg
    |       *.txt
    │
    ├───Training
    │       *.jpg
    |       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат крупно снятые 1d баркоды, с редкими искажениями (редко встречаются сразу несколько баркодов на одном изображении, при этом в разметке это не учтено, в ней содержится только одна строчка). Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

10. [ParcelBar](https://onedrive.live.com/?authkey=%21AKXkkIuTEa8bGMc&id=2937E7810656A67B%211159&cid=2937E7810656A67B)

"""
    Testing
    │       *.jpg
    |       *.txt
    │
    ├───Training
    │       *.jpg
    |       *.txt
    │
    └───Validation
            *.jpg
            *.txt
"""

    Папки Testing, Training и Validation содержат .jpg изображения и .txt разметку для каждого .jpg изображения (имена файлов одинаковые, отличаются только расширения). Все изображения содержат 1d баркоды (сняты не крупно, со средней дистанции), с редкими искажениями (редко встречаются сразу несколько баркодов на одном изображении, при этом в разметке это не учтено, в ней содержится только одна строчка). Разметка имеет формат: "0 x1 y1 x2 y2", где x1 x2 y1 y2 - числа от 0 до 1, т.е. отнормированы по масштабу.

11. [Szentandrási QR Datasets](http://www.fit.vutbr.cz/research/groups/graph/pclines/pub_page.php?id=2012-SCCG-QRtiles)

"""
    qrcode-datasets
    │   README.TXT
    │
    ├───bitmaps
    │       *.png
    │
    └───datasets
        ├───img_1080p
        │       *.JPG
        |       *.csv
        │
        ├───lighting
        │       *.JPG
        |       *.csv
        │
        ├───mobile_multi
        │       *.JPG
        |       *.csv
        │
        ├───more_hard
        │       *.JPG
        |       *.csv
        │
        ├───more_low
        │       *.JPG
        |       *.csv
        │
        ├───more_medium
        │       *.JPG
        |       *.csv
        │
        ├───one_hard
        │       *.JPG
        |       *.csv
        │
        ├───one_low
        │       *.JPG
        |       *.csv
        │
        ├───one_medium
        │       *.JPG
        |       *.csv
        │
        └───semi_high
                *.JPG
                *.csv
"""

    Папки с .JPG и .csv файлами содержат изображения 2d баркодов и их разметку соответственно. Описание разметки представлено в файле README.TXT. Папка bitmaps содержит битовые карты 2d баркодов из .JPG изображений.

12. [Dubská QR Datasets #1](http://www.fit.vutbr.cz/research/groups/graph/pclines/pub_page.php?id=2012-JRTIP-MatrixCode)

"""
    dataset1
        *.jpg
        anotation.csv
        README.txt
"""

"""
    dataset2
        anotation.csv
        *.jpg
"""

    По ссылке доступны для скачивания 2 датасета. Файлы anotation.csv содержат информацию об изображениях. Файлы .jpg содержат изображения с 2d баркодами, по одному на изображение.

13. [Synthetic Barcode Datasets (SBD)](https://github.com/viplabB/SBD/)

    Генератор изображений с баркодами

14. [Bodnár-Huawei Syn10k](https://www.inf.u-szeged.hu/~bodnaar/barcode_database/)

"""
    syn10k_plus_huawei
    ├───huawei
    |       *.jpg
    ├───huawei_gt
    |       *.png
    ├───warp2014_gt
    |       *.png
    └───warp2014_jpg
            *.jpg
"""

    Папка huawei содержит .jpg файлы с изображениями 2d баркода, снятого крупным планом, по одному баркоду на изображения, есть искажения. 
    Папка huawei_gt содержит .png файлы с масками для 2d баркодов из папки huawei.
    Папка warp2014_gt содержит .png файлы с масками для 2d баркодов из папки warp2014_jpg.
    Папка warp2014_jpg содержит .jpg файлы с 2d баркодами, по одному баркоду на файл, есть искажения.

15. [QR-DN1.0](https://data.mendeley.com/datasets/t2bdr663ms/2)

"""
    QR-DN1.0
    ├───extracted One
    │   ├───test
    |   |       *.jpg
    │   ├───train
    |   |       *.jpg
    ├───extracted Quad
    │   ├───test
    |   |       *.jpg
    │   ├───train
    |   |       *.jpg
    ├───extracted Voted
    │   ├───test
    |   |       *.jpg
    │   ├───train
    |   |       *.jpg
    ├───QR
    │   ├───test
    |   |       *.jpg
    │   ├───train
    |   |       *.jpg
    ├───target
    │   ├───test
    |   |       *.jpg
    │   ├───train
    |   |       *.jpg
    └───target quad
        ├───test
        |       *.jpg
        └───train
                *.jpg
"""

    Конечные папки содержат .jpg изображения. На каждом изображении 2d баркоды, изображения все ч/б, все выровнены, без искажений, баркоды на всё изображение. В папке extracted Voted на изображениях есть шум. В папках extracted Quad и target quad на изображении по 4 баркода. Разметки нет.
