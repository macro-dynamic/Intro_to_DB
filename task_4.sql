-- Use the database passed as an argument
USE alx_book_store;

-- Query to get the full description of the books table
SELECT 
    COLUMN_NAME AS 'Column Name', 
    COLUMN_TYPE AS 'Column Type', 
    IS_NULLABLE AS 'Is Nullable', 
    COLUMN_DEFAULT AS 'Default Value', 
    EXTRA AS 'Extra Info'
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_NAME = 'Books' 
    AND TABLE_SCHEMA = 'alx_book_store';
