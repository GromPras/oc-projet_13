Database Schema & Data Models
=============================

Entity–Relationship Diagram
---------------------------

.. graphviz::
   :caption: ER Diagram for oc-lettings-site

   digraph ER {
     graph [rankdir=LR];
     node [shape=record, fontsize=12, fontname="Helvetica"];

     User [
       label="{ User | \
       id: INT PK\l\
       username: VARCHAR(150) UNIQUE\l\
       first_name: VARCHAR(150)\l\
       last_name: VARCHAR(150)\l\
       email: VARCHAR(254)\l\
       is_staff: BOOL\l\
       is_active: BOOL\l\
       date_joined: DATETIME\l\
       }"
     ];

     Address [
       label="{ Address | \
       number: INT\l\
       street: VARCHAR(64)\l\
       city: VARCHAR(64)\l\
       state: CHAR(2)\l\
       zip_code: INT\l\
       country_iso_code: CHAR(3)\l\
       }"
     ];

     Letting [
       label="{ Letting | \
       id: INT PK\l\
       title: VARCHAR(256)\l\
       address_id: INT FK → Address.id\l\
       }"
     ];

     Profile [
        label="{ Profile | \
        id: INT PK\l\
        user_id: INT FK → User.id\l\
        favorite_city: VARCHAR(64)\l\
        }"
     ];

     /* Relationships */
     Address -> Letting [arrowhead=normal, label="has_one"];
     User -> Profile   [arrowhead=normal, label="has_one"];
   }


Data Model Descriptions
-----------------------

.. glossary::
    User
        **Fields**
            - id (AutoField, primary key)
            - username (CharField, max_length=150, unique)
            - first_name (CharField, max_length=150, blank=True)
            - last_name (CharField, max_length=150, blank=True)
            - email (EmailField, blank=True)
            - is_staff (BooleanField)
            - is_active (BooleanField)
            - date_joined (DateTimeField)

    Address
        **Fields**
            - id (AutoField, primary key)
            - number (PositiveIntegerField, max 9999)
            - street (CharField, max_length=64)
            - city (CharField, max_length=64)
            - state (CharField, max_length=2)
            - zip_code (PositiveIntegerField, max 99999)
            - country_iso_code (CharField, max_length=3)

    Letting
        **Fields**
            - id (AutoField, primary key)
            - title (CharField, max_length=256)
            - address_id (OneToOneField to Address.id)

    Profile
        **Fields**
            - id (AutoField, primary key)
            - user_id (OneToOneField to User.id)
            - favorite_city (CharField, max_length=64, blank=True)
