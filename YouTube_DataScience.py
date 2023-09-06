import pandas as pd

# Load the dataset
file_path = '/workspaces/codespaces-blank/GlobalYouTubeStatistics.csv'
df = pd.read_csv(file_path, encoding='latin-1')

# Sort the DataFrame by subscribers
df_sorted = df.sort_values(by='subscribers', ascending=False)

# New dataset with just the top 50 creators (by sub count)
top_50_creators = df_sorted.head(50)

# New dataset with just the top 1000 creators (by sub count)
top_1000_creators = df_sorted.head(1000)

# Correlation between subscribers and views
correlation_subscribers_views_50 = top_50_creators[['subscribers', 'video views']].corr().iloc[0, 1]
correlation_subscribers_views_1000 = top_1000_creators[['subscribers', 'video views']].corr().iloc[0, 1]

print(f"The correlation between subscribers and video views for the top 50 creators is: {correlation_subscribers_views_50}")
print(f"The correlation between subscribers and video views for the top 1000 creators is: {correlation_subscribers_views_1000}")

# Correlation between views and uploads
correlation_views_uploads_50 = top_50_creators[['video views', 'uploads']].corr().iloc[0, 1]
correlation_views_uploads_1000 = top_1000_creators[['video views', 'uploads']].corr().iloc[0, 1]

print(f"The correlation between video views and uploads for the top 50 creators is: {correlation_views_uploads_50}")
print(f"The correlation between video views and uploads for the top 1000 creators is: {correlation_views_uploads_1000}")

# Correlation between views and country population
correlation_views_country_50 = top_50_creators[['video views', 'Population']].corr().iloc[0, 1]
correlation_views_country_1000 = top_1000_creators[['video views', 'Population']].corr().iloc[0, 1]

print(f"The correlation between country population and video views for the top 50 creators is: {correlation_views_country_50}")
print(f"The correlation between country population and video views for the top 1000 creators is: {correlation_views_country_1000}")
