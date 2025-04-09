#!/bin/bash
case "$1" in 
# race 1
1) python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1229/bahrain/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;
# race 2
2)  python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1230/saudi-arabia/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;
# race 3
3 )
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1231/australia/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;
# race 4
4) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1232/japan/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

5) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1233/china/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

6) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1234/miami/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

7) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1235/emilia-romagna/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

8) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1236/monaco/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

9) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1237/canada/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

10) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1238/spain/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

11) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1239/austria/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

12) 
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1240/great-britain/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

13)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1241/hungary/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

14)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1242/belgium/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

15)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1243/netherlands/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

16)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1244/italy/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

17)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1245/azerbaijan/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

18)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1246/singapore/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

19)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1247/united-states/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;


20)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1248/mexico/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

21)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1249/brazil/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

22)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1250/las-vegas/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

23)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1251/qatar/" --sprint_weekend 1
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

24)
python -m scripts.fetch_data --race_no $1 --f1_url "https://www.formula1.com/en/results/2024/races/1252/abu-dhabi/"
python -m scripts.train --race_no $1
python -m scripts.predict --race_no $1
python -m scripts.create_html --race_no $1 ;;

*)
echo "incorrect race number"
;;
esac
