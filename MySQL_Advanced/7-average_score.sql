-- script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. An average score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    
    -- Compute the average score
    SELECT AVG(score) INTO average_score FROM correction WHERE corrections.user_id = p_user_id;

    -- Update the user average score
    UPDATE users SET average_score = average_score WHERE id = p_user_id;
END//
DELIMITER ;