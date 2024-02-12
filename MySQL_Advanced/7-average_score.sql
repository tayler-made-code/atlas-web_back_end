-- script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. An average score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- compute the total score
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = p_user_id;

    -- compute the total projects
    SELECT COUNT(*) INTO total_projects FROM corrections WHERE user_id = p_user_id;

    IF total_projects > 0 THEN
        --compute the average score
        SET average_score = total_score / total_projects;
    ELSE
        SET average_score = 0;
    END IF;

    -- update the user average score
    UPDATE users SET average_score = average_score WHERE id = p_user_id;
END//
DELIMITER ;