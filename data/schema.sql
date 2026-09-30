CREATE TABLE backlog(id VARCHAR PRIMARY KEY, title VARCHAR NOT NULL, status VARCHAR NOT NULL, note VARCHAR, opened DATE NOT NULL, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')), CHECK((status IN ('open', 'in-progress', 'done'))));;
CREATE TABLE facts(id VARCHAR PRIMARY KEY, status VARCHAR NOT NULL, "quote" VARCHAR, tags VARCHAR[] DEFAULT(main.list_value()) NOT NULL, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')), CHECK((status IN ('confirmed', 'preliminary', 'mechanistic', 'disputed', 'insufficient-evidence'))));;
CREATE TABLE fact_sources(fact_id VARCHAR, source_id VARCHAR, PRIMARY KEY(fact_id, source_id));;
CREATE TABLE i18n(entity_id VARCHAR, field VARCHAR, locale VARCHAR, "text" VARCHAR NOT NULL, PRIMARY KEY(entity_id, field, locale));;
CREATE TABLE relations(from_id VARCHAR, to_id VARCHAR, relation VARCHAR, note VARCHAR, PRIMARY KEY(from_id, to_id, relation), CHECK((from_id != to_id)));;
CREATE TABLE session_log(id VARCHAR PRIMARY KEY, entry_date DATE NOT NULL, title VARCHAR NOT NULL, done VARCHAR NOT NULL, considered VARCHAR, rejected VARCHAR, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')));;
CREATE TABLE sources(id VARCHAR PRIMARY KEY, title VARCHAR NOT NULL, url VARCHAR NOT NULL, author VARCHAR, "year" INTEGER, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')), CHECK(starts_with(url, 'https://')));;
CREATE TABLE terms(id VARCHAR PRIMARY KEY, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')));;
CREATE TABLE topics(id VARCHAR PRIMARY KEY, order_key INTEGER NOT NULL, tags VARCHAR[] DEFAULT(main.list_value()) NOT NULL, CHECK(regexp_matches(id, '^[a-z0-9]+(-[a-z0-9]+)*$')));;

