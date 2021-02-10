create table tenant1(
    id integer primary key,
    tenant_name1 text not null
);

create table tenant2(
    id serial primary key,
    tenant_name2 text not null
);

create table tenant3(
    id serial primary key,
    tenant_name3 text not null
);

create table tenant4(
    id serial primary key,
    tenant_name4 text not null
);

create table rubbish_removal(
    id serial primary key,
    tenant_rubbish text not null
);