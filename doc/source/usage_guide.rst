User Guide
======================

Use Cases
----------------

.. graphviz::
   :caption: Use Case Diagram for oc-lettings-site

   digraph UseCase {
     graph [rankdir=TB, splines=ortho];
     node [shape=ellipse, fontsize=12, fontname="Helvetica"];
     
     /* Actors */
     Guest [shape=actor, label="Guest"];
     User [shape=actor, label="Registered User"];
     Admin [shape=actor, label="Administrator"];

     /* Use cases */
     Browse [label="Browse Listings"];
     ViewDetail [label="View Listing Details"];
     Register [label="Register"];
     Login [label="Login"];
     ManageProfile [label="Manage Profile"];
     CreateLetting [label="Create Listing"];
     EditLetting [label="Edit Listing"];
     DeleteLetting [label="Delete Listing"];
     ManageUsers [label="Manage Users"];
     ManageAll [label="Manage All Listings"];

     /* Associations */
     Guest -> Browse;
     Guest -> ViewDetail;
     Guest -> Register;
     Guest -> Login;

     User -> Browse;
     User -> ViewDetail;
     User -> ManageProfile;
     User -> CreateLetting;
     User -> EditLetting;
     User -> DeleteLetting;

     Admin -> ManageUsers;
     Admin -> ManageAll;
   }

