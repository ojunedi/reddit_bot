import praw
import re
import os
from tqdm import tqdm
import time 
from datetime import datetime


def main():
    reddit = praw.Reddit('testing')

    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []


    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))


    subreddit = reddit.subreddit('memes')
    try:
        for submission in tqdm(subreddit.hot(limit=50)):
            if submission.id not in posts_replied_to:
                # searching for key word in title and making sure post is not archived or comments are disabled
                if re.search(" ", submission.title, re.IGNORECASE) and (submission.locked, submission.archived) == (False, False): 
                    submission.reply('very cool!')
                    print("Bot replying to: ", submission.title)
                    posts_replied_to.append(submission.id)
                    # print(submission.locked, submission.archived)
    except Exception as e:
        with open("errors.txt", "a") as f:
            out = f'{datetime.now()}: {e}, {submission.id}'
            f.write(out + "\n")


    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


start = time.time()

main()

print('It took {0:0.1f} seconds'.format(time.time() - start))