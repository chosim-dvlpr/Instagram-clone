INSERT INTO apps_feed (content, image, profile_image, user_id, like_count) VALUES('내용', '사진', '프로필 사진', '사용자id', '좋아요 개수');
DELETE FROM apps_feed WHERE rowid = 2;
SELECT * FROM apps_feed