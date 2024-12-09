import pytest
from BuzzNewsFeed.BuzzNewsFeed import Buzz_newsfeed

@pytest.mark.usefixtures("setup")
class TestBuzz:
    def test_post_text(self):
        q=Buzz_newsfeed(self.driver)
        q.buzz_post_text("hi im kannan")

    @pytest.mark.xfail
    def test_post_pic(self):
        w = Buzz_newsfeed(self.driver)
        photo_path = r"C:\Users\senthamarai.kannan\PycharmProjects\page object model\testcases\frog.jpg"
        w.buzz_share_post(photo_path)

    def test_post_video(self):
        w = Buzz_newsfeed(self.driver)
        video_path= r"https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        w.buzz_share_video("You got Rick rolled", video_path)

