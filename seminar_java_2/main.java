/**
 * Напишите метод, который вернет содержимое текущей папки в виде массива строк.
 * Напишите метод, который запишет массив, возвращенный предыдущим методом в файл.
 * Обработайте ошибки с помощью try-catch конструкции. В случае возникновения исключения,
 * оно должно записаться в лог-файл.
 **/


public static void main(String[] args) {
        try {
            FileWriter fileWriter = new FileWriter("newText.txt");
            String[] list = getArrayString("D:/study/java_start/less1");
            for (String s : list) {
                fileWriter.write(s + "\n");
            }
            fileWriter.close();
            FileHandler fileHandler = new FileHandler("log.txt");
            LOGGER.addHandler(fileHandler);
            SimpleFormatter formatter = new SimpleFormatter();
            fileHandler.setFormatter(formatter);

            // Пример логгирования
            LOGGER.info("Пример записи в лог.");
            LOGGER.warning("Это предупреждение!");


            String fileName = "text.txt"; // Путь к файлу
            BufferedReader reader = new BufferedReader(new FileReader("text.txt"));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                // Здесь можно проводить дополнительную обработку каждой строки,
                // например, анализ или обработка данных
            }
        }catch (Exception e){

        }
    }