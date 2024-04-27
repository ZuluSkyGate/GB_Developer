-- create
CREATE TABLE EMPLOYEE
(
    Id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    adress TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE
VALUES
    (0001, 'Олег', 'Вышкин', 'Севастополь, ул.Ленина, д.2, кв.23');
INSERT INTO EMPLOYEE
VALUES
    (0002, 'Елена', 'Иванова', 'Севастополь, ул.Большая Морская,д.19, кв.43');
INSERT INTO EMPLOYEE
VALUES
    (0003, 'Тимур', 'Исламгулов', 'Москва, проспект Кирова, д.12, кв.19');

-- fetch 
SELECT *
FROM EMPLOYEE
WHERE adress  > 'Севастополь';