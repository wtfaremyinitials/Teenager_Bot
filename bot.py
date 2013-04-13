import praw
import config
import responses
import re
import HTMLParser

usrname    = config.usrname
passwd     = config.passwd
subreddit  = config.sub
commentfoot= config.comment_footer
h		   = HTMLParser.HTMLParser()

def compare(a, b):
	return (h.unescape(a) == h.unescape(b))	

def make_comment(post, message):
	if(isinstance(post, praw.objects.Submission)):
		#check if this comment has already been posted
		for comment in post.comments:
			if(compare(comment.body, message + commentfoot)):
				print("Tried to make the same comment twice! Aborting!")
				return
		print("Commenting: \"" + message + "\" to the post titled: \"" + post.title + "\"")
		submission.comment(message + commentfoot) 
	elif(isinstance(post, praw.objects.Comment)):
		#check if this comment has already been posted
		for reply in post.replies:
			if(compare(reply.body, message + commentfoot)):
				print("Tried to make the same comment twice! Aborting!")
				return
		print("Replying: \"" + message + "\" to the comment: \"" + post.body + "\"")
		post.reply(message + commentfoot)
	else:
		print("Cannot respond to this type.")
	print("Done.")

def make_table(qa):
	table = "| Question | Answer | \n|:-----------|:-----------|\n"
	for key in qa:
		table = table + "| " + key + " | "  + qa[key]  + " |" + "\n"
	return table

def crawl():
	#repeats every 5 min. put any and all code to comment and post here.
	
	#go through subreddit comments
	for comment in sub.get_comments:
		parse_comment(comment)
	
	for submission in sub.get_new():
		parse_submission(submission)
	
	return

def parse_comment(comment):
	body = comment.body
	translation = translate(body)
	if(translation != ""):
		make_comment(translation)
	if(body == "/)"):
		make_comment(comment, "(\\")

#deprecated	
def parse_comments_in_submission(submission):
	for comment in submission.comments:
		parse_comment(comment)
				
def parse_submission(post):
	#translation
	translation = translate(post)
	if(translation != ""):
		make_comment(translation)
	
	#other things i might do to a post
	
def translate(text):
	comment = ""
	#translate words
	for key in responses.translator_words:
		r = key
		match = re.match(r, text, re.IGNORECASE)
		if(match != None):
			comment = comment + "\n\n > " + match + " \n\n " + responses.translator_words[key]
	#regex for US to UK year conversion.
	
	return comment			
	
def create_gender_ask_thread():
	r.submit(subreddit, "Guys ask girls and Girls ask guys weekly thread!", text='')
	make_comment(sub.get_new(limit=1).next(), "Here are the most popular questions and answers from previous threads like this one: \n\n" + make_table(responses.girls_ask_guys))
	make_comment(sub.get_new(limit=1).next(), "Here are the most popular questions and answers from previous threads like this one: \n\n" + make_table(responses.guys_ask_girls))

print("Setting user agent...")
r = praw.Reddit(user_agent="/r/teenagers bot created by /u/wtf_are_my_initials")
print("Done.")

print("Logging in...")
r.login(usrname, passwd)
print("Done.")

print("Selecting subreddit /r/" + subreddit)
sub = r.get_subreddit(subreddit)
print("Done.")

parse_comments_in_submission(sub.get_new(limit=1).next())