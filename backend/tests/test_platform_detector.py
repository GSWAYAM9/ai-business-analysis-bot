from core.platform_detector import detect_platform

def test_detect_platform():
    assert detect_platform("https://instagram.com/brand") == "instagram"
    assert detect_platform("https://youtube.com/channel/abc") == "youtube"
    assert detect_platform("https://example.com") == "website"
