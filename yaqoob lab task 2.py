movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000, 72000000),
    ("Memento", 9000000, 40000000),
    ("Requiem for a Dream", 4500000, 7350000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000, 1045000000),
    ("Avengers: Age of Ultron", 365000000, 1405000000),
    ("Avengers: Endgame", 356000000, 2797800000),
    ("Incredibles 2", 200000000, 1245000000)
]

add_more = input("Do you want to add more movies? (yes/no): ")

if add_more.lower() == "yes":
    num_movies_to_add = int(input("How many movies do you want to add? "))

    for i in range(num_movies_to_add):
        movie_name = input("Enter the movie name: ")
        movie_budget = int(input("Enter the movie budget: "))
        movie_revenue = int(input("Enter the movie revenue: "))
        movies.append((movie_name, movie_budget, movie_revenue))


movie_rois = []
for movie_name, budget, revenue in movies:
    roi = ((revenue - budget) / budget) * 100  
    movie_rois.append((movie_name, roi))


movie_rois.sort(key=lambda x: x[1], reverse=True)


print("\nMovies sorted by ROI (from highest to lowest):")
for movie_name, roi in movie_rois:
    print(f"{movie_name}: ROI = {roi:.2f}%")


total_roi = sum(roi for _, roi in movie_rois)
average_roi = total_roi / len(movies)
print(f"\nAverage ROI for all movies: {average_roi:.2f}%")


high_roi_movies = [movie for movie in movie_rois if movie[1] > average_roi]
print("\nMovies with ROI higher than the average:")
for movie_name, roi in high_roi_movies:
    print(f"{movie_name}: ROI = {roi:.2f}%")
