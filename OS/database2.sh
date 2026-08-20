#!/bin/bash

echo "Welcome to the address book"

choice=0

while true
do

echo -e "\nSelect the choice\n1] Create Address Book\n2] Insert a record\n3] View/Display Address Book\n4] Delete a record\n5] Modify a record\n6] Exit"
read choice

case $choice in

"1")
    echo "Enter the file name"
    read filename
    touch "$filename"
    echo "Address Book Created Successfully"
;;

"2")
    if [ -f "$filename" ]
    then
        echo "Enter id, name, mobileno and city"
        read id name mobno city
        echo -e "$id\t$name\t$mobno\t$city" >> "$filename"
        echo "Record inserted"
    else
        echo "File does not exist, Create Address Book first"
    fi
;;

"3")
    if [ -f "$filename" ]
    then
        cat "$filename"
    else
        echo "File does not exist, Create Address Book first"
    fi
;;

"4")
    if [ -f "$filename" ]
    then
        echo "Enter the id of record you want to delete"
        read idt
        grep -v $idt $filename > tempfile
        mv tempfile $filename
        echo "Record deleted"
    else
        echo "File does not exist, Create Address Book first"
    fi
;;

"5")
    if [ -f "$filename" ]
    then
        echo "Enter the ID of the record you want to update"
        read oid

        echo "Enter the new data"
        read nid nname nmobno ncity

        sed -i "s/^$oid.*/$nid\t$nname\t$nmobno\t$ncity/" "$filename"

        echo "Record updated"
    else
        echo "File does not exist, Create Address Book first"
    fi
;;

"6")
    echo "Exiting from Program"
    exit 0
;;

*)
    echo "Invalid choice"
;;

esac

done
