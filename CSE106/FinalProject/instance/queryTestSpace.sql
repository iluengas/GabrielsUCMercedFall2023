
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

-- SELECT MAX(rowID) 
-- FROM PostTags;

-- SELECT l_postID 
-- FROM likes
-- WHERE l_userID = 0;

-- SELECT postID, post_userID, post_textContent, post_creationDate, post_likes, post_dislikes, parent_postID
-- FROM Posts, 
-- (
--     SELECT l_postID 
--     FROM likes
--     WHERE l_userID = 0
-- )
-- WHERE postID = l_postID;

-- SELECT postID, username,  post_textContent, post_creationDate, likeCnt, post_dislikes
--             FROM Posts, Users,
--             (
--                 SELECT l_postID, COUNT(*) as likeCnt
--                 FROM Likes
--                 GROUP BY l_postID
--             ) 
--             WHERE post_userID = user_id AND 
--                     postID = l_postID;

-- SELECT l_postID, COUNT(*) as likeCnt
-- FROM Likes
-- GROUP BY l_postID;

-- SELECT postID
-- FROM PostTags 
-- WHERE tagID = 1;

-- SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
--             FROM Posts, Users, 
--             (
--                 SELECT postID as p_ID
--                 FROM PostTags 
--                 WHERE tagID = 1
--             )
--             WHERE postID = p_ID AND 
--                     post_userID = user_id; 

-- SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture
--             FROM Posts, Users
--             WHERE post_userID = user_id AND 
--                     parent_postID = 1;
    
SELECT postID, username,  post_textContent, post_imageContent, post_creationDate, post_likes, post_dislikes, profile_picture, parent_postID
            FROM Posts, Users,
            (
                SELECT b_postID
                FROM Bookmarks 
                WHERE b_userID = 0
            ) 
            WHERE post_userID = user_id AND
                    postID = b_postID;

SELECT b_postID
FROM Bookmarks 
WHERE b_userID = 0;