from circle_stats import has_intersection

def test_two_intersections():
    circle_1 = {"x": 0, "y": 0, "r": 5}
    circle_2 = {"x": 6, "y": 0, "r": 5}
    assert has_intersection(circle_1, circle_2) == {
        "intersects": True,
        "intersections_count": 2
    }

def test_no_intersection_far_apart():
    circle_1 = {"x": 0, "y": 0, "r": 3}
    circle_2 = {"x": 10, "y": 0, "r": 3}
    assert has_intersection(circle_1, circle_2) == {
        "intersects": False,
        "intersections_count": 0
    }

def test_touching_externally():
    circle_1 = {"x": 0, "y": 0, "r": 4}
    circle_2 = {"x": 8, "y": 0, "r": 4}
    assert has_intersection(circle_1, circle_2) == {
        "intersects": True,
        "intersections_count": 1
    }

def test_touching_internally():
    circle_1 = {"x": 0, "y": 0, "r": 10}
    circle_2 = {"x": 2, "y": 0, "r": 8}
    assert has_intersection(circle_1, circle_2) == {
        "intersects": True,
        "intersections_count": 1
    }

def test_one_inside_without_touching():
    circle_1 = {"x": 0, "y": 0, "r": 10}
    circle_2 = {"x": 1, "y": 1, "r": 2}
    assert has_intersection(circle_1, circle_2) == {
        "intersects": False,
        "intersections_count": 0
    }
