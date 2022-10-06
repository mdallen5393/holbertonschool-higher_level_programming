# PROJECT: 0x01. SQL - More queries
### AUTHOR: Matthew Allen

## TASKS:
### 0. My privileges! - 0-privileges.sql
Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

### 1. Root user - 1-create_user.sql
Script that creates the MySQL server user `user_0d_1` with all privileges.

### 2. Read user - 2-create_read_user.sql
Script that creates the database `hbtn_0d_2` and the user `user_0d_2` which only has the SELECT privilege.

### 3. Always a name - 3-force_name.sql
Script that creates the tabel `force_name` containing `id` INT, `name` VARCHAR(256) NOT NULL.

### 4. ID can't be null - 4-never_empty.sql
Script that creates the table `id_not_null` with `id` INT (default value `1`), `name` VARCHAR(256).

### 5. Unique ID - 5-unique-id.sql
Script that creates the table `unique_id` with `id` INT (default 1, unique), `name` VARCHAR(256).

### 6. States table - 6-states.sql
Script that creates the database `hbtn_0d_usa` and the table `states` with `id` INT (unique, auto, not null, PK), `name` VARCHAR(256) (not null).

### 7. Cities table - 7-cities.sql
Script that creates the database `hbtn_0d_usa` and the table `cities` with `id` INT (unique, auto, not null, PK), `state_id` INT (not null, FK ref `id` of `states`), `name` VARCHAR(256) (not null)

### 8. Cities of California - 8-cities_of_california_subquery.sql
Script that lists all cities of California that can be found in the database `hbtn_0d_usa`, where `states` contains only one record where `name` = `California` (but the `id` can be different), sorted ascending by `cities.id`.

### 9. Cities by States - 9-cities_by_state_join.sql
Script that lists all cities contained in teh database `hbtn_0d_usa`, displaying `cities.id` - `cities.name` - `states.name`, in ascending order.

### 10. Genre ID by show - 10-genre_id_by_show.sql
Script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked, displaying `tv_shows.title` - `tv_show_genres.genre_id`, sorted in ascending order by `tv_shows.genre_id`.

### 11. Genre ID for all shows - 11-genre_id_all_shows.sql
Script that lists all shows contained in the database `hbtn_0d_tvshows`, displaying `tv_shows.title` - `tv_show_genres.genre_id`, ordered ascending by `tv_shows.title` and `tv_show_genres.genre_id`.

### 12. No genre - 12-no_genre.sql
Script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked, displaying `tv_shows.title` - `tv_show_genres.genre_id`, sorted ascending by `tv_shows.title` and `tv_show_genres.genre_id`.

### 13. Number of shows by genre - 13-count_shows_by_genre.sql
Script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

### 14. My genres - 14-my_genres.sql
Script that uses the `hbtn_0d_tvshows` database to list all genres of the show `Dexter`.

### 15. Only Comedy - 15-comedy_only.sql
Script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

### 16. List shows and genres - 16-shows_by_genre.sql
Script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
