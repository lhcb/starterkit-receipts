Starterkit receipts
===================

Prepare a PDF with receipts for Starterkit attendants.

How to use
----------

Go to the *Management* area of the indico event, then *Registration* and access the registrants list.
Select all, click `Export/CSV` and save in the same folder as the receipt system.
You can choose the name that you like, just remember to update the `Makefile`.

Then, a simple `make` will generate `receipts.pdf` and `attendance.pdf`. 


Aknowledgments
--------------

Based on the work in [https://github.com/mrzool/invoice-boilerplate](https://github.com/mrzool/invoice-boilerplate).
