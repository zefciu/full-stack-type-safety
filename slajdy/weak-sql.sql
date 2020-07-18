UPDATE books set author_id = (
	SELECT id FROM publishers
	WHERE name="Chilton Books"
);

