from tracker import MetricTracker

def test_metrics():
    tracker = MetricTracker(window_size=3)
    
    tracker.add_sample(60)
    tracker.add_sample(80)
    tracker.add_sample(100)
    
    stats = tracker.get_stats()
    assert stats["moving_avg"] == 80.0
    assert stats["all_time_max"] == 100
    
    # Add a 4th sample, '60' should drop out of the window
    tracker.add_sample(120)
    stats = tracker.get_stats()
    
    # New window: [80, 100, 120] -> Avg: 100
    assert stats["moving_avg"] == 100.0
    assert stats["all_time_max"] == 120
    
    print("Metric Tracker tests: PASSED")

if __name__ == "__main__":
    test_metrics()