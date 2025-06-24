import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the data
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Advanced education vs >50K
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced)]
    lower_edu = df[~df['education'].isin(advanced)]

    higher_edu_rich = round((higher_edu[higher_edu['salary'] == '>50K'].shape[0] / higher_edu.shape[0]) * 100, 1)
    lower_edu_rich = round((lower_edu[lower_edu['salary'] == '>50K'].shape[0] / lower_edu.shape[0]) * 100, 1)

    # 5. Min hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. % earning >50K among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    # 7. Country with highest % of >50K earners
    country_group = df.groupby('native-country')['salary']
    rich_country_pct = (country_group.apply(lambda x: (x == '>50K').sum() / x.count()) * 100).round(1)
    highest_earning_country = rich_country_pct.idxmax()
    highest_earning_country_percentage = rich_country_pct.max()

    # 8. Most common job in India for >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Build return dictionary
    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    # Print if needed
    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result
