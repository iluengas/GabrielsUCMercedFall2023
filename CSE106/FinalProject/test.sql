INSERT INTO Users(user_id, username, bio,
                     profile_picture, creation_date, views)
VALUES(?, ?, ?, ?, datetime('now', 'localtime'), 0);

INSERT INTO Posts(postID, post_userID,
                 post_textContent, post_imageContent,
                 post_creationDate, post_likes,
                 post_dislikes, parent_postID)
VALUES(5, 3, 'Insertion DataTime test', NULL, datetime('now', 'localtime'), 0, 0, NULL );