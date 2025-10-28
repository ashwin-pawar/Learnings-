🧹 Data Cleaning Mini Project

So first step I took was that I saw the names of students were not in proper form. We have two ways to fix it — one is replace, and the other one is what I choose. So first, I converted the names into lowercase and then into proper case using the .title() function.

Then I moved towards the age column, where I found some NaN values. The first step was to remove those null values or replace them with 0, but if we replace all NaN values with 0, it would create problems. So, I took the mean (average) value of the students and filled it in. Then those values were in float datatype, so I converted them into int using .astype(int).

Then I saw that the female and male names were not in the correct form, so I used replace because we only have two different values, and it was easy to replace.

After that, I moved to another column — grade. I found there were only 10th and 11th classes, and most of the values were in integer form, so I converted all “10th” and “11th” into 10 and 11 respectively using the .replace() function.

Then I took a mean value from math_score and filled it into the column using fillna(math_mean).
math_mean is a dictionary where I used .mean() and fillna(). Then, in the English_Score column, there were some missing values which were of object datatype, so I had to convert those into numbers. But I couldn’t convert that value into numbers because it was in string datatype and we cannot typecast it directly. So, I converted all missing values into NaN and used .mean() to take the mean value and fill it. Then I did the same with the science_score column.

Right now, I’m on the date column, and here some dates were repeating again and again but in different forms. So, I replaced those values into the same format — dd/mm/yyyy — using .replace(). The same with remarks, I replaced those values (strings) into the correct form using .replace().

📚 Libraries Used

NumPy → for numerical and mathematical operations

Pandas → for analyzing, cleaning, and manipulating data


💡 What I Learned

This project helped me build a solid grip on my foundation concepts.
I believe core skills matter the most — if your foundation is strong, you can build any logic and make any type of project.

In a Data Analyst role, we have to:

Gather data

Clean and prepare it

Make it easy to analyze and visualize

I’m confident that I can create dashboards, but cleaning data, exploring it, and finding insights is the most challenging and exciting part for me — that’s what I’m focusing on now.

🚀 My Next Step

This mini project helped me understand how to clean data properly.
After this, I won’t stop — I’ll keep doing something every single day to improve myself — building projects, creating meaningful and creative dashboards that tell a story just by looking at them.

FOR NOW, BYE!! THANKS. 🙏
