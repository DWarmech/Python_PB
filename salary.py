tabs = int(input())
salary = float(input())

for open_tab in range(tabs):
    page = str(input())

    if page == "Facebook":
        salary -= 150
    elif page == "Instagram":
        salary -= 100
    elif page == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))
