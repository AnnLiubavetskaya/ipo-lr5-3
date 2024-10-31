with open('text.txt', 'r') as file:
    read = file.read()  # Читает весь файл
    words = read.split() 
    
    print("Слов в файле: " + str(len(words)))  #возвращение длины строки
     
