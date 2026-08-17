#!/bin/bash
echo "Welcome to the address book"

choice=0


while true  #this is the practice
do

echo -e "\nSelect the choice\n1]Create Address Book.\n2]Insert a record\n3]View/Display Address Book..\n4]Delete a record.\n5]Modify a record.\n6]Exit"
read choice

case $choice in

"1")
echo -e "Enter the file name"
read filename
touch $filename
echo -e "Address Book Created Successfully"
;;


"2")
if [ -f "$filename" ]
then
echo -e "Enter id , name , mobileno and city"
read id name mobno city
echo -e "$id\t$name\t$mobno\t$city" >> $filename
echo "Record inserted"
else
    echo "File doesnot exist , Create Address Book first"
fi
;;


"3")
if [ -f "$filename" ]
then
cat $filename
else
    echo "File doesnot exist , Create Address Book First"
fi
;;


"4")
if [ -f "$filename" ]
then
    echo -e "Enter the id of record you want to delete"	#or sed -i  $filename
    read idt
    grep -v $idt $filename > tempfile
    mv tempfile $filename
    cat $filename
else
    echo "File doesnot exist , Create Address Book First"
fi

;;

"5")
if [ -f "$filename" ]
then
echo -e "Enter the record u want to update"
read oid oname omobno ocity

echo -e "Enter the new data"
read nid nname nmobno ncity

sed -i "s/$oid $oname $omobno $ocity/$nid $nname $nmobno $ncity/" "$filename"
else
    echo "File doesnot exist , Create Address Book first"
fi
;;

"6")
echo -e "Exiting from Program"
exit 0  #it is the bash's exit cmd
;;


*)
echo "Invalid choice"
;;

esac

done	# while loop ends
