from circle_stats import has_intersection

circle_1 = {"x": 6, "y": 8, "r": 5}
circle_2 = {"x": 7, "y": 15, "r": 7}
circle_3 = {"x": 5, "y": 4, "r": 2}

result = has_intersection(circle_1, circle_2, circle_3)

if result["intersects"]:
    print(f"Kruznice ss pretinaju. Pocet prienikov: {result['intersections_count']}")
else:
    print("Kruznice sa nepretinaju.")