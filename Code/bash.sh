for i in $(cat suspect.txt)
do cat /var/log/apache2/access.log | grep admin | grep $i
python3 manthan2.py
done
