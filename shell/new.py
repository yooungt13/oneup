#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author: youngtian

name = raw_input("Enter file name: ")
title = raw_input("Enter title: ")
tags = raw_input("Enter tags(split by ','): ")
more = raw_input("Enter more content: ")

# create post
fo = open("../_posts/"+name, "wb")
fo.write( "---\n\
layout: post\n\
title: " + title.title() + "\n\
tag: [" + tags + "]\n\
addr: Meituan, Beijing\n\
description: " + title.title() + "\n\
keywords: " + tags.lower() + ",有田十三\n\
---\n\n\
" + more + "\n\n\
<!--more-->\n")

fo.close()

# create tag
for tag in tags.split(','):
	tag = tag.strip()
	fo = open("../tags/" + tag.lower() + ".md", "wb")
	fo.write("---\n\
layout: tags\n\
title: Hello 13 | " + tag.title() + "\n\
tag: " + tag.title() + "\n\
permalink: /tags/" + tag.lower() + "/\n\
---\n")
	fo.close()

print "New post completed."
