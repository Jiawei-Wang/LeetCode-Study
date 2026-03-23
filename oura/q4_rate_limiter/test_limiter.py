from rate_limiter import RateLimiter
import time

def test_rate_limiter():
    # Allow 3 requests every 2 seconds
    limiter = RateLimiter(max_requests=3, window_seconds=2)
    user = "user_123"

    # First 3 should pass
    assert limiter.is_allowed(user) is True
    assert limiter.is_allowed(user) is True
    assert limiter.is_allowed(user) is True
    
    # 4th should fail
    assert limiter.is_allowed(user) is False

    print("Initial limit test: PASSED")

    # Wait for window to clear
    print("Waiting for window to expire...")
    time.sleep(2.1)
    
    # Should pass again
    assert limiter.is_allowed(user) is True
    print("Window reset test: PASSED")

if __name__ == "__main__":
    test_rate_limiter()