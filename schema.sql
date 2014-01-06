drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  course text not null,
  seats integer not null
);

