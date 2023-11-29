

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

SELECT * FROM Posts WHERE parent_postID = 1;

CREATE TABLE PostTags (
    rowID INTEGER PRIMARY KEY NOT NULL,
    postID INT,
    tagID INT,
    FOREIGN KEY (postID) REFERENCES Posts(postID),
    FOREIGN KEY (tagID) REFERENCES Tags(tagID)
);