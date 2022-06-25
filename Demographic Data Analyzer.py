import pandas as pd
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("./adult.data.csv")

    # How many of each race are represented in this dataset? This should be a
    # Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        100 * df.loc[df["education"] == "Bachelors"].size / df.size,
        1,
    )

    # What percentage of people with advanced education (`Bachelors`, `Masters`,
    # or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[
        df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]
    lower_education = df.loc[
        ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    ]

    # percentage with salary >50K
    higher_education_rich = round(
        100
        * higher_education.loc[higher_education["salary"] == ">50K"].size
        / higher_education.size,
        1,
    )

    lower_education_rich = round(
        100
        * lower_education.loc[lower_education["salary"] == ">50K"].size
        / lower_education.size,
        1,
    )

    # What is the minimum number of hours a person works per week
    # (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per
    # week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        100
        * num_min_workers.loc[num_min_workers["salary"] == ">50K"].size
        / num_min_workers.size,
        1,
    )

    # What country has the highest percentage of people that earn >50K?
    highest_country = (
        df[["salary", "native-country"]]
        .groupby("native-country")
        .apply(lambda g: g.loc[g["salary"] == ">50K"].size / g.size * 100)
    )

    highest_earning_country = highest_country.idxmax()
    highest_earning_country_percentage = round(highest_country.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")][
            "occupation"
        ]
        .value_counts()
        .idxmax()
    )

    

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:", highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
calculate_demographic_data(False)
{'race_count': White                 27816
 Black                  3124
 Asian-Pac-Islander     1039
 Amer-Indian-Eskimo      311
 Other                   271
 Name: race, dtype: int64,
 'average_age_men': 39.4,
 'percentage_bachelors': 16.4,
 'higher_education_rich': 46.5,
 'lower_education_rich': 17.4,
 'min_work_hours': 1,
 'rich_percentage': 10.0,
 'highest_earning_country': 'Iran',
 'highest_earning_country_percentage': 41.9,
 'top_IN_occupation': 'Prof-specialty'}


import unittest


class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = calculate_demographic_data(print_data=False)

    def test_race_count(self):
        actual = self.data["race_count"].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected race count values to be [27816, 3124, 1039, 311, 271]",
        )

    def test_average_age_men(self):
        actual = self.data["average_age_men"]
        expected = 39.4
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for average age of men.",
        )

    def test_percentage_bachelors(self):
        actual = self.data["percentage_bachelors"]
        expected = 16.4
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for percentage with Bachelors degrees.",
        )

    def test_higher_education_rich(self):
        actual = self.data["higher_education_rich"]
        expected = 46.5
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for percentage with higher education that earn >50K.",
        )

    def test_lower_education_rich(self):
        actual = self.data["lower_education_rich"]
        expected = 17.4
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for percentage without higher education that earn >50K.",
        )

    def test_min_work_hours(self):
        actual = self.data["min_work_hours"]
        expected = 1
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for minimum work hours.",
        )

    def test_rich_percentage(self):
        actual = self.data["rich_percentage"]
        expected = 10
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for percentage of rich among those who work fewest hours.",
        )

    def test_highest_earning_country(self):
        actual = self.data["highest_earning_country"]
        expected = "Iran"
        self.assertEqual(
            actual,
            expected,
            "Expected different value for highest earning country.",
        )

    def test_highest_earning_country_percentage(self):
        actual = self.data["highest_earning_country_percentage"]
        expected = 41.9
        self.assertAlmostEqual(
            actual,
            expected,
            msg="Expected different value for heighest earning country percentage.",
        )

    def test_top_IN_occupation(self):
        actual = self.data["top_IN_occupation"]
        expected = "Prof-specialty"
        self.assertEqual(
            actual,
            expected,
            "Expected different value for top occupations in India.",
        )
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)        