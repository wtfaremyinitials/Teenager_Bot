sub     = "test"
usrname = "teenager_bot"

#get the bot password from parent directory ;)
with open ("../passwd.txt", "r") as file:
    passwd=file.read().replace('\n', '')


comment_footer = "\n\n *This bot is still in beta. Please excuse any mistakes.* \n\n ^\([What?](http://pastebin.com/ERfMB6vU)\) ^\([Who?](http://reddit.com/u/wtf_are_my_initials)) ^\([Issue?](http://www.reddit.com/message/compose/?to=wtf_are_my_initials&subject=teenager_bot%20has%20said%20something%20inaccurate%20or%20offensive.&message=Please%20include%20what%20message%20you%20would%20like%20removed%20and%20why%20you%20want%20it%20removed)) ^\([Code?](http://www.github.com/)\)"
