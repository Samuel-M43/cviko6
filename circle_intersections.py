



from circle_stats import has_intersection

circle_1 = {"x": 0, "y": 0, "r": 5}
circle_2 = {"x": 7, "y": 0, "r": 3}

result = has_intersection(circle_1, circle_2)

if result["intersects"]:
    print(f"Kružnice se protínají. Počet průniků: {result['intersections_count']}")
else:
    print("Kružnice se neprotínají.")