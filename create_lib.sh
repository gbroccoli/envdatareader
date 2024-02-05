# генерация для windows
g++ -c -fPIC main.cpp -o envdatareader.o && g++ -shared -o envdatareader.dll envdatareader.o

# удаление ненужного файла
rm -rf envdatareader.o 

# генерация для linux
g++ -c -fPIC main.cpp -o envdatareader.o && g++ -shared -o envdatareader.so envdatareader.o

# удаление ненужного файла
rm -rf envdatareader.o
