import praw
import config
import responses

usrname    = config.usrname
passwd     = config.passwd
subreddit  = config.sub
commentfoot= config.comment_footer
 
def comment(submission, message):
	print("Commenting: \"" + message + "\" to the post titled: \"" + submission.title + "\"")
	submission.add_comment(message + commentfoot) 
	print("Done.")

def make_table(qa):
	table = "| Question | Answer | \n|:-----------|:-----------|\n"
	for key in qa:
		table = table + "| " + key + " | "  + qa[key]  + " |" + "\n"
	return table

def crawl():
	#repeats every 5 min. put any and all code to comment and post here.
	return

print("Setting user agent...")
r = praw.Reddit(user_agent="/r/teenagers bot created by /u/wtf_are_my_initials")
print("Done.")

print("Logging in...")
r.login(usrname, passwd)
print("Done.")

print("Selecting subreddit /r/" + subreddit)
sub = r.get_subreddit(subreddit)
print("Done.")


#I have a bash script that runs bot.py when it is needed, instead of the loop being in python.

#need better methods & stuffs here
r.submit(subreddit, "Guys ask girls and Girls ask guys weekly thread!", text='TEXT')

comment(sub.get_new(limit=1).next(), "Here are the most popular questions and answers from previous threads like this one: \n\n" + make_table(responses.girls_ask_guys))
comment(sub.get_new(limit=1).next(), "Here are the most popular questions and answers from previous threads like this one: \n\n" + make_table(responses.guys_ask_girls))
