-- SQL script that creates a function SafeDiv that divides (and returns) the
-- first by the second number or returns 0 if the second number is 0
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        return 0;
    ELSE
        return a / b;
    END IF;
END//
DELIMITER ;