from instapy import smart_run
from instapy import InstaPy

#set 
my_username = '#youruser'
my_password = '#yourpassword'


session = InstaPy(username=my_username,
                  password=my_password,
                  headless_browser=False)
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=50,
                                    min_followers=30,
                                    min_following=50)

    #settings
    session.set_do_follow(True, percentage=100)
    
    #actions
    session.set_dont_like(['#yourtag', '#yourtag', '#yourtag'])

    session.like_by_tags(['#yourtag', '#yourtag'], amount=100)
