#! /usr/bin/python

import praw

user_agent = ("simple praw script for "
              "finding FIXED posts "
              "by Charlie Pashayan")
reddit = praw.Reddit(user_agent = user_agent)
v_fixed = []
i = 0;
first = 1
submission_generator = reddit.get_front_page(limit = 1000)
for submission in submission_generator:
    #title = submission.title
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    #print submission.title
    first = 1;
    i+=1
    print i
    for comment in flat_comments:
    	try:
    		if "le" in comment.body.lower():
    			if(comment.body):
    				if(first):
    					print "------->" + submission.title
    					first = first - 1; 
    				print "\t" +"------->"+ "\a" + comment.body
    				#v_fixed.append(comment.body)

    	except AttributeError:
    		pass
