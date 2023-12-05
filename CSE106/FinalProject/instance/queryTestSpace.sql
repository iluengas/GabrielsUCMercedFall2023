
-- CREATE TABLE Posts (
--     postID            INTEGER PRIMARY KEY
--                               NOT NULL,
--     post_userID       INTEGER,
--     post_textContent  TEXT,
--     post_imageContent BLOB,
--     post_creationDate  TEXT,
--     post_likes  INTEGER,
--     post_dislikes   INTEGER,
--     parent_postID   INTEGER,
--     FOREIGN KEY (parent_postID) REFERENCES Posts(postID),
--     FOREIGN KEY (post_userID) REFERENCES Users(user_id)
-- );

-- SELECT * FROM Posts WHERE parent_postID = 1;

-- CREATE TABLE PostTags (
--     rowID INTEGER PRIMARY KEY NOT NULL,
--     postID INT,
--     tagID INT,
--     FOREIGN KEY (postID) REFERENCES Posts(postID),
--     FOREIGN KEY (tagID) REFERENCES Tags(tagID)
-- );

-- Functions to inssert Data into posts and Users

-- INSERT INTO Users(user_id, username, bio,
--                      profile_picture, creation_date, views)
-- VALUES(?, ?, ?, ?, datetime('now', 'localtime'), 0);

-- INSERT INTO Posts(postID, post_userID,
--                  post_textContent, post_imageContent,
--                  post_creationDate, post_likes,
--                  post_dislikes, parent_postID)
-- VALUES(5, 3, 'Insertion DataTime test', NULL, datetime('now', 'localtime'), 0, 0, NULL );


-- Funtions to attatch usernames belonging to a post's user to the postQuery (replacing the post_userID column)
-- SELECT postID, username, post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes 
-- FROM Posts, Users 
-- WHERE post_userID = user_id;

-- SELECT * 
-- FROM Likes 
-- WHERE l_userID = 3 AND
--         l_postID = 1;

SELECT * 
FROM Dislikes
WHERE d_userID = ? AND 
        l_postID = ?;