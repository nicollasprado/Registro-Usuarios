CREATE TABLE IF NOT EXISTS users (
    id INT unsigned NOT NULL PRIMARY KEY auto_increment,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(30) NOT NULL,
    creationTime datetime default now() NOT NULL
    lastUpdateTime datetime default on update now()
);

CREATE TABLE IF NOT EXISTS roles_categories (
    id INT unsigned NOT NULL PRIMARY KEY auto_increment,
    category_name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS roles (
    id INT unsigned NOT NULL PRIMARY KEY auto_increment,
    role_name VARCHAR(255) NOT NULL,
    category_id INT unsigned,
    FOREIGN KEY (category_id) REFERENCES roles_categories(id) ON DELETE CASCADE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS users_roles (
    user_id INT unsigned FOREIGN KEY REFERENCES users(id) NOT NULL ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) NOT NULL ON DELETE CASCADE
);

ALTER TABLE users ADD FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE;