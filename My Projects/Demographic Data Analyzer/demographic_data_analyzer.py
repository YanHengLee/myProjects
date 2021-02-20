import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    races = df["race"].value_counts()
    race_count = pd.Series(data=races.values, index=[races.index])  # Change it to Pandas Series

    # What is the average age of men?
    men_chart = df[df.ne("Female").all(axis=1)]
    average_age_men = round(men_chart["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_counts = (df["education"] == "Bachelors").sum()
    education_total = df["education"].count()
    percentage_bachelors = round((bachelor_counts / education_total) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # with `Bachelors`, `Masters`, or `Doctorate`
    advance_education = df.loc[df["education"].str.contains("Bachelors|Masters|Doctorate")]
    adv_high_salary = advance_education.loc[advance_education["salary"].str.contains(">50K")]
    higher_education_count = adv_high_salary["salary"].count()
    # What percentage of people without advanced education make more than 50K?
    # without `Bachelors`, `Masters`, or `Doctorate`
    low_education = df.loc[~df["education"].str.contains("Bachelors|Masters|Doctorate")]
    low_high_salary = low_education.loc[low_education["salary"].str.contains(">50K")]
    low_high_salary_count = low_high_salary["salary"].count()
    # percentage with salary >50K
    all_high_salary = advance_education["salary"].count()
    all_low_salary = low_education["salary"].count()
    higher_education_rich = round(higher_education_count / all_high_salary * 100, 1)
    lower_education_rich = round(low_high_salary_count / all_low_salary * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_rich = df.loc[(df["hours-per-week"] == 1) & (df["salary"] == ">50K")]
    all_min_hours = df.loc[df["hours-per-week"] == 1]
    num_min_workers_rich = len(min_hours_rich.index)
    rich_percentage = round((num_min_workers_rich / len(all_min_hours.index)) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    all_salary = df.loc[df["salary"] == ">50K"]
    high_country_count = all_salary["native-country"].value_counts()
    country_count = df["native-country"].value_counts()
    highest_earning_country = (high_country_count / country_count).idxmax()
    highest_earning_country_percentage = round((high_country_count / country_count).max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_salary_indians = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    occupation_count = high_salary_indians["occupation"].value_counts()
    top_IN_occupation = occupation_count.idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
