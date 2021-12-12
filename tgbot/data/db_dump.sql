
-- Таблица: Operators
CREATE TABLE IF NOT EXISTS Operators (
    id SERIAL PRIMARY KEY,
    tg_id BIGINT NOT NULL UNIQUE,
    name VARCHAR(32) NOT NULL,
    is_ready BOOLEAN NOT NULL DEFAULT(False)
);

-- Таблица: Sessions
CREATE TABLE IF NOT EXISTS Dialogs (
    id SERIAL PRIMARY KEY,
    operator_tg_id BIGINT NOT NULL,
    client_tg_id BIGINT NOT NULL,
    UNIQUE(operator_tg_id, client_tg_id),
    FOREIGN KEY (operator_tg_id) REFERENCES Operators(tg_id)
);

-- Таблица: Tickets
CREATE TABLE IF NOT EXISTS Tickets (
    id SERIAL PRIMARY KEY,
    client_tg_id BIGINT NOT NULL,
    msg_id BIGINT NOT NULL,
    datetime_msg TIMESTAMP NOT NULL,
    UNIQUE(client_tg_id, msg_id)
);
