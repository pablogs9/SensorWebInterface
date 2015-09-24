drop table if exists data;
create table data (
  id integer primary key autoincrement,
  Period real not null,
  Frequency real not null,
  Pulses real not null,
  timestamp text not null
);
