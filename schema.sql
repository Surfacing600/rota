create table tenant1(
    id integer primary key autoincrement,
    tenant_name1 text not null
);

create table tenant2(
    id integer primary key autoincrement,
    tenant_name2 text not null
);

create table tenant3(
    id integer primary key autoincrement,
    tenant_name3 text not null
);

create table tenant4(
    id integer primary key autoincrement,
    tenant_name4 text not null
);

create table rubbish_removal(
    id integer primary key autoincrement,
    tenant_rubbish text not null
);